n = input("enter your name ")
v =("aeiou")
vc = 0
for x in range(len(n)):
    if n[x] in v:
        vc += 1
    else:
        pass
print(n)
print("you have",vc,"vowels in your name")
