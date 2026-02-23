class CodeGraph:
    def __init__(self):
        self.entities = {}
        self.relationships = []

    def add_entity(self, entity):
        self.entities[entity.id] = entity

    def add_relationship(self, relationship):
        self.relationships.append(relationship)

    def to_dict(self):
        return {
            "entities": [e.to_dict() for e in self.entities.values()],
            "relationships": [r.to_dict() for r in self.relationships],
        }