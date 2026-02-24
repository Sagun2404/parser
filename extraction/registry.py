from extraction.python import PythonExtractor
from extraction.typescript import TypeScriptExtractor
from extraction.c import CExtractor
from extraction.javascript import JavaScriptExtractor 
from extraction.java import JavaExtractor
from extraction.cpp import CppExtractor
from extraction.ruby import RubyExtractor
from extraction.rust import RustExtractor
from extraction.go import GoExtractor
from extraction.c_sharp import CSharpExtractor
from extraction.cpp import CppExtractor

EXTRACTOR_REGISTRY = {
    "python": PythonExtractor(),
    "typescript": TypeScriptExtractor(),
    "c": CExtractor(),
    "javascript": JavaScriptExtractor(), 
    "java": JavaExtractor(), 
    "cpp": CppExtractor(),  
    "ruby": RubyExtractor(),
    "rust": RustExtractor(),
    "go": GoExtractor(),
    "csharp": CSharpExtractor(),
    
}