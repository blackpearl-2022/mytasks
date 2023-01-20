# sum of n numbers within a range
# upperlimit=int(input("Enter the upper limit: "))#3
# lowerlimit=int(input("Enter the lower limit: "))#1
# sum=0
# while(lowerlimit<=upperlimit):#3<=3
#     sum+=lowerlimit# sum=3+3 = 3
#     lowerlimit+=1#3+1=4
# print(sum)

#reverse of a number
# Number = int(input("Please Enter any Number: ")) #120
# Reverse = 0
# while (Number > 0): # 120>0  | 12>0 | 1>0
#     Reminder = Number % 10# 120%10 = 0 | 12%10 = 2 | 1%10 = 1
#     Reverse = (Reverse * 10) + Reminder# (0*10)+0 = 0 | (0*10) + 2 = 2 | (2*10)+1 = 21
#     Number = Number // 10# 120/10=12 | 12 //10 = 1 | 1 //10 = 0
#
# print("Reverse of entered number is ",Reverse)

#Sum of cube of digits of number

# num=int(input("Enter the number:- "))#123
# sum=0
# while(num!=0): # 123>0 | 12>27 | 1>0
#     Reminder=num % 10 # 123%10=3 | 12%10=2 | 1%10 = 1
#     sum=sum+(Reminder**3)# 0+(3**3)= 27 | 27+(2**3)=8+27=35 | 35+(1**3)=35+1= 36
#     num = num // 10 #123//10 = 12 | 12/10 = 1 | 1//10 =0
# print(sum)

#multiplication table of a number
n=int(input("Enter the number:- "))
for i in range(1,11):
    m=i*n
    print (i,"x",n,"=",m)
