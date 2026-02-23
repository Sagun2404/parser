; Function declarations
(function_declaration
  name: (identifier) @definition.function)

; Interface/Class declarations
(class_declaration
  name: (identifier) @definition.class)

(interface_declaration
  name: (identifier) @definition.interface)

; Function calls
(call_expression
  function: (identifier) @reference.call)


