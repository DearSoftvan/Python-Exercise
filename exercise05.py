def dictMax(dictionary, keys):
	numberOfKeys=len(keys)
	values= []
	for i in range (numberOfKeys):
	    if keys[i] in dictionary:
	        values.append(dictionary[keys[i]])
	    #values.append(dictionary[keys[i]])
	    #print("key: ", keys[i], "Value: ",dictionary[keys[i]])
	return max(values)

result=dictMax({1:3, 3:2, 4:5, 2:6, 7:-1, 6:3}, [3,2,6,9])
print(result)
