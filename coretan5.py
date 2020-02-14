#RAJUT
f = input("Masukkan Kata yang mau di rajut")
g = []

#Jumlah Kapital
jk = sum(1 for c in f if c.isupper())
#Jumlah kata yang mau dihapus
jkdel = len(f)-jk
#pengurangan len
a = len(f)
# z.append(len(x))
b = len(f) -(a-1)


g.append(f[jkdel:a])
print(str(g))