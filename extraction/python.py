from tree_sitter import QueryCursor
from core.entity import Entity
from core.relationship import Relationship
from extraction.capture_mapper import CAPTURE_TYPE_MAP
from extraction.base import BaseExtractor

class PythonExtractor(BaseExtractor):

    def extract(self, tree, source, file_path):
        entities = []
        relationships = []
        
        # This map links AST Node IDs to our Entity objects
        node_entity_map = {}
        # This map stores the actual tree-sitter node objects for later traversal
        node_storage = {}

        cursor = QueryCursor(self.query)
        captures = cursor.captures(tree.root_node)

        # 1. First Pass: Create Entities
        for capture_name, nodes in captures.items():
            # We only create entities for the "container" nodes (definitions/references)
            # We ignore the ".name" auxiliary tags in this loop
            if not capture_name.startswith(('definition', 'reference')):
                continue

            entity_type = CAPTURE_TYPE_MAP.get(capture_name)
            if not entity_type:
                continue

            for node in nodes:
                # Logic to find the 'name' of the entity
                # We check for a child with the field 'name' (common in tree-sitter-python)
                # or fallback to the node's own text
                name_node = node.child_by_field_name('name')
                if name_node:
                    name = source[name_node.start_byte:name_node.end_byte]
                else:
                    # Fallback: find any identifier child or use the node's text
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
                node_storage[node.id] = node

        # 2. Second Pass: Parent-Child Linking (The "Defines" Relationship)
        for node_id, entity in node_entity_map.items():
            current_node = node_storage.get(node_id)
            if not current_node:
                continue

            # Walk up the AST to find the nearest parent that is also an entity
            parent = current_node.parent
            while parent:
                if parent.id in node_entity_map:
                    parent_entity = node_entity_map[parent.id]
                    
                    # Update the entity metadata
                    entity.parent_id = parent_entity.id
                    
                    # Create the formal relationship
                    relationships.append(
                        Relationship(
                            source_id=parent_entity.id,
                            target_id=entity.id,
                            type="defines"
                        )
                    )
                    # Stop at the first valid parent found
                    break
                parent = parent.parent

        return entities, relationships