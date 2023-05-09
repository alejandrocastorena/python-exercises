99.9
# Float

"False"
# Str

False
# Bool

'0'
# Str

0
# Int

True
# Bool

'True'
# Str

[{}]
# List

{'a': []}
# Dict

# A term or phrase typed into a search box 
# Str

# Whether or not a user is logged in
# Bool

# A discount amount to apply to a user's shopping cart
# Int

# Whether or not a coupon code is valid
# Bool

# An email address typed into a registration form
# Str

# The price of a product
# Int

# The email addresses collected from a registration form
# List

# Information about applicants to Codeup's data science program
# Dict

'1' + 2
# Error cannot concatenate an int to a string

6 % 4
# Takes the remainder of 6 from 4 which is 2

type(6 % 4)
# class 'int'

type(type(6 % 4))
# class 'type'

'3 + 4 is ' + 3 + 4
# Error cannot concatenate an int to a string

0 < 0
# Statement is False

'False' == False
# False

True == 'True'
# False

5 >= -5
# Statement is True

True or "42"
# True I guess?

6 % 5
# Takes the remainder of 6 from 5 which is 1

5 < 4 and 1 == 1
# False i guess?

'codeup' == 'codeup' and 'codeup' == 'Codeup'
# False

4 >= 0 and 1 !== '1'
# Error invalid syntax

6 % 3 == 0
# True

5 % 2 != 0
# True

[1] + 2
# Cannot concatenate

[1] + [2]
# Adds both lists together [1,2]

[1] * 2
# multiplies the list creating [1,1]

[1] * [2]
# Can't multiply lists together

[] + [] == []
# True

{} + {}
# Can't multiply dicts

daily_fee = 3
The_Little_Mermaid = 3
Brother_Bear = 5
Hercules = 1
Total_rent = (daily_fee * The_Little_Mermaid) + (daily_fee * Brother_Bear) + (daily_fee * Hercules)
print('$',Total_rent)

Google = 400
Amazon = 380
Facebook = 350
Total_pay = (Google * 6) + (Amazon * 4) + (Facebook * 10)
print('$',Total_pay)

username = 'Codeup'
password = 'notastrongpassword'



