'''6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. 
Convert the extracted value to a floating point number and print it out.'''

text = "X-DSPAM-Confidence:    0.8475";
num = text.find('0') 	#Find starting position of 0.8475
num = text[num:]		#String slicing of 0.8475
num = float(num)		#Convert to floating point number
print num				
