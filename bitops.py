def bitcat(nums, bits):
	if type(nums) != list or type(bits) != list: raise TypeError("Parameter must be a list")
	if len(nums) != len(bits): raise ValueError("Lists must be same length")
	for i in range(len(nums)):
		if type(nums[i]) is not int or type(bits[i]) is not int: raise TypeError("Value not an int at index "+str(i))
		if nums[i] >= 2**bits[i]: raise ValueError("Value is greater than "+str(bits[i])+" bit(s) at index "+str(i))
	
	r = nums[-1]
	for i in range(len(nums)-1): r += nums[i] << sum(bits[i+1:])
	return r

def bitsplit(num, bits):
	if type(num) is not int: raise TypeError("First parameter must be int")
	if type(bits) is not list: raise TypeError("Second parameter must be list")
	for i in range(len(bits)):
		if type(bits[i]) is not int: raise TypeError("Value is not an int at index "+str(i))
	
	r = []
	for i in range(len(bits)): r.append( num >> sum(bits[i+1:]) & (2**bits[i]-1) )
	return r
