# It is currently 2.87 days past the due date (2015-07-28) so your late penalty is 60 percent.

## 8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() function. 
## The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. 
## When the program completes, sort and print the resulting words in alphabetical order.
## You can download the sample data at http://www.pythonlearn.com/code/romeo.txt

fname = raw_input("Enter file name: ")
fh = open(fname)              # Open File
list = []                     # Create empty list to add list of words
for line in fh:
  words = line.split()        # split line into list of words
  for i in words:
    if i not in list:         # check if word already in list
      list.append(i)          # if not append to list
list.sort()                   # sort in alphabetical order
print list                    # print in alphabetical order


