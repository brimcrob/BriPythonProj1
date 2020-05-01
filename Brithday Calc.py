import time
birth_year = input('Year You Were Born: ')
print(type(birth_year))
current_date = time.strftime("%Y")
age = int(current_date) - int(birth_year)

print(age)
