def test_primo(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n >= 3:
        i = n - 1
        while i >= 2:
            if n % i == 0:
                return False
            i -= 1
        else:
            return True

n = 0
while n < 100:
    n = n + 1
    if test_primo(n):
        print(f"{n}")

