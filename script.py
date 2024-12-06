def prime_factorization(number):
    factors = []
    divisor = 2
    while divisor * divisor <= number:
        while number % divisor == 0:
            factors.append(divisor)
            number //= divisor
        divisor += 1
    if number > 1:
        factors.append(number)
    return factors


def point(is_correct):
    score = 0
    if is_correct:
        score += 1


def main():
    while True:
        number = input("Enter a number (or press Enter to quit): ")
        if number == "":
            break
        try:
            num = int(number)
            print(f"Prime factors of {num}: {prime_factorization(num)}")
        except ValueError:
            print("Please enter a valid integer.")


if __name__ == "__main__":
    main()
