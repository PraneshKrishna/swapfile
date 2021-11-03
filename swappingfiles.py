def swapfile():
    filename = input("Enter the file name: ")
    file1 = open(filename,'r')
    filename2 = input("Enter the second file name: ")
    file2 = open(filename2,'r')
    data_a = file1
    data_b = file2
    with open(file1, 'r') as a:
        data_a = a.read()
    with open(file2, 'r') as a:
        data_b = a.read()
    with open(file1, 'w') as a:
        a.write(data_b)
    with open(file2, 'w') as a:
          a.write(data_a)

swapfile()