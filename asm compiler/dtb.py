exponent = int(input("Enter a bit length: ")) #Get a bit length
maxint = 2**exponent #Calculates the maximum integer for the specified bit length to detirmine if goodnum should be true
goodnum = False #No number inputed yet, therefor false

binary_arr=[None]*exponent #Create an array the size of the bit length (variable: exponent)

while goodnum == False: #While false, continue to ask for an acceptable number
	number = int(input("Enter a 32 bit integer: ")) #Get a base 10 number to convert
	"""
	Next, check if the number entered can create a signed or unsigned binary number that
	can fit into the specified bit length. If it is, se goodnum to True and stop checking for a good number.
	"""
	if (number < maxint)&(number > (maxint/-2)):
		goodnum = True
	else:
		print "Bad number, try again..." #Number will not fit in specified bit length

"""
This adds one to the binary number stored in binary_arr.
This is to be used to sign a 2's compliment binary number.
"""
def addone():
	carry = False
	for x in range(0, exponent):
		if (carry == False)&(binary_arr[x] == 0):
			binary_arr[x] = 1
			break
		elif (carry == False)&(binary_arr[x] == 1):
			binary_arr[x] = 0
			carry = True
		else:	
			if (binary_arr[x] == 1)&(carry == True):
				binary_arr[x] = 0
			elif (binary_arr[x] == 0)&(carry == True):
				binary_arr[x] = 1
				break
	return

"""
If the number is greater than zero, check if the number is 
larger than the most signifigant bit and subtract 2^x if it is and insert a 1 in that bit position.
Otherwise, insert a 0 in that bit position check the next most signifigant bit and check then
subtract if smaller inserting either a 1 or a 0. Keep repeating with the next most signifigant
bit until there is nothing left to check (ie. until it has reached 2^0
"""
def greaterthanzero(gtz):
	for x in reversed(range(0, exponent)):
		if gtz >= 2**x:
			binary_arr[x] = 1
			gtz -= 2**x
		else:
			binary_arr[x] = 0
	return
	
"""
If the number is less than zero, convert it back into a positive number (x*-1) and pass to the 
"greaterthanzero()" function. When it gets the resulting biinary number back from that function,
flip all of the bits and add 1 to the binary number to sign the now negative binary number
in two's compliment.
"""
def lessthanzero(ltz):
	greaterthanzero(ltz*-1)
	for x in reversed(range(0, exponent)):
			if binary_arr[x] == 1:
				binary_arr[x] = 0
			elif binary_arr[x] == 0:
				binary_arr[x] = 1
	addone();
	return
	
if goodnum == True: #If goodnum == True, detirmine how to create the binary number.
	if number > 0: #If the base 10 number is > 0, call the function to create a positive unsigned binary number
		greaterthanzero(number); #Pass the base 10 number to the function that does this
	elif number < 0: #If the base 10 number is < 0, call the function to create a negative signed binary number
		lessthanzero(number); #Pass the base 10 number to the function that does this
	elif number == 0: #If the number is 0...
		binary_arr=[0]*exponent #make the entire array that holds the binary number 0 also.
		
for x in reversed(range(0, exponent)):
	print(binary_arr[x]), #Print the array, all characters on the same line without stupid syntax included in the print.