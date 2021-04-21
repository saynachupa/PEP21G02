"""
Get text from input abcefg
return bcdefgh
"""

input1= input('Enter your text')
slice1 = input1[1:3]
slice2 = input1[3:4]
rev1 = slice1[::-1]
rev2 = slice2[::-1]
print(input1+slice2)
