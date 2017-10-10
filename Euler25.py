digits = []
# creates empty list 'digits'
fibo = [0, 1]
# creates list 'fibo' to hold fibonacci sequence. I left the numbers 0 and 1
# in the list from the start because the following formula would produce
# negative values for these two numbers
for i in range(10000):
# initiates a for loop for all i up to 10000. I chose 10000 after a bit of
# guess and check, realizing that 10000 could generate up to 2000+ digit numbers
# meaning my answer would be somewhere in the middle of this range
    fibo.append(fibo[-1] + fibo[-2])
# this does the actual fibonacci computations, it appends the list 'fibo' with
# the outputs of the "Fn = Fn-1 + Fn-2" formula given in the directions
    if len(str(max(fibo))) == 1000:
# this takes the max (value closest to infinity) in the list fibo, converts it
# to a string with 'str', and then uses 'len' to count the digits of the number
        digits.append(i)
# if a number has a thousand digits, this appends the list 'digits' to include
# only these numbers (there are 5 of them in total)
print(min(digits))
# this prints the smallest of these five numbers, and therefore the first term
# in the sequence that has 1000 digits
