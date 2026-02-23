class Relationship:
    def __init__(self, source_id: str, target_id: str, type: str):
        self.source_id = source_id
        self.target_id = target_id
        self.type = type

    def to_dict(self):
        return {
            "source": self.source_id,
            "target": self.target_id,
            "type": self.type,
        }