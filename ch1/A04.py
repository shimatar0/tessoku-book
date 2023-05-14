n = int(input())

# nを2進数に変換
n2 = bin(n)[2:]

# 2進数を10桁で0埋め
n2 = n2.zfill(10)
print(n2)
