# Case 2 - Reducer using standard input and output
# Easy to test locally in the terminal

# This is an identity reducer - it just echos the mapper output.

import sys

for line in sys.stdin:
  datalist = line.strip().split('\t')
  if (len(datalist) == 2) : 
    count, word = datalist
    print(count,'\t',word)
   


