

class Gameboard: 
  def __init__(self):
    self.matrix = {1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9'}



  def print_board(self):
    print(f"{self.matrix[1][1]}|{self.matrix[2]}|{self.matrix[3]}\n"
          f"{self.matrix[4]}|{self.matrix[5]}|{self.matrix[6]}\n"
          f"{self.matrix[7]}|{self.matrix[8]}|{self.matrix[9]}\n")
    
  def edit(self, player, position):
    if type(player) == Player and type(position) == int:
      for i in range(len(self.matrix)):
        for j in range(len(self.matrix[i])):
          if self.matrix[i][j] == position and type(self.matrix[i][j]) == int:
            self.matrix[i][j] = player.symbol
        
  def check(self):
    for i in range(0,3):
      if (self.matrix[1+i] == 'x' and self.matrix[2+i] == 'x' and self.matrix[3+i] == 'x'):
        return 'x'
      
          
  def clear(self):
    self.matrix = {1: ['1','x','o'], 2:['2','x','o'], 3:['3','x','o'], 4:['4'], 5:'5', 6:'6', 7:'7', 8:'8', 9:'9'}
    return 'New Game!'


gameboard = Gameboard()

class Player:
  def __init__(self, symbol, name):
    self.name = name
    self.symbol = symbol
    self.win = False
    self.score = 0

  def win_status(self):
    if gameboard.check() == 'x' and self.symbol == 'x':
      self.win = True
    elif gameboard.check() == 'o' and self.symbol == 'o':
      self.win = True

blah = True
while()
choice1_name = input('Enter Player 1 name')

choice1_symbol = input('Enter Symbol')
player1 = Player(choice1_symbol, choice1_name)

choice2_name = input('Enter Player 2 name')
if 

choice2_name
playing = True
turn = 0
while playing == True:
  gameboard.print_board()
  choice = input()
  player1 = Player('x', 'Jack')
  gameboard.edit(player1, 10)
  gameboard.print_board()
    
