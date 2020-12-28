print("hello")
f1 = open ('a1.txt',"r")
flines1 = f1.readlines()
print(flines1) 
f1.close()

f2 = open ('a2.txt', "r")
flines2 = f2.readlines()
print(flines2)
f2.close()

f1 = open ('a1.txt',"w")
for line in flines2:
    f1.write(line)
f1.close()
f2 = open ('a2.txt', "w")
for line in flines1:
    f2.write(line)
f2.close()

#l =f1.readlines()
#print l
#swap(file1,file2)
