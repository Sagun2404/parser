class BaseExtractor:
    def extract(self, tree, source: str, file_path: str):
        raise NotImplementedError