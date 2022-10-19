# Python - Access List Items

## Access Items 

bike = ['Kawasaki','Apache','Ducati','Victor','XL 100']
print(bike[2])

## Negative Indexing

bike = ['Kawasaki','Apache','Ducati','Victor','XL 100']
print(bike[-2])

## Range of Indexes

bike0 = ['Kawasaki','Apache','Ducati','Victor','XL 100','Hayabusa','Duke','KTM','Dodge']
print(bike0[2:6])
bike1 = ['Kawasaki','Apache','Ducati','Victor','XL 100','Hayabusa','Duke','KTM','Dodge']
print(bike1[:6])
bike2 = ['Kawasaki','Apache','Ducati','Victor','XL 100','Hayabusa','Duke','KTM','Dodge']
print(bike2[2:])

## Range of Negative Indexes

bike3 = ['Kawasaki','Apache','Ducati','Victor','XL 100','Hayabusa','Duke','KTM','Dodge']
print(bike3[-6:-2])
bike4 = ['Kawasaki','Apache','Ducati','Victor','XL 100','Hayabusa','Duke','KTM','Dodge']
print(bike4[:-2])
bike5 = ['Kawasaki','Apache','Ducati','Victor','XL 100','Hayabusa','Duke','KTM','Dodge']
print(bike5[-6:])

## Check if Item Exists

bike = ['Kawasaki','Apache','Ducati','Victor','XL 100']
if 'Kawasaki' in bike:
    print('Yes, Kawasaki in the bike list')
else:
    print('No, Kawaskai is not in the list')

