lang= 'Java'

# if lang == 'Python':
#     print("Language is Python")
# else:
#     print("No match")


#when we have to check more than one language
if lang == 'Python':
    print("Language is Python")
elif lang == 'Java':
    print("Language is Java")
else:
    print("No match")

# and or not operators
user = 'Admin'
logged_in = True

if user=='Admin' and logged_in:
    print('Welcome')
else:
    print('Bad Cred')


    #False values
        # False
        # None
        # Zero of any numeric type
        # Any empty sequence. For example, '',(),[]
        # Amy empty mapping. For example, {} , means empty dictionary

condition = {}

if condition:
    print("Evaluated to true")
else:
    print("Evaluated to False")



