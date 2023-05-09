99.9
# float
"False"
# str
False
# bool
'0'
# str
0
# int
True
# bool
'True'
# str
[{}]
# list
{'a': []}
# dict

# A term or phrase typed into a search box
# str

# Whether or not a user is logged in
# bool

# A discount amount to apply to a user's shopping cart
# float

# Whether or not a coupon code is valid
# bool

# An email address typed into a registration form
# str

# The price of a product
# float

# The email addresses collected from a registration form
# list

# Information about applicants to Codeup's data science program
# dict

# '1' + 2
# typeError

# 6 % 4
# takes the remainder of 6 from 4 which is 2 int

# type(6 % 4)
# describes the type which is an int

#type(type(6 % 4))
# since type is inside of a type the type of type it appears to be is a type...

# '3 + 4 is ' + 3 + 4
# typeError

# 0 < 0
# False

# 'False' == False
# False

# True == 'True'
# False

# 5 >= -5
# True

# True or "42"
# True

# 6 % 5
# takes the remainder of 6 from 5 which is 1

# 5 < 4 and 1 == 1
# False

# 'codeup' == 'codeup' and 'codeup' == 'Codeup'
# False

#4 >= 0 and 1 !== '1'
# Error invaild syntax

# 6 % 3 == 0
# True

# 5 % 2 != 0
# True

# [1] + 2
# Type error

# [1] + [2]
# Adds both lists together creating a new list: [1,2]

#[1] * 2
# Multiplies the existing list by two which creates a new list: [1,1]

#[1] * [2]
# typeerror

#[] + [] == []
# True

# {} + {}
# typeerror

The_little_mermaid = 3
Brother_bear = 5
Hercules = 1
total_fees = (The_little_mermaid * 3) + (Brother_bear * 3) + (Hercules * 3)
print(total_fees)

Google = 400
Amazon = 380
Facebook = 350
total_pay = (Google * 6) + (Amazon * 4) + (Facebook * 10)
print(total_pay)

can_be_enrolled = class_not_full and schd_not_conf
class_not_full = True
schd_not_conf = True
can_be_enrolled
# True

class_is_full = False
schd_conf = False

enroll_stat = not (class_is_full or schd_conf)
enroll_stat

purch_more_than_two = True
prod_not_exp = True
premium_member = False

discount_elig = prod_not_exp and (purch_more_than_two)
discount_elig
# True

username = 'Codeup'
password = 'notastrongpassword'

password_length = length(password) >= 5
username_length = length(username) <=20
qual = password != username
user_and_password_valid = password_length and user_name_length and qual
user_and_password_valid
# True



