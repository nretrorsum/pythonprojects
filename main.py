list = [1,2,3,2,5]
new_list = []

def func(list, new_list):
    for i in range(len(list)):
        if list[i] == list[i-1]+1:
            new_list.append(list[i])
    print("New list is:", new_list) 

def numcalc(new_list):
    result = 0
    for i in range(len(new_list) - 1):
        result = new_list[i] + new_list[i+1]
    print("Sequential number from list:", result)
    
func(list, new_list)
numcalc(new_list)