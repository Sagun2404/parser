from extraction.python import PythonExtractor
from extraction.typescript import TypeScriptExtractor


EXTRACTOR_REGISTRY = {
    "python": PythonExtractor(),
    "typescript": TypeScriptExtractor(),
}