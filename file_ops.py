'''
mode:
r -> read . The file must exists otherwise will get an error. FileNotFoundError
w -> write . If the file is not there, it will create a file and start writing into it.
            if the file is there, it will remove the existing file content and start
            writing as a fresh file
a -> append. If the file is not there, it will create a file and start writing into it.
            if the file is there, it will not remove the existing file content rather
            it will continue(append) write along with existing content
r+ -> read-write => file gets opened for reading and writing
w+ -> write-read => write and read whatever been writen
rb -> read binary file (special file like image, video , audio)
wb -> write binary

READ-> read(), readline(), readlines()
WRITE -> write(), writelines()
'''

# with open('myfile.txt','r') as fo:
#     print(fo.read())

# with open('days','r') as fh:
#     #print(fh.read())
#     # print(fh.readline(),end='')
#     # print(fh.readline())
#     print(fh.readlines()[1:6])

# with open('myfile.txt','w') as fo:
#     print(fo.writelines(["SCB\n","GS"]))

# with open('myfile.txt','a') as fo:
#     print(fo.writelines(["\nAMEX\n","FORD"]))

# with open('myfile.txt','r+') as fh:
#     print(fh.read())
#     fh.write("\nIntuit")

# with open('myfile.txt','w+') as fo:
#     fo.writelines(['Python\n','AIML\n','BigData\n','Devops\n','Cloud'])
#     fo.seek(0,0)
#     print(fo.read())

with open(r'C:\Users\RaghulRamesh\OneDrive\Pictures\puppy.jpg','rb') as fo:
    with open(r'C:\Users\RaghulRamesh\OneDrive\Pictures\puppy2.jpg', 'wb') as wfo:
        wfo.writelines(fo.readlines())