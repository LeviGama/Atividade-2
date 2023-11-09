a = int(input("digite o valor A: " ) )
b = int(input("digite o valor B: " ) )
c = int(input("digite o valor C: " ) )

if a < b and a < c:
    print(f"o menor numero é {a}")

elif b < c and b < a:
    print(f"o menor numero é {b}")

else :
    print(f"o menor numero é {c}")