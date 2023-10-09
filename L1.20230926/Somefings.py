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


test.assert_equals(get_users_ids("uid12345"), ["12345"])
test.assert_equals(get_users_ids("   uidabc  "), ["abc"])
test.assert_equals(get_users_ids("#uidswagger"), ["swagger"])
test.assert_equals(get_users_ids("uidone, uidtwo"), ["one", "two"])
test.assert_equals(get_users_ids("uidCAPSLOCK"), ["capslock"])

test.describe("Advanced tests")
test.assert_equals(get_users_ids("uid##doublehashtag"), ["doublehashtag"])
test.assert_equals(get_users_ids("  uidin name whitespace"), ["in name whitespace"])
test.assert_equals(get_users_ids("uidMultipleuid"), ["multipleuid"])
test.assert_equals(get_users_ids("uid12 ab, uid#, uidMiXeDcHaRs"), ["12 ab", "", "mixedchars"])
test.assert_equals(get_users_ids(" uidT#e#S#t# "), ["test"])
