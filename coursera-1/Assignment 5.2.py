# It is currently 23.86 days past the due date (2015-07-07) so your late penalty is 100 percent.

## 5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
## Once 'done' is entered, print out the largest and smallest of the numbers. 
## If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. 
## Enter the numbers from the book for problem 5.1 and Match the desired output as shown.

num_list = []
largest = None
smallest = None

while True:
    inp = raw_input("Enter a number: ")
    if inp == "done" : break
    try:
        num = int(inp)
	num_list.append(num)
    except:
        print "Invalid input"
    continue
        
for num in num_list:
	if largest<num or largest == None:
		largest = num 
	if smallest>num or smallest == None:
		smallest = num 

print 'Maximum is', largest
print 'Minimum is', smallest
