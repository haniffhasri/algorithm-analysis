def crack_safe_combination():
    # Iterate through all possible combinations from 000 to 999
    for i in range(1000):
        # we want to ensure the combination is always represented with three digits
        # Even if the value of the combination is less than 100 or less than 10.
        combination = str(i).zfill(3)

        # Check if the combination opens the safe
        if is_correct_combination(combination):
            print(f"The safe combination is: {combination}")
            return
        else:
            print(f"Tried combination: {combination}")

    print("Unable to find the safe combination.")


def is_correct_combination(combination):
    #The correct combination here:
    return combination == '158'


crack_safe_combination()


