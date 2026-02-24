class Calculator
  def initialize(a, b)
    @a = a
    @b = b
  end

  def add
    @a + @b
  end
end

def square(x)
  x * x
end

calc = Calculator.new(5, 3)
result = calc.add
puts result