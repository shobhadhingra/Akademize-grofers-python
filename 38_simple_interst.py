def print_sum_of_simple_interest(n,p,r):
    sum= (n*p*r)/100
    print(f"sum of simple interest = {sum}")


def main():
    n = int(input("Enter N: "))
    p = int(input("Enter p: "))
    r = int(input("Enter r: "))
    print_sum_of_simple_interest(n,p,r)

main()