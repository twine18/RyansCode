digits = []
for i in range (1, 101):
    digits.append(i ** 2)
sum(digits)
newdigits = []
for i in range (1, 101):
    newdigits.append(i)
sum(newdigits) ** 2
print((sum(newdigits) ** 2) - (sum(digits)))

# line 1 creates empty list 'digits'
# line 2 initiates a for-loop for i in range 1 through 100
# line 3 squares each number i and appends the list 'digits'
# therefore adding these values to 'digits'
# line 4 takes the sum of all i in 'digits'
# line 5 creates a new empty list, 'newdigits' for our second operation
# line 6 initiates another for-loop for i in range 1 through 100
# line 7 appends 'newdigits' therefore adding all i
# in the range to 'newdigits'
# the operation in line 8 takes the sum of all i in newdigits and squares it
# line 9 squares the sum of 'newdigits', then subtracts the sum of 'digits'
# from it, giving us the difference requested in the problem, then prints it
