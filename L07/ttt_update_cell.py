# 撰寫一程式，檔案名稱 ttt_update_cell.py
# 定義棋盤格狀態變數 cell_1 ~ cell_9 與目前的棋子變數 chess 如下，
# 根據指定位置，更新對應的棋盤格狀態變數 cell_1 ~ cell_9，
# 設定該位置的棋盤格變數為目前的棋子值，並顯示棋盤狀態。

# 棋盤格變數：保存棋盤狀態的變數
# 變數編號對應的棋盤位置如下
#  1 | 2 | 3 
# ---+---+---
#  4 | 5 | 6 
# ---+---+---
#  7 | 8 | 9 
cell_1 = ' '
cell_2 = ' '
cell_3 = ' '
cell_4 = ' '
cell_5 = ' '
cell_6 = ' '
cell_7 = ' '
cell_8 = ' '
cell_9 = ' '
# 目前棋子變數：保存目前使用的棋子
chess = 'x'

# 使用者指定棋子位置
# TODO: 程式寫這裡
position = int(input())
# 根據指定位置，更新對應的棋盤格狀態變數 cell_1 ~ cell_9，
# TODO: 程式寫這裡

if position == 1:
    cell_1 = chess
elif position == 2:
    cell_2 = chess
elif position == 3:
    cell_3 = chess
elif position == 4:
    cell_4 = chess
elif position == 5:
    cell_5 = chess
elif position == 6:
    cell_6 = chess
elif position == 7:
    cell_7 = chess
elif position == 8:
    cell_8 = chess
elif position == 9:
    cell_9 = chess

# 顯示棋盤
# TODO: 程式寫這裡

print('',cell_1,'|',cell_2,'|',cell_3,'')
print('---+---+---')
print('',cell_4,'|',cell_5,'|',cell_6,'')
print('---+---+---')
print('',cell_7,'|',cell_8,'|',cell_9,'')