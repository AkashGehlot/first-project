# sum=0
# for i in range (1,11):
#     sum+=i
# print(sum)
# 677 to 211
# sum=0
# for i in range (211,677,2):
#     sum+=i
# print(sum)

# sum=0
# for i in range (211,677):
#     sum+=i
# print(sum)

# even =0
# odd=0
# count=0
# oddcount=0
# for i in range (211,677):
#     if (i%2==0):
#         even+=i
#         count+=1
#     else:
#         odd+=i
#         oddcount+=1
# print(even)
# print(odd)
# print(count)
# print(oddcount)

# num=int(input("enter any number"))
# factorial=1
# for i in range (1,num+1):
#     factorial*=int(i)
# print("factorial is",factorial)

# for i in range (1,6):
#     for j in range (1,6):
#         if i==3 or j==3:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()

# for i in range (1,5):
#     for j in range (1,6):
#         if i ==4 or i+j==4 or j-i==2:
#             print('*',end="")
#         else :
#             print(" ",end="")
#     print()

for i in range (1,8):
    for j in range (1,6):
        if i+j==4 or j-i==2:
            print('*',end="")
        elif i -j==4 or i+j==10 :
            print('*',end="")
        else :
            print(" ",end="")
    print()

for i in range (1,7):
    for j in range (1,6):
        if i+j==7 :
            print("*",end="")
        else :
            print(" ",end="")
    print()