#return 155
#Write a Python program to filter the positive numbers from a list.

def filter(list):
    result= []
    #index=0
    for i in list:
        if(int(list[i]) > 0):
            result.append(list[i])
            #index=index+1
    return result

my_list = [1, 7 , 3.4]
filter(my_list)
