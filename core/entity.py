import uuid


class Entity:
    def __init__(
        self,
        type: str,
        name: str,
        file: str,
        start_line: int,
        end_line: int,
        signature: str | None = None,
        parent_id: str | None = None,
        metadata: dict | None = None,
    ):
        self.id = str(uuid.uuid4())
        self.type = type
        self.name = name
        self.file = file
        self.start_line = start_line
        self.end_line = end_line
        self.signature = signature
        self.parent_id = parent_id
        self.metadata = metadata or {}

    def to_dict(self):
        return self.__dict__