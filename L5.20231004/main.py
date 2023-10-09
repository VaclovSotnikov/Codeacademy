# my_dictionary = {"name": "Vaclov", "surname": "Sotnikov"}

# my_dictionary["phone"] = 123456789
# print(my_dictionary["phone"])

# my_dictionary = {"name": "Tom", "surname": "Edison"}

# print(f"name: {my_dictionary['name']}")
# print(f"surname: {my_dictionary['surname']}")

# d1 = {'a': 10, 'b': 20, 'c': 30}
# d2 = {'b': 200, 'd': 400}

# d1.update(d2)
# print(d1)

# my_set = {1, 2, 3, 1, 1}
# my_set.add(5)

# print(my_set)

# numbers_list = [1, 2, 3, 4, 5, 5, 5, 6, 8, 9, 9]
# numbers_set = set(numbers_list)
# print(len(numbers_set))

# my_variable = (1,)
# print(type(my_variable))

#1
name = input("enter your name: ")
surname= input("enter your surname: ")
age = int(input("enter your age: "))

my_dict = {"name": name, "surname":surname, "age": age}
print(my_dict)
# my_dict = {}
# my_dict["name"] = name
# my_dict["surname"] = surname
# my_dict["age"] = age
# print(my_dict)

print(f"User name is: {my_dict['name']}")

