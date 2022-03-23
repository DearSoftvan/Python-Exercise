#this function take a dictionary and a list of keys than returns the maximum value from dictionary which its key given in the list
def dictMax(dictionary, keys):
	#define variable for keeping the length of list
	numberOfKeys=len(keys)
	
	#define a list for keep values which pointed by the keys
	values= []
	
	#this loop for collect the values which pointed by keys
	for i in range (numberOfKeys):
		#this if case for check the keys are there provisions in dictionary 
	   if keys[i] in dictionary:
	        values.append(dictionary[keys[i]])
		#if the key doesn't exist in dictionary there will be send a just warning message
	   else:
	       print("Warning: There is ",keys[i]," in key list, but there aren't any key in the dictionary like as ", keys[i],".")
	    #values.append(dictionary[keys[i]])
	    #print("key: ", keys[i], "Value: ",dictionary[keys[i]])
	return max(values)

print("Welcome the kitchen of Softone")

#There is a sample call for the funciton dictMax()
result=dictMax({1:3, 3:2, 4:5, 2:6, 7:-1, 6:3}, [3,2,6,9])
print("Result is: ", result)
