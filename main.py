from core.graph import CodeGraph
from scanning.file_scanner import scan_directory
from parsing.parser_factory import parse_source
from parsing.query_loader import load_query
from extraction.generic_extractor import extract
from serialization.json_serializer import export_graph


def main(project_path):
    graph = CodeGraph()

    for file_path, language, source in scan_directory(project_path):

        tree, language_obj = parse_source(language, source)

        query = load_query(language, language_obj)

        entities, relationships = extract(
            tree, source, file_path, query
        )

        for e in entities:
            graph.add_entity(e)

        for r in relationships:
            graph.add_relationship(r)

    export_graph(graph)


if __name__ == "__main__":
    main("test_project")