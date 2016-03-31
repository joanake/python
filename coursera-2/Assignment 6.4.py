# It is currently 16.86 days past the due date (2015-07-14) so your late penalty is 100 percent.

## 6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. 
## Convert the extracted value to a floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475";
found = text.find('0')
found_2 = text.find('5')+1
x = text[found:found_2]
print float(x)
