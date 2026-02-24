class Calculator {
    add(a: number, b: number): number {
        return a + b;
    }
}

function square(x: number): number {
    return Math.sqrt(x);
}

const result = square(10);
console.log(result);