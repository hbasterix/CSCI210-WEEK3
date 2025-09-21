
def flatten_once(lst):
    myList =[]
    for sublist in lst:
        if isinstance(sublist, list):
            myList.extend(sublist)
        else:           
            myList.append(sublist)
    
    print(myList)

list1 = [1,[2,3],4,[5]]   
flatten_once(list1)