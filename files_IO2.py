fileptr = open("testfile.txt","r");  
reads=fileptr.readline()  #type1
print(reads)


for i in fileptr:  #type2 iterating
    print(i)
