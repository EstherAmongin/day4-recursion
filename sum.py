def sum(list1):
    
    mysum=0
    for i in list1:
        if isinstance(i,int):
            mysum+=i

        elif isinstance(i,list):
            mysum+=sum(i)
        
    return mysum

if __name__ == '__main__':
    print(sum([2,1,[2,3]]))