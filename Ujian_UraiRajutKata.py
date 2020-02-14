def urai(y):
    z = ''
    y = y.replace(' ','')

    #panjang kata
    length= len(y)

    i =0

    for j in range(length):
        for k in range(j+1):
            z+= y[k]
    return z


#RAJUT
def rajut(f):
    f = f.replace(' ','')
    #Jumlah Kapital
    jk = sum(1 for c in f if c.isupper())
    #Jumlah kata yang mau dihapus
    jkdel = len(f)-jk
    #pengurangan len
    a = len(f)
    # z.append(len(x))
    b = len(f) -(a-1)


    hasil = f[jkdel:a]
    return hasil
    
print(urai('Code'))
print(urai('Python'))
print(urai('Purwadhika'))
print(rajut('CCoCodCode'))
print(rajut('PPyPytPythPythoPython'))
print(rajut('PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika'))