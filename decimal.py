b=int(input("enter the binary number"))
d=0
i=0
while(b!=0):
	dig=b%10
	d=d+(dig*(2**i))
	i=i+1
	b=b//10
print("decimal eqivalent is",d)