n, x = map(int, input().split())

# n個の配列を入力
a = list(map(int, input().split()))

# xが配列に含まれているかどうか
flg = False
if x in a:
    flg = True

if flg:
    print("Yes")
else:
    print("No")
