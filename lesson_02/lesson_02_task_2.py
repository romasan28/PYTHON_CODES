def is_year_leap(year):
   return "False" if year % 4 != 0 else "True"

y = int(input("Введите год " ))
s = is_year_leap(y)
print('Год', y, s)