; =========================
; Comments
; =========================
(line_comment) @comment

; =========================
; Import Declaration
; =========================
(import_declaration
  (scoped_identifier) @name.import) @definition.import

; =========================
; Class Definition
; =========================
(class_declaration
  name: (identifier) @name.definition.class) @definition.class

; =========================
; Field Declarations
; =========================
(field_declaration
  declarator: (variable_declarator
    name: (identifier) @name.definition.field)) @definition.field

; =========================
; Constructor Definition
; =========================
(constructor_declaration
  name: (identifier) @name.definition.constructor) @definition.constructor

; Constructor Parameters
(constructor_declaration
  parameters: (formal_parameters
    (formal_parameter
      name: (identifier) @name.definition.parameter)))

; =========================
; Method Definitions
; =========================
(method_declaration
  name: (identifier) @name.definition.method) @definition.method

; Method Parameters
(method_declaration
  parameters: (formal_parameters
    (formal_parameter
      name: (identifier) @name.definition.parameter)))

; =========================
; Local Variables
; =========================
(local_variable_declaration
  declarator: (variable_declarator
    name: (identifier) @name.definition.variable)) @definition.variable

; =========================
; Object Creation (new Calculator)
; =========================
(object_creation_expression
  type: (type_identifier) @name.reference.class) @expression.object_creation

; =========================
; Method Invocation
; =========================
(method_invocation
  name: (identifier) @name.reference.call) @expression.call

; Method Invocation With Object
(method_invocation
  object: (identifier) @reference.object
  name: (identifier) @name.reference.method) @expression.method_call

; =========================
; Field Access (this.a)
; =========================
(field_access
  field: (identifier) @name.reference.field) @expression.field_access

; =========================
; Assignment
; =========================
(assignment_expression
  left: (_) @reference.left
  right: (_) @reference.right) @statement.assignment

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
; Integer Literals
; =========================
(decimal_integer_literal) @constant.integer