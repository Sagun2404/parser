; =========================
; Include
; =========================
(preproc_include
  path: (system_lib_string) @name.import) @definition.import


; =========================
; Class Definition
; =========================
(class_specifier
  name: (type_identifier) @name.definition.class) @definition.class


; =========================
; Method Definition (inside class)
; =========================
(function_definition
  declarator: (function_declarator
    declarator: (field_identifier) @name.definition.method)) @definition.method


; Method Parameters
(parameter_declaration
  declarator: (identifier) @name.definition.parameter)


; =========================
; Top-level Function
; =========================
(function_definition
  declarator: (function_declarator
    declarator: (identifier) @name.definition.function)) @definition.function


; =========================
; Variable Declaration
; =========================
(declaration
  declarator: (identifier) @name.definition.variable) @definition.variable


; Initialized Variable
(declaration
  declarator: (init_declarator
    declarator: (identifier) @name.definition.variable)) @definition.variable


; =========================
; Method Call (obj.add())
; =========================
(call_expression
  function: (field_expression
    argument: (identifier) @reference.object
    field: (field_identifier) @name.reference.method)) @expression.method_call


; =========================
; Namespace-qualified access (std::cout)
; =========================
(qualified_identifier
  scope: (namespace_identifier) @reference.namespace
  name: (identifier) @name.reference.symbol) @expression.qualified


; =========================
; Return Statement
; =========================
(return_statement) @statement.return


; =========================
; Binary Expression
; =========================
(binary_expression
  left: (_) @reference.left
  right: (_) @reference.right) @expression.binary


; =========================
; Number Literals
; =========================
(number_literal) @constant.number