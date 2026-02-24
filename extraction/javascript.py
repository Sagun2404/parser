from tree_sitter import QueryCursor
from core.entity import Entity
from core.relationship import Relationship
from extraction.capture_mapper import CAPTURE_TYPE_MAP
from extraction.base import BaseExtractor


class JavaScriptExtractor(BaseExtractor):

    def extract(self, tree, source, file_path):
        entities = []
        relationships = []

        cursor = QueryCursor(self.query)
        captures = cursor.captures(tree.root_node)

        node_entity_map = {}

        # -------------------------
        # Create entities
        # -------------------------
        for capture_name, nodes in captures.items():
            entity_type = CAPTURE_TYPE_MAP.get(capture_name)
            if not entity_type:
                continue

            for node in nodes:
                name = source[node.start_byte:node.end_byte]

                entity = Entity(
                    type=entity_type,
                    name=name,
                    file=file_path,
                    start_line=node.start_point[0] + 1,
                    end_line=node.end_point[0] + 1,
                )

                entities.append(entity)
                node_entity_map[node.id] = entity

        # -------------------------
        # Parent-child linking
        # -------------------------
        for entity in entities:
            node = tree.root_node.descendant_for_byte_range(
                entity.start_byte if hasattr(entity, "start_byte") else 0,
                entity.end_byte if hasattr(entity, "end_byte") else 0,
            )

            parent = node.parent if node else None

            while parent:
                parent_entity = node_entity_map.get(parent.id)
                if parent_entity:
                    entity.parent_id = parent_entity.id
                    relationships.append(
                        Relationship(
                            source_id=parent_entity.id,
                            target_id=entity.id,
                            type="defines"
                        )
                    )
                    break
                parent = parent.parent

        return entities, relationships