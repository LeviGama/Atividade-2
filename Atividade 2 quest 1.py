dias = int(input("Digite a idade em dias: "))

anos = dias // 365
sobra = dias % 365
meses = sobra // 30
sobra = sobra % 30

print (f"A idade é {anos} anos, {meses} meses e {sobra} dias :)")
