#Task 1
try:
    file1 = open('my_file.txt','r')
    read_file = file1.read()
    print(read_file)
    file1.close()
except FileNotFoundError:
    print("Error: File Does not exist")
finally:
    print("Execution Complete")
#Task 2
try:
    file2 = open('output.txt','w')
    wrt_snt = input('Enter Text data to the output file:')
    cnf_snt = file2.write(wrt_snt)
    print(cnf_snt," Number of Strings Added")
    file2.close()

    file2 = open('output.txt','a')
    wrt_Msnt = input('Enter Additional Data to append:')
    cnf_Msnt = file2.write(wrt_Msnt)
    print(cnf_Msnt," Number of Strings Appended")
    file2.close()

    file2 = open('output.txt','r')
    read_file2 = file2.read()
    print(read_file2)
    file2.close()
except:
    print("Some error occured")  
