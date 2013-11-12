import sys
import string

letters = string.uppercase
d = open("sowpods.txt", "r")
for line in d:
   cur = 0
   if any((c in letters) for c in line):
      for ch in line:
         if cur > 0:
            if ch == line[cur - 1]:
              letters = letters.replace(ch,"")
         cur = cur + 1

for a in letters:
   print a
