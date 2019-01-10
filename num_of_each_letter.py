str = input("Provide a passage to reveal the number of times each letter appears: ")
i , ctr = 0, 0
letter = 'a'
letter_detected = False
while i is not 26:
    for x in str:
        if x is chr(ord(letter)):
            ctr += 1
    if ctr is not 0:
        print("The number of " + (chr(ord(letter))).upper() + "'s in the passage is", ctr)
        letter_detected = True
    ctr = 0
    letter = chr(ord(letter) + 1)
    i += 1
if letter_detected is False:
    print("No letters were detected")











