def print_sum_of_natural_numbers(n):
    sum = int((n* (n+1)) / 2)
    print(f"sum of first {n} natural numbers = {sum}")


def main():
    n = int(input("Enter N: "))
    print_sum_of_natural_numbers(n)

main()