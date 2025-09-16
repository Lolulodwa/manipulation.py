# Ask the user to enter a sentence
str_manip = input("Enter a sentence: ")

length = len(str_manip)
print("Length of the sentence:", length)

last_letter = str_manip[-1]
replaced_str = str_manip.replace(last_letter, "@")
print("Replaced string:", replaced_str)

last_three_reversed = str_manip[-3:][::-1]
print("Last 3 characters reversed:", last_three_reversed)

five_letter_word = str_manip[:3] + str_manip[-2:]
print("Five-letter word:", five_letter_word)