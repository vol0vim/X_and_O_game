# Игра в крестики-нолики для двоих человек
game_map =[[".",".","."],
          [".",".","."],
          [".",".","."]]
          
#рисуем игровое поле с совершенными ходами   
def print_game_map(): 
    i=0
    print(" "*3, "0","1","2")
    print(" "*2,"_"*6)
    for i in range(3):
       print(i, "|", game_map[i][0], game_map[i][1], game_map[i][2] )

#получает ход игрока и вносим его на игровое поле
def player_xod (symbol): 
    print('Игрок "', symbol, '" Сделайте свой ход (в формате "0 2"(№строки №столбца)):')
    coordinate = list(map(int, input().split(" ")))
    game_map[coordinate[0]][coordinate[1]]= symbol

#Проверка выйгрыша
def check_winner(symbol):
    winner = ""
    i=0
    j=0
    for i in range(3):
        if game_map[i][0] == symbol and game_map[i][1] == symbol and game_map[i][2] == symbol:
            winner = symbol
    for j in range(3):
        if game_map[0][j] == symbol and game_map[1][j] == symbol and game_map[2][j] == symbol:
            winner = symbol
    if game_map[0][0] == symbol and game_map[1][1] == symbol and game_map[2][2] == symbol:
        winner = symbol
    if game_map[0][2] == symbol and game_map[1][1] == symbol and game_map[2][0] == symbol:
        winner = symbol   
    return winner


# Основная программа
have_a_winner = False
player_1 = True
winner = ""
while have_a_winner == False:
    print_game_map()
    if player_1 == True:
        symbol = "X"
        player_xod (symbol)
        winner=check_winner(symbol)
        player_1 = False
    else:
        symbol = "O"
        player_xod (symbol)
        winner=check_winner(symbol)
        player_1 = True
    if winner == "X" or winner == "O":
        have_a_winner = True
    else:
        have_a_winner = False

print_game_map() 
print('Игрок "', winner, '" ПОБЕДИЛ')     
 
