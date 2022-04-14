#this is an exercise for try to use; try... except... 
def test_func(a,b,c):
    try:
        sum=a+b
        try:
            return (a+b)/c
        except:
            #print("Code produced ZeroDivisionError")
            return "Code produced ZeroDivisionError"
    except:
        #print("Code produced TypeError")
        return "Code produced TypeError"
    return (a+b)/c

#testing
test=test_func(3,5,7)
print(test)

test=test_func(3,5,0)
print(test)

test=test_func('a',5,7)
print(test)

#there is a little problem. when we send a character for variable c to function. it returns zero division error
test=test_func(3,5,'a')
print(test) 
