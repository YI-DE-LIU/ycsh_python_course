# 撰寫一排序程式，檔案名稱 sort3.py
# 提示使用者輸入三個數字，將數字由大至小分行顯示

a = float(input())
b = float(input())
c = float(input())

x = max(a,b,c)
z = min(a,b,c)
y = a+b+c-x-z

print(x)
print(y)
print(z)