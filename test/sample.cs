// Test.cs
using System;

namespace Demo
{
    class Calculator
    {
        private int a;
        private int b;

        public Calculator(int a, int b)
        {
            this.a = a;
            this.b = b;
        }

        public int Add()
        {
            return a + b;
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Calculator calc = new Calculator(5, 3);
            int result = calc.Add();
            Console.WriteLine(result);
        }
    }
}