# It is currently 9.87 days past the due date (2015-07-21) so your late penalty is 100 percent.

## 7.1 Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case. 
## Use the file words.txt to produce the output below. You can download the sample data at http://www.pythonlearn.com/code/words.txt

# Use words.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
inp = fh.read()
inp = inp.strip()
print inp.upper()

