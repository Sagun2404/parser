; =========================
; Includes
; =========================
(preproc_include
  path: (_) @name.import) @definition.import

; =========================
; Function Definitions
; =========================
(function_definition
  declarator: (function_declarator
    declarator: (identifier) @name.definition.function)) @definition.function

; =========================
; Struct Definitions
; =========================
(struct_specifier
  name: (type_identifier) @name.definition.struct) @definition.struct

; =========================
; Variable Declarations
; =========================
(declaration
  declarator: (init_declarator
    declarator: (identifier) @name.definition.variable)) @definition.variable

; =========================
; Function Calls
; =========================
(call_expression
  function: (identifier) @name.reference.call) @expression.call

; =========================
; Assignments
; =========================
(assignment_expression
  left: (identifier) @name.definition.variable
  right: (_) @expression.value) @statement.assignment