# 棋盤格變數：保存棋盤狀態的變數
# 變數編號對應的棋盤位置如下
#  1 | 2 | 3 
# ---+---+---
#  4 | 5 | 6 
# ---+---+---
#  7 | 8 | 9 
cell_1 = 'x'
cell_2 = 'x'
cell_3 = 'o'
cell_4 = ' '
cell_5 = 'o'
cell_6 = ' '
cell_7 = 'x'
cell_8 = ' '
cell_9 = ' '

# 讀取棋盤狀態變數 (cell_1 ... cell9) ，顯示棋盤
# 顯示棋盤結果如下
#  x | x | o 
# ---+---+---
#    | o |   
# ---+---+---
#  x |   |   
print(cell_1,"|",cell_2,"|",cell_3)
print("---+---+---")
print(cell_4,"|",cell_5,"|",cell_6)
print("---+---+---")
print(cell_7,"|",cell_8,"|",cell_9)