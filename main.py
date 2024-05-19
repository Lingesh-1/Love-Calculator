print("The LOVE CALCULATOR is calculating your score.....")
n1=input("Enter Name1:")
n2=input("Enter Name1:")
x=['T','R','U','E','t','r','u','e']
t=0
l=['L','O','V','E','l','o','v','e']
lo=0
for i in range(len(n1)):
     if n1[i] in x:
         t+=1

for j in range(len(n2)):
     if n2[j] in x:
         t+=1        
for k in range(len(n1)):
     if n1[k] in l:
          lo+=1
for a in range(len(n2)):
     if n2[a] in l:
         lo+=1
s=str(t)+str(lo)
i=int(s)
if i<10 or i>90:
    print(f"Your score is:{s}, you go togethere like coke and mentos!") 


elif i>=40 and i<=50:
    print(f"Your score is:{s}, you are alright togethere.") 
else:
    print(f"your score is:{i}")
# print(f"Your Score is {t}{lo}")


# #Method 2
# print("The LOVE CALCULATOR is calculating your score.....")
# n1=input()
# n2=input()
# c=n1+n2
# k= c.lower()

# t=k.count('t')
# r=k.count('r')
# u=k.count('u')
# e=k.count('e')
# d1=t+r+u+e

# l=k.count('l')
# o=k.count('o')
# v=k.count('v')
# e=k.count('e')
# d2=l+o+v+e

# s=str(d1)+str(d2)
# i=int(s)
# if i<10 or i>90:
#     print(f"Your score is{s}, you go togethere like coke and mentos!") 


# elif i>=40 and i<=50:
#     print(f"Your score is{s}, you are alright togethere.") 
# else:
#     print(f"your score is{i}")
