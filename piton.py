def frameStr(s, t):
	if(t<=0):
		print(s)
		return 155
	front='-=X '
	end='X=-'
	line='-'
	equal='='
	x='x'

	lines=line
	equals=equal
	exs=x

    
	for i in range(t-1):
		lines=lines+line
		equals=equals+equal
		exs=exs+x
		#i++

	front=lines+equals+exs
	end=exs+equals+lines
	print(front + " " + s + " " + end)
	

#Test
text='Aslan Parçası'
frameStr('A',0)
frameStr(text,5)

