import os


def load_query(language, language_obj):
    query_path = os.path.join("queries", f"{language}.scm")

    with open(query_path, "r", encoding="utf-8") as f:
        query_str = f.read()
   
   
    return language_obj.query(query_str)