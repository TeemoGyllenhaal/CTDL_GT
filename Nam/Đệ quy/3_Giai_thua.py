def giaithua(n):
    if n == 0:
        return 1
    else:
        giaithua = 1
        for i in range(1, n + 1):
            giaithua *= i
        return giaithua
print(giaithua(5)) # Kết quả: 120
