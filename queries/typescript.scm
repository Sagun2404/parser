; =========================
; CLASS DEFINITIONS
; =========================
(class_declaration
  name: (type_identifier) @definition.class)

; =========================
; METHOD DEFINITIONS
; =========================
(method_definition
  name: (property_identifier) @definition.method)

; =========================
; FUNCTION DEFINITIONS
; =========================
(function_declaration
  name: (identifier) @definition.function)

; =========================
; VARIABLE DEFINITIONS
; =========================
(variable_declarator
  name: (identifier) @definition.variable)

; =========================
; FUNCTION CALLS
; =========================
(call_expression
  function: (identifier) @reference.call)

(call_expression
  function: (member_expression
    property: (property_identifier) @reference.call))