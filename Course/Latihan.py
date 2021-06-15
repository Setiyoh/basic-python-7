# String Formatting
txt = "Nama saya {}, umur saya {}"
nama = "Setiyo"
umur = 47
print(txt.format(nama,umur))
txt = "Nama saya {}, umur saya {}".format(nama,umur)
print(txt)

#Sting Operations
b = "Hello, World!"
# H e l l o ,   W o r l d !
# 0 1 2 3 4 5 6 7 8 9 10 11 12
print(b[12])
print(b[1:6])
print(b[5:])
print(len(b))

a = "Hello"
c = "Neko"
d = a + c
e = a + " " + c
print(d)
print(e)

# Input
name = input("Siapa namamu : ")
print("Namaku adalah",name,"kamu siapa ya ?")
print("Namaku adalah"+name+"kamu siapa ya ?")

#Booleans
print(10>7)
print(10<7)
a = int(input("Masukkan angka pertama : "))
b = int(input("Masukkan angka kedua : "))
if a==b:
   print("Angka pertama sama dengan angka kedua")
else:
    print("Kedua angka berbeda")    

#List
mylist = []
mylist.append(9) #Sisipkan data
mylist.append(10)
mylist.append(20)
mylist = [9,10,20]
print(mylist[0])
print(mylist[1])
print(mylist[2])
print(len(mylist))
print(mylist)

#mylist.append(int(input("Masukkan angka : ")))
print(len(mylist))
print(mylist)
mylist[0]=30
print(mylist[0])
print(mylist)

#if else
a = int(input("Masukkan angka 1 : "))
b = int(input("Masukkan angka 2 : "))
if a > b:
    print("a lebih besar dari b")
elif a < b:
    print("a kurang dari b")
else:
    print("a sama dengan b")        