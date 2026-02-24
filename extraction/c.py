# extraction/c_extractor.py

from tree_sitter import QueryCursor
from core.entity import Entity
from core.relationship import Relationship
from extraction.capture_mapper import CAPTURE_TYPE_MAP
from extraction.base import BaseExtractor


class CExtractor(BaseExtractor):

    def extract(self, tree, source, file_path):
        entities = []
        relationships = []

        cursor = QueryCursor(self.query)
        captures = cursor.captures(tree.root_node)

        node_entity_map = {}

        # ------------------------
        # PASS 1 — CREATE ENTITIES
        # ------------------------
        for capture_name, nodes in captures.items():

            entity_type = CAPTURE_TYPE_MAP.get(capture_name)
            if not entity_type:
                continue

            for node in nodes:
                name = source[node.start_byte: node.end_byte]

                entity = Entity(
                    type=entity_type,
                    name=name,
                    file=file_path,
                    start_line=node.start_point[0] + 1,
                    end_line=node.end_point[0] + 1,
                )

                entities.append(entity)
                node_entity_map[node.id] = entity

        # ------------------------
        # PASS 2 — PARENT-CHILD LINKING
        # ------------------------
        ALLOWED_PARENTS = [
            "function",
            "struct",
            "enum",
        ]

        for node_id, entity in node_entity_map.items():

            node = tree.root_node.descendant_for_byte_range(
                entity.start_line - 1,
                entity.end_line - 1,
            )

            parent = node.parent
            while parent:

                parent_entity = node_entity_map.get(parent.id)

                if parent_entity and parent_entity.type in ALLOWED_PARENTS:
                    entity.parent_id = parent_entity.id

                    relationships.append(
                        Relationship(
                            source_id=parent_entity.id,
                            target_id=entity.id,
                            type="defines",
                        )
                    )
                    break

                parent = parent.parent

        return entities, relationships