def is_two(n):
    if n == 2:
        return True
    if n == '2':
        return True
    else:
        return False
    
def is_vowel(v):
    v = v.lower()
    if v == ('a' or 'e' or 'i' or 'o' or 'u'):
        return True
    else:
        return False
    
def is_consonant(cs):
    if type(cs) == str:
        is_only_letters = cs.isalpha()
        return is_only_letters and not is_vowel(cs)
    else:
        return False

def cap_first_cons(fc):
    if fc[0] in ('a' or 'e' or 'i' or 'o' or 'u'):
        return ("invalid: this string does not start with a consonant")
    else:
        return fc.capitalize()
    
def calculate_tip(bill, tip_perc):
    return bill * tip_perc
calculate_tip(50, .15)

def apply_discount(orig_price, disc_perc):
    return orig_price - ((disc_perc / 100) * orig_price)
apply_discount(70, 35)

def handle_commas(string):
    string = string.replace("," , "") 
    return int(string)
handle_commas('75,00,000,000')


def get_letter_grade(grade):
    if grade >= 90:
        return 'A'
    elif grade >= 80:
        return 'B'
    elif grade >= 70:
        return 'C'
    elif grade >= 60:
        return 'D'
    else:
        return 'F'

def remove_vowels(rv):
    v = ('a', 'e', 'i', 'o', 'u') 
    for x in rv.lower():
        if x in v:
            rv = rv.replace(x, "")
              
    return rv
remove_vowels('volkswagon')
