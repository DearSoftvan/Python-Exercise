#return 155
#Write a Python program to filter the positive numbers from a list.

def filter(list):
    result= []
    #index=0
    for i in range(len(list)):
        print('i is :', i)
        if(int(list[i]) > 0):
            result.append(list[i])
            #index=index+1
    return result

#Test Part
my_list = [1, 7 , 3.4, -3, 5, -12, 0]
final=filter(my_list)
print(final) 
