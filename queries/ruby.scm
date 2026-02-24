; =========================
; Class Definition
; =========================
(class
  name: (constant) @name.definition.class) @definition.class


; =========================
; Method Definition
; =========================
(method
  name: (identifier) @name.definition.method) @definition.method


; =========================
; Method Parameters
; =========================
(method
  parameters: (method_parameters
    (identifier) @name.definition.parameter))


; =========================
; Instance Variables (@a, @b)
; =========================
(instance_variable) @name.definition.field


; =========================
; Local Variable Assignment
; =========================
(assignment
  left: (identifier) @name.definition.variable
  right: (_) @expression.value) @statement.assignment


; =========================
; Instance Variable Assignment
; =========================
(assignment
  left: (instance_variable) @name.definition.field
  right: (identifier) @reference.symbol) @statement.assignment


; =========================
; Object Creation (Calculator.new)
; =========================
(call
  receiver: (constant) @name.reference.class
  method: (identifier) @name.reference.method) @expression.object_creation


; =========================
; Method Call on Variable (calc.add)
; =========================
(call
  receiver: (identifier) @reference.object
  method: (identifier) @name.reference.method) @expression.method_call


; =========================
; Standalone Call (puts result)
; =========================
(call
  method: (identifier) @name.reference.call) @expression.call


; =========================
; Binary Expression
; =========================
(binary
  left: (_) @reference.left
  right: (_) @reference.right) @expression.binary


; =========================
; Integer Literals
; =========================
(integer) @constant.integer