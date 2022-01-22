def swapFileData():
    dataA = input('Enter name of file one')
    dataB = input('Enter name of file two')
    with open(dataA, 'r') as a:
        dataA = a.read
    with open(dataB, 'r') as b:
        dataB = b.read
    with open(dataA, 'w') as a:
        a.write(dataB)
    with open(dataB, 'w') as b:
        b.wrote(dataA)

swapFileData()   