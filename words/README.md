# Commands for processing text

cat rj.txt | python 1mapper.py | sort | python 1reducer.py > oo.txt
cat oo.txt | python 2mapper.py | sort -Descending | python 2reducer.py > o.txt
Get-Content -Path .\o.txt -TotalCount 10

## if Bash

cat oo.txt | python 2mapper.py | sort -r          | python 2reducer.py > o.txt
head -10 o.txt

## Challenge

1. What kind of words are most common? 
2. Do these help determine the main idea?
3. Google 'stopwords'.
4. Could you update the process to remove all stopwords to get a better understanding? 