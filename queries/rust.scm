; =========================
; Comment
; =========================
(line_comment) @comment


; =========================
; Struct Definition
; =========================
(struct_item
  name: (type_identifier) @name.definition.struct) @definition.struct


; =========================
; Struct Fields
; =========================
(field_declaration
  name: (field_identifier) @name.definition.field) @definition.field


; =========================
; Impl Block
; =========================
(impl_item
  type: (type_identifier) @name.reference.struct) @definition.impl


; =========================
; Function Definition (Top-level)
; =========================
(function_item
  name: (identifier) @name.definition.function) @definition.function


; =========================
; Method Definition (inside impl)
; =========================
(function_item
  name: (identifier) @name.definition.method)


; =========================
; Parameters
; =========================
(parameter
  pattern: (identifier) @name.definition.parameter)


; =========================
; Self Parameter
; =========================
(self_parameter) @name.definition.parameter


; =========================
; Let Declarations
; =========================
(let_declaration
  pattern: (identifier) @name.definition.variable) @definition.variable


; =========================
; Associated Function Call (Calculator::new)
; =========================
(call_expression
  function: (scoped_identifier
    path: (identifier) @reference.scope
    name: (identifier) @name.reference.call)) @expression.call


; =========================
; Method Call (calc.add())
; =========================
(call_expression
  function: (field_expression
    value: (identifier) @reference.object
    field: (field_identifier) @name.reference.method)) @expression.method_call


; =========================
; Field Access (self.a)
; =========================
(field_expression
  value: (self)
  field: (field_identifier) @name.reference.field) @expression.field_access


; =========================
; Binary Expression
; =========================
(binary_expression
  left: (_) @reference.left
  right: (_) @reference.right) @expression.binary


; =========================
; Struct Construction
; =========================
(struct_expression
  name: (type_identifier) @name.reference.struct) @expression.struct_init


; =========================
; Macro Invocation (println!)
; =========================
(macro_invocation
  macro: (identifier) @name.reference.macro) @expression.macro


; =========================
; Literals
; =========================
(integer_literal) @constant.integer
(string_literal) @constant.string