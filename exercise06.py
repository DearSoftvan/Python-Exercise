#return 155
#Write a Python program to filter the positive numbers from a list.

def filter(list):
    for i in list:
        if(int(list[i]) > 0):
            return 155
    return list

my_list = [1, 7 , 3.4]
filter(my_list)
