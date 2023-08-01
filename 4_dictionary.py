student= {'name': 'Abhi', 'age': 10, 'subjects':['Math', 'English']}

print(student['subjects']) 
print(student.get('subjects')) #give same as above
print(student.get('phone')) #return None becz key doesn't exist

print(student.get('phone', 'Not Found')) #if you want to return a specific message if value not found
student['grade']='Sixth' # add the new key-value to dict
student['age']= 11 #change the key's value in dict

#we can do all these things in a single command
student.update({'name':'Vedagya','age': 7, 'phone':1234567890})
print(student)

del student['phone']
print(student)

#we can also pop and save the popped value in a variable
# age= student.pop('age')
# print(age)

print(len(student))
print(student.keys())
print(student.values())
print(student.items())

#it will print key and value from student
for k,i in student.items():
    print(k,i)



