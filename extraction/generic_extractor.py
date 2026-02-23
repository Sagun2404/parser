from tree_sitter import QueryCursor
# Assuming Entity and CAPTURE_TYPE_MAP are defined
from core.entity import Entity
from extraction.capture_mapper import CAPTURE_TYPE_MAP


def extract(tree, source, file_path, query):
    entities = []
    relationships = []

    cursor = QueryCursor(query)  # query in constructor
    captures = cursor.captures(tree.root_node)  # dict {name: [nodes]}

    for capture_name, nodes in captures.items():  # No manual grouping needed!
        entity_type = CAPTURE_TYPE_MAP.get(capture_name)
        if not entity_type:
            continue

        for node in nodes:
            name = node.text.decode('utf8')
            entity = Entity(
                type=entity_type,
                name=name,
                file=file_path,
                start_line=node.start_point[0] + 1,
                end_line=node.end_point[0] + 1,
            )
            entities.append(entity)

    return entities, relationships

