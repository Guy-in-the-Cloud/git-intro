from sympy import isprime

n = int(input("Enter the nth prime: ")) # nth prime number

out = 2
count = 1
index = 1


while count - 1 != n: # 2 != 3

    if isprime(index): # isprime(3)
        out = index # out = 3
        count+=1 # count = 3
    
    index += 1         # index = 3

print(out)

# why...
# bhavika was here :)