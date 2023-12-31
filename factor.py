# 素因数分解のプログラム
# 
# %%
# 2から100までの範囲の整数すべてに対して
# 素因数をすべて出力します。
#
for i in range(2,101):
    print(i,end='...')
    #
    # この部分に、iのすべての素因数を
    # 空白で区切って出力するコードを
    # 書きなさい。
    #
    # 注)この部分以外を編集した回答は
    # 無効とし、0点とします。また、
    # 自作でないパッケージやモジュール
    # を使ったものも0点とします。
    #
    # ヒント1:二重ループを使いましょう。
    # ヒント2:整数iが整数jで何回割れ
    # るか調べる方法から考えてみてください。
    # ヒント3:整数除算演算子//もしくは
    # 代入演算子//=が必要です。
    div = i
    for j in range(2,i+1):
        while div % j == 0:
            div //= j
            print(j,end=' ')
    print()
# %%
