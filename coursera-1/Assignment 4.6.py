# It is currently 30.86 days past the due date (2015-06-30) so your late penalty is 100 percent.

## 4.6 Write a program to prompt the user for hours and rate per hour using raw_input to compute gross pay. 
## Award time-and-a-half for the hourly rate for all hours worked above 40 hours. 
## Put the logic to do the computation of time-and-a-half in a function called computepay() and use the function to do the computation. 
## The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
## You should use raw_input to read a string and float() to convert the string to a number. 
## Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly.


hrs = raw_input("Enter Hours:")
rph = raw_input("Enter Rate:")
hrs = float(hrs)
rph = float(rph)

def computepay(h,r):
	if (h>40):
    	pay = (h - 40) * (r * 1.5) + (40 * r)

	else:
    	pay = h * r
	return pay

print computepay(hrs,rph)
    
p = computepay(hrs,rate)
print p
