import math  

def main():
    Num1 = input("Enter number 1 ")
    Num2 = input("Enter number 2 ")
    pythag(Num1, Num2)


def pythag(Num1, Num2):


    C = int(Num1) ** 2 + int(Num2) ** 2
    result = math.isqrt(C)
    print(result)

main()
