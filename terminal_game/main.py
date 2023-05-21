class Gameboard: 
  def __init__(self):
    self.matrix = [[1,2,3],[4,5,6],[7,8,9]]

  def print_board(self):
    for row in self.matrix:
        for index in row:
            print(index, end = '    ')
        print('\n')

  def edit(self, player, position):
    if type(player) == Player and type(position) == int:
      for i in range(len(self.matrix)):
        for j in range(len(self.matrix[i])):
          if self.matrix[i][j] == position and type(self.matrix[i][j]) == int:
            self.matrix[i][j] = player.symbol
        
  def check(self):
    for row in self.matrix:
      counter = 0
      for num in row:
        if num == 'x':
          counter += 1
        if counter == 3:
          return 'x'
        elif counter == 0:
          return 'o'
        else: 
          continue
    for j in range(3):
      counter = 0
      for i in range(3):
        if self.matrix[i][j] == 'x':
          counter += 0
      if counter == 3:
          return 'x'
      elif counter == 0:
          return 'o'
      else: 
          continue
    for i in range(3):
      for j in range(3):
        if i == j:
          if self.matrix == 'x':
            counter += 1
          
  def clear(self):
    self.matrix = [[1,2,3],[4,5,6],[7,8,9]]
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
      
token = True

   
gameboard.print_board()
player1 = Player('x', 'Jack')
gameboard.edit(player1, 10)
gameboard.print_board()
  
