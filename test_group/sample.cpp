#include <iostream>

class Calculator {
public:
    int add(int a, int b) {
        return a + b;
    }
};

int main() {
    Calculator calc;
    int result = calc.add(2, 3);
    std::cout << result << std::endl;
    return 0;
}