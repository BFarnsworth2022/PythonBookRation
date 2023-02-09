"""
A - Z 	65 - 90
0 - 9		48 - 57
.		46
,		44
/		47
?		63

chr(22)


MorseCodeCharacters = "KMRSUAPTLOWI.NJEF0YV,G5/Q9ZH38B?427C1D6X"

a = "Hello, World!"
print(a[1])


for x in "banana":
  print(x)

a = "Hello, World!"
print(len(a))


txt = "The best things in life are free!"
print("free" in txt)

if "free" in txt:
  print("Yes, 'free' is present.")

txt = "The best things in life are free!"
print("expensive" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

b = "Hello, World!"
print(b[2:5])

b = "Hello, World!"
print(b[2:])


b = "Hello, World!"
print(b[-5:-2])

a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.lower())

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

a = "Hello, World!"
print(a.replace("H", "J"))

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

s = '123abc'
n = 3
''.join([char*n for char in s])
"""


"""
def Convert(string):
    list1 = []
    list1[:0] = string
    return list1
  
  
# Driver code
# str1 = "ABCD"
MorseCodeCharacters = "KMRSUAPTLOWI.NJEF0YV,G5/Q9ZH38B?427C1D6X"
print(Convert(MorseCodeCharacters))
"""

import random
import os
MorseCodeCharacters = "KMRSUAPTLOWI.NJEF0YV,G5/Q9ZH38B?427C1D6X"
NumChar = 5

Training = ''.join([char*NumChar for char in MorseCodeCharacters])

def Convert(string):
    list1 = []
    list1[:0] = string
    return list1

def encrypt(string, length):
    return ' '.join(string[i:i+length] for i in range(0,len(string),length))


def encrypt2(string, length):
    return ''.join(string[i:i+length] for i in range(0,len(string),length))

ConvertTraining = Convert(Training)
#print(ConvertTraining)

random.shuffle(ConvertTraining)
z = ''.join(ConvertTraining)
#print(z)
x = encrypt(z, 5)
print(x)


#os.system('ebook2cw.exe -w 25 -f 800 -o MorseCode MorseCode.txt')
