; =========================
; CLASS DEFINITIONS
; =========================
(class_definition
  name: (identifier) @definition.class)

; =========================
; FUNCTION DEFINITIONS
; =========================
(function_definition
  name: (identifier) @definition.function)

; =========================
; VARIABLE DEFINITIONS
; =========================
(assignment
  left: (identifier) @definition.variable)

; =========================
; IMPORTS
; =========================
(import_statement
  name: (dotted_name
          (identifier) @reference.import))

; =========================
; FUNCTION CALLS
; =========================
(call
  function: (identifier) @reference.call)

(call
  function: (attribute
              attribute: (identifier) @reference.call))