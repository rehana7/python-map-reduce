# Case 2 - Mapper using standard input and output
# Easy to test locally in the terminal

import sys 

# for each line, reverse
for line in sys.stdin:
  strList = line.strip().split('\t')
  if (len(strList) == 2):
    key, value = strList
    # print(value,'\t',key)
    # right justify using 8 columns - sorting done automatically
    print(value.strip().zfill(8),'\t',key)
