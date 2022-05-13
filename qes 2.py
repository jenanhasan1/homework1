DEC = int(input('Enter dec number: '))

n_Binary = []
i=0
while DEC > 0:
    
    b = DEC % 2
    
    DEC = int(DEC / 2)
    
    n_Binary.append(b)
    
n_Binary.reverse()

print(n_Binary)

