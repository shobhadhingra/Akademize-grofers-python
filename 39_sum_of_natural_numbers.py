def get_sum(n):
    sum= 0
    for i in range(n+1):
        sum= sum+i

    return sum


def main():
    n = int(input("Enter N: "))
    sum= get_sum(n)
    print(f"sum of first {n} natural numbers= {sum}")

main()