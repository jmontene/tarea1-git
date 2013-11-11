import sys

letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
d = open("sowpods.txt", "r")
for line in d:
   cur = 0
   if any((c in letters) for c in line):
      for ch in line:
         if cur > 0:
            if ch in letters and ch == line[cur - 1]:
              letters.remove(ch)
         cur = cur + 1

for a in letters:
   print a
