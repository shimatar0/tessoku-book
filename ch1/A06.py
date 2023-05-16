n, q = map(int, input().split())

a = list(map(int, input().split()))
ll = []
for i in range(q):
    ll.append(list(map(int, input().split())))

# 累積和を計算しておく
ruiseki = [0] * n
for i, v in enumerate(a):
    if i == 0:
        ruiseki[i] = v
    else:
        ruiseki[i] = ruiseki[i-1] + v

ruiseki.insert(0, 0)

# クエリを処理する
for v in ll:
    print(ruiseki[v[1]] - ruiseki[v[0]-1])
