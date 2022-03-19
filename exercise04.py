#This is a program that accepts an integer (n) and computes the value of n+nn+nnn
#for instance if n=5 > 5+55+555
def program(n,time):
    carrier=n
    total=carrier
    for i in range (time-1):
        carrier=carrier*10
        total=total+carrier
    return total

result=program(5,3)
print(result)


