'''
Exercise 6.5 Take the following Python code that stores a string:‘
str = 'X-DSPAM-Confidence: 0.8475'
Use find and string slicing to extract the portion of the string after the colon
character and then use the float function to convert the extracted string into a
floating point number.
'''
entry = 'X-DSPAM-Confidence: 0.8475'
space_pos = entry.find(' ')
print (float(entry[space_pos+1:]))

portion = float(entry[entry.find(' ')+1:])
print (portion)

print(float(entry[entry.find(' ')+1:]))