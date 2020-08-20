n=int(input("Enter number of rows "))
m=int(input("Enter number of columns "))
mat=[]
print("Enter elements :")
for i in range(0,n):
    arr=[]
    for j in range(0,m):
        z=int(input())
        arr.append(z)
    mat.append(arr)
k=int(input("Enter the value of k: "))

print("Original Matrix is :")
for i in range(0,n):
    for j in range(0,m):     
        print(mat[i][j],end=" ")
    print()

i=0
while(k):
        for j in range(0,n):
            temp=mat[j][i%m]
            mat[j][i%m]=mat[j][(i+1)%m]
            mat[j][(i+1)%m]=temp 
        k=k-1
        i=i+1


print("After rotation  :")
for i in range(0,n):
    for j in range(0,m):     
        print(mat[i][j],end=" ")
    print()