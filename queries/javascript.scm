; =========================
; Comments
; =========================
(comment) @comment

; =========================
; Function Definition
; =========================
(function_declaration
  name: (identifier) @name.definition.function) @definition.function

; Function Parameters
(function_declaration
  parameters: (formal_parameters
    (identifier) @name.definition.parameter))

; =========================
; Return Statement
; =========================
(return_statement) @statement.return

; =========================
; Binary Expression
; =========================
(binary_expression
  left: (identifier) @reference.left
  right: (identifier) @reference.right) @expression.binary

; =========================
; Variable Declaration (let/const)
; =========================
(variable_declarator
  name: (identifier) @name.definition.variable) @definition.variable

; =========================
; Function Call
; =========================
(call_expression
  function: (identifier) @name.reference.call) @expression.call

; Method Call (console.log)
; =========================
(call_expression
  function: (member_expression
    object: (identifier) @reference.object
    property: (property_identifier) @name.reference.method)) @expression.method_call

; =========================
; Numbers
; =========================
(number) @constant.number