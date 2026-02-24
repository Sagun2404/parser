
from tree_sitter_language_pack import get_language

SUPPORTED_LANGUAGES = {
    "python": "python",
    "javascript": "javascript",
    "typescript": "typescript",
    "cpp": "cpp",
    "c": "c",
    "rust": "rust",
    "go": "go",
    "java": "java",
    "csharp": "csharp",
    "ruby": "ruby",
}


def load_language(language_name):
    
    return get_language(SUPPORTED_LANGUAGES[language_name])
