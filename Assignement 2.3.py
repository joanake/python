# It is currently 37.86 days past the due date (2015-06-23) so your late penalty is 100 percent.

# Write a program to prompt the user for hours and rate per hour using raw_input to compute gross pay. Use 35 hours and a rate of 2.75 per hour to test the program (the pay should be 96.25). You should use raw_input to read a string and float() to convert the string to a number. Do not worry about error checking or bad user data.

hrs = raw_input("Enter Hours:")
rph = raw_input ("Enter Rate:")
pay = float(hrs) * float(rph)
print pay
