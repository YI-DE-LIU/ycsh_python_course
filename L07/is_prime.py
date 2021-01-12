# 撰寫一程式，程式檔名為 is_prime.py
# 提示使用者輸入一數字（100 以內的正整數），判斷此數字是否為質數，
# 若為質數，顯示 '是質數' ，反之顯示 '不是質數' 。

n = int(input())

is_prime = False

if n == 2:
    is_prime = True
if n == 3:
    is_prime = True
if n == 5:
    is_prime = True
if n == 7:
    is_prime = True
if n == 11:
    is_prime = True
if n == 13:
    is_prime = True
if n == 17:
    is_prime = True
if n == 19:
    is_prime = True
if n == 23:
    is_prime = True
if n == 29:
    is_prime = True
if n == 31:
    is_prime = True
if n == 37:
    is_prime = True
if n == 41:
    is_prime = True
if n == 43:
    is_prime = True
if n == 47:
    is_prime = True
if n == 53:
    is_prime = True
if n == 59:
    is_prime = True
if n == 61:
    is_prime = True
if n == 67:
    is_prime = True
if n == 71:
    is_prime = True
if n == 73:
    is_prime = True
if n == 79:
    is_prime = True
if n == 83:
    is_prime = True
if n == 89:
    is_prime = True
if n == 97:
    is_prime = True

if is_prime:
    print('是質數')
else:
    print('不是質數')

#若是全為if會使其速度變慢，每次都需判斷全部，因此可改為elif