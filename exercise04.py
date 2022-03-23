#there is two program 
#first one is the program() that take an integer (n) and computes the value of nnn
#the program2() that accepts an integer (n) and computes the value of n+nn+nnn
#for instance if n=5 & time=3 > 555
def program(n,time):
    if(time == 0):
        return n
    if(time < 1):
        return "Error"
    carrier=n
    total=n
    base=10
    for i in range (time-1):
        carrier=carrier*base
        total=total+carrier
    return total

result= program(5,3)
print("The result of program() is :",result)



#for instance if n=5 & time=3 > 5+55+555=615
def program2(n,time):
    subtotal=0
    sum=0
    number=n
    for i in range(time):
        #print("i: ", i)
        for k in range(i+1):
            number=n*10**k
            sum=sum+number
            #print("k: ", k)
            #print("presum: ", subtotal)
        subtotal=sum+subtotal
        #print("sum: ", sum)
    return sum
    
result= program2(5,3)
print("The result of program2() is:", result)


#there is a alternative of program2()
def program3(n,time):
    if(time < 0):
        return "Error"
    sum=0
    for i in range(1,time+1): 
        number=program(n,i)
        sum= sum+ number
    return sum
result= program3(5,3)
print("The result of program3() is:", result)
