def calcul(a,b,cal):
	if cal == '+':
		print(f"{a} {cal} {b} = {a+b}")
	elif cal == '-':
		print(f"{a} {cal} {b} = {a+b}")
	elif cal == '*':
                print(f"{a} {cal} {b} = {(a*b):.2f}")
	elif cal == '/':
                print(f"{a} {cal} {b} = {(a/b):.2f}")
	else:
		print("Invalid !!!")

calcul(3, 9.8, '*')
