num_rows = int(input())
num_cols = int(input())

i=1

while i <= num_rows:
    z = 'A'
    for j in range(num_cols):
       print(f'{i}{z}', end=' ')
       z = chr(ord(z)+1)  
    i+=1

print()
