subjects=['Hindi', 'English','Maths', 'Science', 'SST','Computer']

# print(subjects)
# print(len(subjects))

# print(subjects[4]) #print 4th index value from the list
# print(subjects[0:5])# print 0,1,2,3,4th index value from list
# print(subjects[0:])#print all values from list
# print(subjects[2:])#print 2nd index value to last value of list
# print(subjects[-1])#print last value of list

subjects.append('Sanskrit')

# #subjects.insert(0,'Sanskrit')
# #print(subjects)
subjects.append('Arts')
# subjects.insert(0,'Arts') #insert the value @given index
# #print(subjects)

# subjects_2=['Games', 'CCA']
# #subjects.insert(0,subjects_2) #insert the value as one item
# print(subjects)


# subjects.extend(subjects_2) # each individual items are being extended at the end
# print(subjects)

subjects.remove('Arts');

# print(subjects)
print(subjects.pop()) # this will give us the popped value


subjects.reverse()
print(subjects)

# subjects.sort() #sorting in ascending order
# print(subjects)

nums= [3,5,2,8,6,4]
#nums.sort() 
nums.sort(reverse=True) #sort in descending order
print(nums)

#if we want to get sorted list without changing original list use sorted()
sorted_nums= sorted(nums)
print(sorted_nums)

#min & max value of list 
print(min(nums))
print(max(nums))
print(sum(nums))

#to check the index of a value in list
print(subjects.index('Maths'))

#if we want to check whether a particular value is in the list or not with True & False
print('Maths' in subjects)

for item in subjects:
    print(item)
print('--------------------------')
for i,c in enumerate(subjects):
    print(i,c)
print('--------------------------')
for i,c in enumerate(subjects,start=1):
    print(i,c)
print('--------------------------')

#we want to print subjects as comma sepatated values in a row
subjects_str = ' , '.join(subjects)
print(subjects_str)

new_list= subjects_str.split(' , ') # we want our original list back
print(new_list)

#sets
fruits={'Banana', 'Apple', 'Orange', 'Grapes'}

new_fruits={'Papaya', 'Cheeku','Apple','Orange'}

print(fruits.intersection(new_fruits)) #common subjects in both sets
print(fruits.difference(new_fruits)) #items which are in fruits but not in new_fruits

print(fruits.union(new_fruits)) # j
