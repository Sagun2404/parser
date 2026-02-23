; Function declarations
(function_declaration
  name: (identifier) @definition.function)

; Class declarations
(class_declaration
  name: (type_identifier) @definition.class)

; Method definitions inside classes
(method_definition
  name: (property_identifier) @definition.method)

; Function calls
(call_expression
  function: (identifier) @reference.call)

; Imports
(import_statement
  source: (string) @import.statement)