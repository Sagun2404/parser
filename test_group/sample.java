// Test.java

import java.util.List;

public class Calculator {

    private int a;
    private int b;

    public Calculator(int a, int b) {
        this.a = a;
        this.b = b;
    }

    public int add() {
        return a + b;
    }

    public static void main(String[] args) {
        Calculator calc = new Calculator(5, 3);
        int result = calc.add();
        System.out.println(result);
    }
}