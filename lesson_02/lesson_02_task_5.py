def month_of_season(num):
    if 1 <= n <= 2 or n == 12 :
       print("Сейчас зима")
    elif 3 <= n <= 5 :
       print("Сейчас весна")
    elif 6 <= n <= 8 :
       print("Сейчас лето")
    elif 9 <= n <= 11 :
       print("Сейчас осень")
    else:
       print("Пожалуйста введите число месяца (от 1 до 12)")

n = int(input())
month_of_season(n)