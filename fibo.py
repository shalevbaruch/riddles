import math

def recursive_fibo(n):
    if n == 1 or n == 0:
        return 1
    return recursive_fibo(n-1) + recursive_fibo(n-2)


def close_formula_fibo(n):
    x = math.sqrt(5)
    return int(((x+1) / (2*x)) * ((0.5 + x/2) ** n) + ((x-1) / (2*x)) * ((0.5 - x/2) ** n)) 


def main():
    n = input("enter the number you want to check: ")
    print("using recursive_fibo - the answer is: {}".format(recursive_fibo(int(n))))
    print("using close_formula_fibo - the answer is: {}".format(close_formula_fibo(int(n))))

if __name__ == "__main__":
    main()