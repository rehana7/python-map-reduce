# Python Map Reduce

Basic piping introduction and concepts needed in preparation for working with big data solutions.

## Requirements

- Install Chocolatey, the Windows package manager
- Install the Miniconda 3 version for Python + common packages
- Install Visual Studio Code for text editing

## Recommended 

- Add Open PowerShell Here as Administrator to File Explorer context menu.
- Add Open Command Window Here as Administrator to File Explorer context menu.
- Add Open Anaconda Prompt Here as Administrator to File Explorer context menu.

OR be able to cd (change directory) to get to folder. 

See: [Basic Setup for Big Data](https://github.com/denisecase/basic-setup-for-bigdata)

## Case 1:  Local file-based

```PowerShell
python 11mapper.py
python 12sorter.py
python 13reducer.py
```

## Case 2:  Use standard input and output

Use the console (standard input and output) and shell commands to pipe information.  When piping, we can use the built-in shell sort command, so we don't need that anymore. THe general process is:

cat data | map | sort | reduce

PowerShell and Bash use the same commands:

```Bash
cat part.txt
cat part.txt | python 21mapper.py
cat part.txt | python 21mapper.py | sort
cat part.txt | python 21mapper.py | sort  | python 22reducer.py
cat part.txt | python 21mapper.py | sort  | python 22reducer.py > o.txt
cat purchases.txt | python 21mapper.py | sort  | python 22reducer.py > out.txt

```

## Challenge

How many times was each paymentType used?

## References

- [Udacity "Introduction to Hadoop and MapReduce"](https://classroom.udacity.com/courses/ud617/)
- [IBM Python for Data Science](https://cognitiveclass.ai/courses/python-for-data-science)
- [Basic Setup for Big Data](https://github.com/denisecase/basic-setup-for-bigdata)

## Repository

- [https://github.com/denisecase/python-map-reduce](https://github.com/denisecase/python-map-reduce)
