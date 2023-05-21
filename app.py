first_name = "saba"
last_name = "abzhandadze"
print(type(first_name))
age = 22
print(type(age))
is_student = True
print(type(is_student))
pi = 3.14
print(type(pi))
result = None
print(type(result))
greeting = "hello my dear friends"
my_bio = "my name is " + first_name + " " + \
    last_name + " im " + str(age) + " years old"
print(my_bio)
print(f"{greeting} my name is {first_name} {last_name} im {age} years old")
birth_year = 2000
number_for_zodiac = birth_year / age
print(number_for_zodiac)

number_for_zodiac = birth_year * age
print(number_for_zodiac)

number_for_zodiac = birth_year - age
print(number_for_zodiac)

number_for_zodiac = birth_year + age
print(number_for_zodiac)

square_length = 7
square_width = 5
square_area = square_length * square_width
print(f"ოთხკუთხედის ფართობია {square_area}")