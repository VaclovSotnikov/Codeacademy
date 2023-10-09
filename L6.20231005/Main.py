# my_list = [1, 2, 3]

# print(f"length of the list {my_list} is: {len(my_list)}")

#2

# my_list = ["Petras", "Antanas", "Juozas", "Vaclov"]
# print(*my_list , sep=" | ")

#3

# my_list = [3.547, 4.795, 4.131, 6.661]
# new_list = []
# for number in my_list:
#     new_list.append(round(number, 2))

# print(new_list)

#4

# my_list = ['Konaitis', "Petraitis", "Zimnickas", "Sotnikov"]
# sorted_list = sorted(my_list)
# print(sorted_list)

#5

your_number = input("Enter your number: ")
print("number is {:0.3f}.".format(your_number))
print(round(your_number, 2))



# We've got a very long string, containing a bunch of User IDs. This string is a listing, which seperates each user ID with a comma and a whitespace ("' "). 
# Sometimes there are more than only one whitespace. Keep this in mind! Futhermore, some user Ids are written only in lowercase, others are mixed lowercase and uppercase characters. 
# Each user ID starts with the same 3 letter "uid", e.g. "uid345edj". But that's not all! Some stupid student edited the string and added some hashtags (#). 
# User IDs containing hashtags are invalid, so these hashtags should be removed!

# Task
# Remove all hashtags
# Remove the leading "uid" from each user ID
# Return an array of strings --> split the string
# Each user ID should be written in only lowercase characters
# Remove leading and trailing whitespaces


# test.assert_equals(get_users_ids("uid12345"), ["12345"])
# test.assert_equals(get_users_ids("   uidabc  "), ["abc"])
# test.assert_equals(get_users_ids("#uidswagger"), ["swagger"])
# test.assert_equals(get_users_ids("uidone, uidtwo"), ["one", "two"])
# test.assert_equals(get_users_ids("uidCAPSLOCK"), ["capslock"])

# test.describe("Advanced tests")
# test.assert_equals(get_users_ids("uid##doublehashtag"), ["doublehashtag"])
# test.assert_equals(get_users_ids("  uidin name whitespace"), ["in name whitespace"])
# test.assert_equals(get_users_ids("uidMultipleuid"), ["multipleuid"])
# test.assert_equals(get_users_ids("uid12 ab, uid#, uidMiXeDcHaRs"), ["12 ab", "", "mixedchars"])
# test.assert_equals(get_users_ids(" uidT#e#S#t# "), ["test"])

# income_list = "uid12 ab, uid#, uidMiXeDcHaRs"

# import re
# prefix = "uid"
# delete_uid = []
# list_without_uid = []
# split2 = []

# cleared = re.sub("[# ]","", income_list)
# lower = cleared.lower()
# split = cleared.split(",")

# for item in split:
#     delete_uid = item.index(prefix) + len(prefix)
#     list_without_uid.append(item[delete_uid:].strip())


# print(list_without_uid)


# def get_users_ids(string):
#     return [w.replace("uid", "", 1).strip() for w in string.lower().replace("#", "").split(",")]

# print(type(split))

# my_string = "uidMultipleuid"
# prefix = "uid"

# delete_uid = my_string.index(prefix) + len(prefix)
# my_string = my_string[delete_uid:]
# print(my_string)


# my_string = my_string.replace("#", "")
# my_string = my_string.replace(" ", "")

# print(my_string)

# income_list = "uid##doublehashtag"

# import re
# prefix = "uid"
# delete_uid = []

# delete_uid = income_list.index(prefix) + len(prefix)
# my_string = income_list[delete_uid:]
# claered = re.sub("[# uid]","",my_string)

# lower = claered.lower()
# split = lower.split(",")
# print(split)