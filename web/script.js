const primeFactor = (number) => {
    factors = [];
    divisor = 2;
    while (divisor * divisor <= number) {
        while (number % divisor == 0) {
            factors.push(divisor);
            number /= divisor;
        };
        divisor += 1;
    };
    if (number > 1) factors.push(number);
    return factors;
};

const addEvent = () => {
    const input = document.getElementById('input');
    input.addEventListener('input', () => {
        const output = document.querySelector('h1');
        output.textContent = '';
        const factors = primeFactor(input.value);
        factors.forEach(prime => {
            output.textContent += prime + ' × ';
        });
        output.textContent = output.textContent.slice(0, -3);
    });
};

window.addEventListener('DOMContentLoaded', () => {
    addEvent();
});