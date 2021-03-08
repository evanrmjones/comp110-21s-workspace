"""EX03 - prime functions."""


__author__: str = "YOUR PID HERE"


def main() -> None:
    """Entrypoint of the program."""
    # Put print statements here to test your function
    # ex. print(is_prime(5)), print(list_primes(10, 20))
    print(list_primes(3, 7))   


def is_prime(num: int) -> bool: 
    """Determines if a number is prime."""
    for i in range(1, num, 2):
        if num % i == 0 and i != 1 or num % 2 == 0:
            return False 
    else: 
        return True


def list_primes(num1: int, num2: int) -> list[int]: 
    """Determines if a range of numers is prime."""
    prime_range: range = range(num1, num2)
    prime_nums: list[int] = []
    for i in prime_range: 
        if is_prime(i) and i > 0 and i != 1 or i == 2:
            prime_nums.append(i)
    return prime_nums
 

if __name__ == "__main__":
    main()