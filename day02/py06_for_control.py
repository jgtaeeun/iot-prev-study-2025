#for문

# range()
print(range(9)) #0~8

for i in range(9):
    print(i)
    
for i in range(9):
    print(i, end=" ")       #end 인자로 출력 끝을 조정 \t " " \n
print()


sum=0
for i in range(1,11):
    sum=sum+i
print("1부터 10까지의 합 = ", sum)    


sum=0
for i in range(1,20,2):
    print(i)