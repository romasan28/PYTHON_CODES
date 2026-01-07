def fizz_buzz(n):
    n=n+1
    for x in range (1, n):
        if (x % 3 == 0) and (x % 5 == 0):
           print("fizzbuzz, ")
        elif x % 5 == 0:
           print("buzz, ")
        elif x % 3 == 0:
           print("fizz, ")
        else:
           print(x," ")
    
n=int(input("Введите число: "))
fizz_buzz(n)