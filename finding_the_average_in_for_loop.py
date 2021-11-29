# finding the average
# find the average of the values in the for loop below


counter = 0
sum = 0

for a_number in [1, 2, 3, 4, 5, 10, 28, 30]:
    # first we need to know how many numbers there is
    counter = counter + 1
    # One will be added to the counter every time it loops.
    # and then we need the sum of all values
    sum = sum + a_number

avg = sum / counter
print("The number of values in the list:", counter)
print("The sum of all values in the list:", sum)
print("The average value:", avg)