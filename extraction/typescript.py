from tree_sitter import QueryCursor
from core.entity import Entity
from extraction.capture_mapper import CAPTURE_TYPE_MAP
from extraction.base import BaseExtractor


class TypeScriptExtractor(BaseExtractor):

    def extract(self, tree, source, file_path):
        entities = []

        cursor = QueryCursor(self.query)
        captures = cursor.captures(tree.root_node)

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

        return entities, []