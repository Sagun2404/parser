from tree_sitter import Parser
from parsing.language_registry import load_language


def parse_source(language_name, source_code):
    language = load_language(language_name)
    parser = Parser(language)
   

    tree = parser.parse(bytes(source_code, "utf8"))
    return tree, language