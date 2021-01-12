# 撰寫一程式，檔案名稱 ttt_game.py
# 由兩方交替輸入棋子位置，'x' 棋為先手，'o' 棋為後手，
# 每一輪開始時，提示使用者輸入下棋位置，並檢查可否落子，落子失敗則退出程式，
# 成功落子後顯示棋盤狀態，並判斷勝負，勝利則顯示該方勝利，否則繼續下一輪


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

# 顯示棋盤
print('',cell_1,'|',cell_2,'|',cell_3,'')
print('---+---+---')
print('',cell_4,'|',cell_5,'|',cell_6,'')
print('---+---+---')
print('',cell_7,'|',cell_8,'|',cell_9,'')

# 第 1 輪
# 設定目前棋子 x 先
chess = 'x'
# 選擇位置
position = int(input('請輸入棋子位置：'))
# 檢查位置是否被佔用
# TODO: 程式寫這裡
is_occupied = True

if position == 1 and cell_1 !=' ' :
    is_occupied = False
elif position == 2 and cell_2 !=' ' :
    is_occupied = False
elif position == 3 and cell_3 !=' ' :
    is_occupied = False
elif position == 4 and cell_4 !=' ' :
    is_occupied = False
elif position == 5 and cell_5 !=' ' :
    is_occupied = False
elif position == 6 and cell_6 !=' ' :
    is_occupied = False
elif position == 7 and cell_7 !=' ' :
    is_occupied = False
elif position == 8 and cell_8 !=' ' :
    is_occupied = False
elif position == 9 and cell_9 !=' ' :
    is_occupied = False

if is_occupied == False:
    print('錯誤，此位置已經有棋子了，結束程式')
    exit()
# 更新棋盤變數
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
# 確認勝負
# TODO: 程式寫這裡

wins = (
    cell_1 == chess and cell_2 == chess and cell_3 == chess or 
    cell_4 == chess and cell_5 == chess and cell_6 == chess or 
    cell_7 == chess and cell_8 == chess and cell_9 == chess or  
    cell_1 == chess and cell_4 == chess and cell_7 == chess or  
    cell_2 == chess and cell_5 == chess and cell_8 == chess or
    cell_3 == chess and cell_6 == chess and cell_9 == chess or
    cell_1 == chess and cell_5 == chess and cell_9 == chess or
    cell_3 == chess and cell_5 == chess and cell_7 == chess 
)
if wins:
    print("x勝利，結束程式")
    exit()
# 第 2 輪
# 設定目前棋子
chess = 'o'
# 選擇位置
# TODO: 程式寫這裡
position = int(input('請輸入棋子位置：'))
# 檢查位置是否被佔用
# TODO: 程式寫這裡
is_occupied = True

if position == 1 and cell_1 !=' ' :
    is_occupied = False
elif position == 2 and cell_2 !=' ' :
    is_occupied = False
elif position == 3 and cell_3 !=' ' :
    is_occupied = False
elif position == 4 and cell_4 !=' ' :
    is_occupied = False
elif position == 5 and cell_5 !=' ' :
    is_occupied = False
elif position == 6 and cell_6 !=' ' :
    is_occupied = False
elif position == 7 and cell_7 !=' ' :
    is_occupied = False
elif position == 8 and cell_8 !=' ' :
    is_occupied = False
elif position == 9 and cell_9 !=' ' :
    is_occupied = False

if is_occupied == False:
    print('錯誤，此位置已經有棋子了，結束程式')
    exit()
# 更新棋盤變數
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
# 確認勝負
# TODO: 程式寫這裡
wins = (
    cell_1 == chess and cell_2 == chess and cell_3 == chess or 
    cell_4 == chess and cell_5 == chess and cell_6 == chess or 
    cell_7 == chess and cell_8 == chess and cell_9 == chess or  
    cell_1 == chess and cell_4 == chess and cell_7 == chess or  
    cell_2 == chess and cell_5 == chess and cell_8 == chess or
    cell_3 == chess and cell_6 == chess and cell_9 == chess or
    cell_1 == chess and cell_5 == chess and cell_9 == chess or
    cell_3 == chess and cell_5 == chess and cell_7 == chess 
)
if wins:
    print("o勝利，結束程式")
    exit()

# 第 3 輪
# 設定目前棋子
# TODO: 程式寫這裡
chess = 'x'
# 選擇位置
# TODO: 程式寫這裡
position = int(input('請輸入棋子位置：'))
# 檢查位置是否被佔用
# TODO: 程式寫這裡
is_occupied = True

if position == 1 and cell_1 !=' ' :
    is_occupied = False
elif position == 2 and cell_2 !=' ' :
    is_occupied = False
elif position == 3 and cell_3 !=' ' :
    is_occupied = False
elif position == 4 and cell_4 !=' ' :
    is_occupied = False
elif position == 5 and cell_5 !=' ' :
    is_occupied = False
elif position == 6 and cell_6 !=' ' :
    is_occupied = False
elif position == 7 and cell_7 !=' ' :
    is_occupied = False
elif position == 8 and cell_8 !=' ' :
    is_occupied = False
elif position == 9 and cell_9 !=' ' :
    is_occupied = False

if is_occupied == False:
    print('錯誤，此位置已經有棋子了，結束程式')
    exit()
# 更新棋盤變數
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
# 確認勝負
# TODO: 程式寫這裡
wins = (
    cell_1 == chess and cell_2 == chess and cell_3 == chess or 
    cell_4 == chess and cell_5 == chess and cell_6 == chess or 
    cell_7 == chess and cell_8 == chess and cell_9 == chess or  
    cell_1 == chess and cell_4 == chess and cell_7 == chess or  
    cell_2 == chess and cell_5 == chess and cell_8 == chess or
    cell_3 == chess and cell_6 == chess and cell_9 == chess or
    cell_1 == chess and cell_5 == chess and cell_9 == chess or
    cell_3 == chess and cell_5 == chess and cell_7 == chess 
)
if wins:
    print("x勝利，結束程式")
    exit()
# 第 4 輪
# 設定目前棋子
# TODO: 程式寫這裡
chess = 'o'
# 選擇位置
# TODO: 程式寫這裡
position = int(input('請輸入棋子位置：'))
# 檢查位置是否被佔用
# TODO: 程式寫這裡
is_occupied = True

if position == 1 and cell_1 !=' ' :
    is_occupied = False
elif position == 2 and cell_2 !=' ' :
    is_occupied = False
elif position == 3 and cell_3 !=' ' :
    is_occupied = False
elif position == 4 and cell_4 !=' ' :
    is_occupied = False
elif position == 5 and cell_5 !=' ' :
    is_occupied = False
elif position == 6 and cell_6 !=' ' :
    is_occupied = False
elif position == 7 and cell_7 !=' ' :
    is_occupied = False
elif position == 8 and cell_8 !=' ' :
    is_occupied = False
elif position == 9 and cell_9 !=' ' :
    is_occupied = False

if is_occupied == False:
    print('錯誤，此位置已經有棋子了，結束程式')
    exit()
# 更新棋盤變數
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
# 確認勝負
# TODO: 程式寫這裡
wins = (
    cell_1 == chess and cell_2 == chess and cell_3 == chess or 
    cell_4 == chess and cell_5 == chess and cell_6 == chess or 
    cell_7 == chess and cell_8 == chess and cell_9 == chess or  
    cell_1 == chess and cell_4 == chess and cell_7 == chess or  
    cell_2 == chess and cell_5 == chess and cell_8 == chess or
    cell_3 == chess and cell_6 == chess and cell_9 == chess or
    cell_1 == chess and cell_5 == chess and cell_9 == chess or
    cell_3 == chess and cell_5 == chess and cell_7 == chess 
)
if wins:
    print("o勝利，結束程式")
    exit()
# 第 5 輪
# 設定目前棋子
# TODO: 程式寫這裡
chess = 'x'
# 選擇位置
# TODO: 程式寫這裡
position = int(input('請輸入棋子位置：'))
# 檢查位置是否被佔用
# TODO: 程式寫這裡
is_occupied = True

if position == 1 and cell_1 !=' ' :
    is_occupied = False
elif position == 2 and cell_2 !=' ' :
    is_occupied = False
elif position == 3 and cell_3 !=' ' :
    is_occupied = False
elif position == 4 and cell_4 !=' ' :
    is_occupied = False
elif position == 5 and cell_5 !=' ' :
    is_occupied = False
elif position == 6 and cell_6 !=' ' :
    is_occupied = False
elif position == 7 and cell_7 !=' ' :
    is_occupied = False
elif position == 8 and cell_8 !=' ' :
    is_occupied = False
elif position == 9 and cell_9 !=' ' :
    is_occupied = False

if is_occupied == False:
    print('錯誤，此位置已經有棋子了，結束程式')
    exit()
# 更新棋盤變數
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
# 確認勝負
# TODO: 程式寫這裡
wins = (
    cell_1 == chess and cell_2 == chess and cell_3 == chess or 
    cell_4 == chess and cell_5 == chess and cell_6 == chess or 
    cell_7 == chess and cell_8 == chess and cell_9 == chess or  
    cell_1 == chess and cell_4 == chess and cell_7 == chess or  
    cell_2 == chess and cell_5 == chess and cell_8 == chess or
    cell_3 == chess and cell_6 == chess and cell_9 == chess or
    cell_1 == chess and cell_5 == chess and cell_9 == chess or
    cell_3 == chess and cell_5 == chess and cell_7 == chess 
)
if wins:
    print("x勝利，結束程式")
    exit()
# 第 6 輪
# 設定目前棋子
# TODO: 程式寫這裡
chess = 'o'
# 選擇位置
# TODO: 程式寫這裡
position = int(input('請輸入棋子位置：'))
# 檢查位置是否被佔用
# TODO: 程式寫這裡
is_occupied = True

if position == 1 and cell_1 !=' ' :
    is_occupied = False
elif position == 2 and cell_2 !=' ' :
    is_occupied = False
elif position == 3 and cell_3 !=' ' :
    is_occupied = False
elif position == 4 and cell_4 !=' ' :
    is_occupied = False
elif position == 5 and cell_5 !=' ' :
    is_occupied = False
elif position == 6 and cell_6 !=' ' :
    is_occupied = False
elif position == 7 and cell_7 !=' ' :
    is_occupied = False
elif position == 8 and cell_8 !=' ' :
    is_occupied = False
elif position == 9 and cell_9 !=' ' :
    is_occupied = False

if is_occupied == False:
    print('錯誤，此位置已經有棋子了，結束程式')
    exit()
# 更新棋盤變數
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
# 確認勝負
# TODO: 程式寫這裡
wins = (
    cell_1 == chess and cell_2 == chess and cell_3 == chess or 
    cell_4 == chess and cell_5 == chess and cell_6 == chess or 
    cell_7 == chess and cell_8 == chess and cell_9 == chess or  
    cell_1 == chess and cell_4 == chess and cell_7 == chess or  
    cell_2 == chess and cell_5 == chess and cell_8 == chess or
    cell_3 == chess and cell_6 == chess and cell_9 == chess or
    cell_1 == chess and cell_5 == chess and cell_9 == chess or
    cell_3 == chess and cell_5 == chess and cell_7 == chess 
)
if wins:
    print("o勝利，結束程式")
    exit()
# 第 7 輪
# 設定目前棋子
# TODO: 程式寫這裡
chess = 'x'
# 選擇位置
# TODO: 程式寫這裡
position = int(input('請輸入棋子位置：'))
# 檢查位置是否被佔用
# TODO: 程式寫這裡
is_occupied = True

if position == 1 and cell_1 !=' ' :
    is_occupied = False
elif position == 2 and cell_2 !=' ' :
    is_occupied = False
elif position == 3 and cell_3 !=' ' :
    is_occupied = False
elif position == 4 and cell_4 !=' ' :
    is_occupied = False
elif position == 5 and cell_5 !=' ' :
    is_occupied = False
elif position == 6 and cell_6 !=' ' :
    is_occupied = False
elif position == 7 and cell_7 !=' ' :
    is_occupied = False
elif position == 8 and cell_8 !=' ' :
    is_occupied = False
elif position == 9 and cell_9 !=' ' :
    is_occupied = False

if is_occupied == False:
    print('錯誤，此位置已經有棋子了，結束程式')
    exit()
# 更新棋盤變數
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
# 確認勝負
# TODO: 程式寫這裡
wins = (
    cell_1 == chess and cell_2 == chess and cell_3 == chess or 
    cell_4 == chess and cell_5 == chess and cell_6 == chess or 
    cell_7 == chess and cell_8 == chess and cell_9 == chess or  
    cell_1 == chess and cell_4 == chess and cell_7 == chess or  
    cell_2 == chess and cell_5 == chess and cell_8 == chess or
    cell_3 == chess and cell_6 == chess and cell_9 == chess or
    cell_1 == chess and cell_5 == chess and cell_9 == chess or
    cell_3 == chess and cell_5 == chess and cell_7 == chess 
)
if wins:
    print("x勝利，結束程式")
    exit()
# 第 8 輪
# 設定目前棋子
# TODO: 程式寫這裡
chess = 'o'
# 選擇位置
# TODO: 程式寫這裡
position = int(input('請輸入棋子位置：'))
# 檢查位置是否被佔用
# TODO: 程式寫這裡
is_occupied = True

if position == 1 and cell_1 !=' ' :
    is_occupied = False
elif position == 2 and cell_2 !=' ' :
    is_occupied = False
elif position == 3 and cell_3 !=' ' :
    is_occupied = False
elif position == 4 and cell_4 !=' ' :
    is_occupied = False
elif position == 5 and cell_5 !=' ' :
    is_occupied = False
elif position == 6 and cell_6 !=' ' :
    is_occupied = False
elif position == 7 and cell_7 !=' ' :
    is_occupied = False
elif position == 8 and cell_8 !=' ' :
    is_occupied = False
elif position == 9 and cell_9 !=' ' :
    is_occupied = False

if is_occupied == False:
    print('錯誤，此位置已經有棋子了，結束程式')
    exit()
# 更新棋盤變數
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
# 確認勝負
# TODO: 程式寫這裡
wins = (
    cell_1 == chess and cell_2 == chess and cell_3 == chess or 
    cell_4 == chess and cell_5 == chess and cell_6 == chess or 
    cell_7 == chess and cell_8 == chess and cell_9 == chess or  
    cell_1 == chess and cell_4 == chess and cell_7 == chess or  
    cell_2 == chess and cell_5 == chess and cell_8 == chess or
    cell_3 == chess and cell_6 == chess and cell_9 == chess or
    cell_1 == chess and cell_5 == chess and cell_9 == chess or
    cell_3 == chess and cell_5 == chess and cell_7 == chess 
)
if wins:
    print("o勝利，結束程式")
    exit()
# 第 9 輪
# 設定目前棋子
# TODO: 程式寫這裡
chess = 'x'
# 選擇位置
# TODO: 程式寫這裡
position = int(input('請輸入棋子位置：'))
# 檢查位置是否被佔用
# TODO: 程式寫這裡
is_occupied = True

if position == 1 and cell_1 !=' ' :
    is_occupied = False
elif position == 2 and cell_2 !=' ' :
    is_occupied = False
elif position == 3 and cell_3 !=' ' :
    is_occupied = False
elif position == 4 and cell_4 !=' ' :
    is_occupied = False
elif position == 5 and cell_5 !=' ' :
    is_occupied = False
elif position == 6 and cell_6 !=' ' :
    is_occupied = False
elif position == 7 and cell_7 !=' ' :
    is_occupied = False
elif position == 8 and cell_8 !=' ' :
    is_occupied = False
elif position == 9 and cell_9 !=' ' :
    is_occupied = False

if is_occupied == False:
    print('錯誤，此位置已經有棋子了，結束程式')
    exit()
# 更新棋盤變數
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
# 確認勝負
# TODO: 程式寫這裡
wins = (
    cell_1 == chess and cell_2 == chess and cell_3 == chess or 
    cell_4 == chess and cell_5 == chess and cell_6 == chess or 
    cell_7 == chess and cell_8 == chess and cell_9 == chess or  
    cell_1 == chess and cell_4 == chess and cell_7 == chess or  
    cell_2 == chess and cell_5 == chess and cell_8 == chess or
    cell_3 == chess and cell_6 == chess and cell_9 == chess or
    cell_1 == chess and cell_5 == chess and cell_9 == chess or
    cell_3 == chess and cell_5 == chess and cell_7 == chess 
)
if wins:
    print("x勝利，結束程式")
    exit()