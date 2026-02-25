; =========================
; CLASS DEFINITIONS
; =========================
(class_definition
  name: (identifier) @class.name) @definition.class

; =========================
; FUNCTION DEFINITIONS
; =========================
(function_definition
  name: (identifier) @function.name) @definition.function

; =========================
; VARIABLE DEFINITIONS
; =========================
(assignment
  left: (identifier) @variable.name) @definition.variable

; =========================
; FUNCTION CALLS
; =========================
(call
  function: [
    (identifier) @call.name
    (attribute attribute: (identifier) @call.name)
  ]) @reference.call