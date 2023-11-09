print("!!! ATENÇÃO UTILIZE APENAS NÚMEROS INTEIROS E POSITIVOS! !!! ")

a = int(input("digite o valor A: " ) )
b = int(input("digite o valor B: " ) )
c = int(input("digite o valor C: " ) )

if a > b + c:

    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

    print (f"{a}, {b} e {c} formam um triângulo com a seguinte área: {area} ")
else:
    print(f"{a}, {b} e {c} não formam um triângulo :(")
