#there is two program 
#first one is the program() that take an integer (n) and computes the value of nnn
#the program2() that accepts an integer (n) and computes the value of n+nn+nnn
#for instance if n=5 & time=3 > 555
def program(n,time):
    carrier=n
    total=carrier
    for i in range (time-1):
        carrier=carrier*10
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
