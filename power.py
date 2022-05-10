#This is a program for calculate a to the power of n.

def power(a, n):
    result=a
    for i in range(n-1):
        result=result*a
    return result

result=power(5, 2)
print(result) 
