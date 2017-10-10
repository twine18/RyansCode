digits = []
# creates empty list 'digits'

for i in range (1, 101):
    digits.append(i ** 2)
# line 4 initiates a for-loop for i in range 1 through 100
# line 5 squares each number i and appends the list 'digits'
# therefore adding these values to 'digits'

print sum(digits)
#this prints the sum of all i in 'digits'

newdigits = []
# creates a new empty list, 'newdigits' for our second operation
for i in range (1, 101):
    newdigits.append(i)
# line 15 initiates another for-loop for i in range 1 through 100
# line 16 appends 'newdigits' therefore adding all i
# in the range to 'newdigits'

print (sum(newdigits) ** 2)
# this function takes the sum of all i in newdigits, squares it, then prints it

print((sum(newdigits) ** 2) - (sum(digits)))
# this function takes the answer from the function in line 21 and subtracts the
# sum of 'digits' – which we found earlier from it, giving us our final answer
# and then printing it
