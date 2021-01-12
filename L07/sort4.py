# 撰寫一排序程式，檔案名稱 sort4.py
# 提示使用者輸入四個數字，將數字由大至小分行顯示

a = float(input())
b = float(input())
c = float(input())
d = float(input())

if d > c:
    c, d = d, c
if c > b:
    b, c = c, b
if b > a:
    a, b = b, a

if d > c:
    c, d = d, c
if c > b:
    b, c = c, b

if d > c:
    c, d = d, c

print(a)
print(b)
print(c)
print(d)