import os


EXTENSION_LANGUAGE_MAP = {
    ".py": "python",
    ".js": "javascript",
    ".ts": "typescript",
    ".cpp": "cpp",
    ".c": "c",
    ".rs": "rust",
    ".go": "go",
    ".java": "java",
    ".cs": "csharp",
    ".rb": "ruby",
}


def scan_directory(root_path):
    for root, _, files in os.walk(root_path):
        for file in files:
            ext = os.path.splitext(file)[1]
            language = EXTENSION_LANGUAGE_MAP.get(ext)

            if not language:
                continue

            file_path = os.path.join(root, file)

            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                source = f.read()

            yield file_path, language, source