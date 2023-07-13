# 双子素数を出力するプログラム
#
# %%
# まず、1000未満の素数のリストprimeを作成。
# この部分は修正しないでください。
prime = []
for i in range(2,1000):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        prime.append(i)

# %%
# ここに、上記で作成した素数リストprimeに
# 含まれる双子素数のペアをすべて印字する
# コードを書いてください。リストprimeを
# 利用していないコードは無効とし、0点と
# しますので注意してください。
#
# ヒント1:リストの長さを計算するには、関数
# lenを使います。
# 
# ヒント2:prime[i]+2とprime[i+1]が等しければ
# prime[i],prime[i+1]は双子素数であることが
# 分かります。
for i in range(len(prime)-1):
    if prime[i] + 2 == prime[i+1]:
        print(prime[i],prime[i+1])
# %%