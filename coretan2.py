# a = len(z)
# b = len(y) -(a-1)

kata = "Aliando"

def urai(kata):
  for i in range (0,len(kata)):
    a = len(kata) #Aliando
    b = len(kata)-(a-1) #A
    for j in kata:
        b +=1  
        hasil = (kata[0:b])
    
      
  return hasil
print(urai(kata))



# def total(x,y):
#     z = x+y
#     return z
# print(total(4,5))