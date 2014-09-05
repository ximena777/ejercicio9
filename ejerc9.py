def suma_primos(a):
	con=1
	num=1
	con2=1
	cant=0
	suma=0
	while con<=a:
		while con2<=num:
			if num%con2==0:
				cant=cant+1
			con2=con2+1
		else:
			if cant==2:
				suma=suma+num
				con=con+1
			cant=0
			con2=1
			num=num+1
	else:
		print "para ",a ," la sumatoria de primos es: ",suma


x=int(raw_input("Ingrese Numero: "))
suma_primos(x)
