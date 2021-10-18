a="123"
b=3
while b>0:
	wd=input("enter passwprd: ")
	if (wd==a):
		print("successfully logged in")
		break
	else:
		b=b-1
		print("wrong password")
		print(f"{b} attempts left")
