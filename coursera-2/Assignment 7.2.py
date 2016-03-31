# It is currently 9.87 days past the due date (2015-07-21) so your late penalty is 100 percent.

## 7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
### X-DSPAM-Confidence:    0.8475
## Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below.
## You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.

# Use the file name mbox-short.txt as the file name

fname = raw_input("Enter file name: ")              #Ask for file name
fh = open(fname)                                    #Open file

total = []                                          #Create empty list

for line in fh:
    if line.startswith('X-DSPAM-Confidence'):       #If line contains X-DSPAM-Confidence
      flt = float(line.split(':')[1])               #Float the numbers only; which is stored in [1]
      flt = float(line.split(':')[1])               #Append numbers to list
      total.append(flt)

average = sum(total)/len(total)                     #Calculate average of numbers
average = str(average)                              #Convert average to string for printing

print  'Average spam confidence: ' + average
