#Below code finds whether or not we got something matching to what we're looking for

true_or_false = False
for a_number in [9, 8, 39, 39, 382, 100, 2, 200, 200, 300]:
    if a_number == 200:
        true_or_false = True
        print("We have a match:", a_number, true_or_false)
    else:
        print(a_number)

