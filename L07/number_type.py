# 撰寫一程式，程式檔名為 number_type.py
# 提示使用者輸入一整數，判斷此數字的奇偶與正負。
# 並顯示結果，結果如 '正偶數'、'偶數'、'負偶數'、'正奇數'、'負奇數'。

x = int(input('請輸入數字:'))

if x % 2 ==0 :
    if x > 0 :
        print('正偶數')
    elif x == 0 :
        print('偶數')
    else :
        print('負偶數') 
else :
    if x > 0 :
        print('正奇數')
    elif x == 0 :
        print('奇數')
    else :
        print('負奇數') 

