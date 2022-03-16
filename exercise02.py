#rateOfInterest must be enter as percentage
def compoundInterest(amount, stepNumber, rateOfInterest):
	if(stepNumber < 1):
		print('Error: Step number is less than 1')
		return -1

	interest=(100+rateOfInterest)/100
	for i in range(stepNumber):
		amount=amount*interest
	return amount



#here is for the test our function
result= compoundInterest(1000, 2, 50)
print(result) 


