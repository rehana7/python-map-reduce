# Case 2 - Mapper using standard input and output
# Easy to test locally in the terminal

import sys 
import re

# flat map each line of text to many words
for line in sys.stdin:
  wordList = line.strip().lower().split(" ")
  for word in wordList:
    #word.replace(',','')
    #word.replace('.','')
    #word.replace("\'",'')
    cleanWord = re.sub('[^a-zA-Z]+', '', word)
    print(cleanWord,',',1)
