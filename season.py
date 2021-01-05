month = int(input())
if month >= 2 and month <= 4:
    print("春天")
elif month >= 5 and month <= 7:
    print("夏天")
elif month >= 8 and month <= 10:
    print("秋天")
elif month ==11 or month == 1 or month == 2 :
    print("冬天")
else:
    print("輸入錯誤")
