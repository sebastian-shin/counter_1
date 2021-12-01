#Below code finds whether or not we got something matching to what we're looking for

true_or_false = False
print('Before', true_or_false)
for a_number in [9, 8, 39, 39, 382, 100, 2, 200, 200, 300]:
    if a_number == 200:
        true_or_false = True
    print(a_number, true_or_false)
print('After', true_or_false)
#


