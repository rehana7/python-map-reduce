# Commands for processing text

```PowerSHell
cat rj.txt | python 1mapper.py | sort | python 1reducer.py > oo.txt
cat oo.txt | python 2mapper.py | sort -Descending | python 2reducer.py > o.txt
Get-Content -Path .\o.txt -TotalCount 10
```

## if Bash

```Bash
cat oo.txt | python 2mapper.py | sort -r | python 2reducer.py > o.txt
head -10 o.txt
```

## Challenge

1. What kind of words are most common in a given corpus (text collection), for example, Romeo & Juliet? 
2. Do the most common words help determine the main idea?
3. Google 'stopwords'.
4. Could you update the process to remove all stopwords to get a better understanding? 
