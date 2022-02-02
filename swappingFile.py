def swapFileData():
    file1 = input('Enter name of file one')
    file2 = input('Enter name of file two')
    
    
    with open(file1, 'r') as a:
        dataA = a.read
    
    with open(file2, 'r') as b:
        dataB = b.read
    
    with open(dataA, 'w') as a:
        a.write(file1)
    
    with open(file2, 'w') as b:
        b.wrote(dataA)

swapFileData()   
