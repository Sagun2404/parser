import os

from core.graph import CodeGraph
from scanning.file_scanner import scan_directory
from parsing.parser_factory import parse_source
from parsing.query_loader import load_query
from extraction.registry import EXTRACTOR_REGISTRY
from serialization.json_serializer import export_graph
from analyzer.call_graph_builder import build_call_graph
from tree_sitter_language_pack import get_language, get_parser
def main(project_path: str):
  


    try:
        csharp_lang = get_language("")
        print("✅ HTML is supported as 'node'")
    except ValueError:
     print("❌ Language not found")
    
    graph = CodeGraph()

    for file_path, language, source in scan_directory(project_path):
    
       
        print(f"Processing file: {file_path}")
        print(f"Detected language: {language}")

        try:
            # Parse source
            tree, language_obj = parse_source(language, source)
            print(f"Parsed AST for {file_path}")
            print("========== AST ==========")
            print(tree.root_node)
            print("=========================")

            # Load query
            query = load_query(language, language_obj)
            print(f"Loaded query for {language}")
            print("========== QUERY ==========")
            print(query)
            # Get language-specific extractor
            extractor = EXTRACTOR_REGISTRY.get(language)
            print(f"Using extractor: {extractor.__class__.__name__}" if extractor else "No extractor found")
            if not extractor:
                print(f"No extractor found for language: {language}")
                continue

            # Inject query into extractor
            extractor.query = query

            # Extract entities and relationships
            entities, relationships = extractor.extract(
                tree, source, file_path
            )
            
            relationships = build_call_graph(entities, relationships)

            # Add to graph
            for entity in entities:
                graph.add_entity(entity)

            for relationship in relationships:
                graph.add_relationship(relationship)

        except Exception as e:
            print(f"Error processing {file_path}")
            print(f"Reason: {e}")
            continue

    # Export final graph
    output_path = os.path.join(os.getcwd(), "output.json")
    export_graph(graph, output_path)

    print("\nAnalysis complete.")
    print(f"Output written to: {output_path}")


if __name__ == "__main__":
    # Change this to your test directory
    main("test")