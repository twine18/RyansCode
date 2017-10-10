def chain(n, count = 1):
# creates a user-defined function 'chain', and starts count at 1
    while n > 1:
# creates a while-loop for all n greater than i
        count += 1
# adds 1 to n, then redefines n as n+1, continuing this for n > 1
        if n % 2 == 0:
            n = n/2
# if n divided by 2 has remainder 0, the number is even, so it runs number 'n'
# through the even function defined in the problem: n = n/2
        else:
            n = 3*n + 1
# if n does not satisfy the 'if' condition, n is odd, so it puts n through the
# the function defined for odd numbers in the problem: n = 3*n + 1
    return count
# returns the count

max = [0,1000000]
# 'max' function returns the argument in its range closest to positive infinity
for i in range(1000000):
# initiates a for-loop for all i up to 1000000
    largestnumber = chain(i)
# defines 'largestnumber' as all i up to 1000000 within the function 'chain'
# which I created earlier
    if largestnumber > max[0]:
        max[0] = largestnumber
        max[1] = i
# gives the two different maximums, respectively: the maximum number of terms
# in the largest chain and the maximum number that produces this chain
print "%s, %s" % (max[0], max[1])
# prints the number that creates the largest chain, and then the number of
# values 'n' inside this chain
