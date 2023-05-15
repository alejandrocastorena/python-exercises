import itertools as it
import function_exercises as fe
fe.is_vowel('a')
fe.is_two('2')
fe.is_consonant('b')

from function_exercises import calculate_tip
calculate_tip(bill=50, tip_perc=.15)

import json

profiles = json.load(open('profiles.json'))

len(profiles)

len([profile for profile in profiles if profile['isActive'] == True])

len([profile for profile in profiles if profile['isActive'] == False])

grand_total = 0

for profile in profiles:
    user_balance = float(profile['balance'].strip('$').replace(',', ''))
    grand_total = grand_total + user_balance
    
print(grand_total)

round(grand_total / len(profiles), 2)

balance_ls = []
for profile in profiles:
    user_balance = profile['balance'].strip('$').replace(',', '')
    print(user_balance)
    balance_ls.append(user_balance)
    balance_ls
    min(balance_ls)

for profile in profiles:
    if profile['balance'].strip('$').replace(',', '') == min(balance_ls):
        print(f'User: {profile["name"]}- has the lowest balance: {profile["balance"]}')

max(balance_ls)
for profile in profiles:
    if profile['balance'].strip('$').replace(',', '') == max(balance_ls):
        print(f'User: {profile["name"]}- has the highest balance: {profile["balance"]}')

profiles[0]
profile['favoriteFruit']

fruit_list = []

for profile in profiles:
    print(profile['favoriteFruit'])
    fruit_list.append(profile['favoriteFruit'])

max((fruit_list), key = fruit_list.count)
min((fruit_list), key = fruit_list.count)

profile['greeting']

greeting_list = []

for profile in profiles:
    print(profile['greeting'])
    greeting_list.append(profile['greeting'])

message = profile['greeting'].split(' ')
message

for word in message:
    if word.isdigit():
        print(' # Unread messages:', word)

sum_messages = 0

for profile in profiles:
    message = profile['greeting'].split(' ')
    for word in message:
        if word.isdigit():
            sum_messages = sum_messages + int(word)
    sum_messages


