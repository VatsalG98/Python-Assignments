def fact(num):
    if num == 0 or num == 1:
        return 1
    else:
        factorial=num * fact(num - 1)
        return factorial


num=5
n=fact(num)
print("Factorial of",num,"is:",n)
