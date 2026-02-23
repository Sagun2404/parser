; Function definitions
(function_definition
  name: (identifier) @definition.function)

; Class definitions
(class_definition
  name: (identifier) @definition.class)

; Function calls
(call
  function: (identifier) @reference.call)

; Imports
(import_statement
  name: (dotted_name) @import.statement)

(import_from_statement
  module_name: (dotted_name) @import.statement)