file = [
  ['v', 'e', 'd', 'j', 'n', 's', 'e', 'o'],
  ['v', 'p', 'y', 't', 'h', 'o', 'n', 'o'],
  ['v', 'n', 'o', 'h', 't', 'y', 'p', 'o'],
]

def checkLeftToRight(matrix, word):
  for i in range(len(matrix)):
    count = 0
    positions = {}

    for j in range(len(matrix[i])):
      if count != len(word):
        if matrix[i][j] == word[count]:
          count += 1
          positions[matrix[i][j]] = { 'x': i, 'y': j }
      else:
        return positions

def checkRightToLeft(matrix, word):
  for i in range(len(matrix) - 1, -1, -1):
    count = 0
    positions = {}

    for j in range(len(matrix[i]) - 1, -1, -1):
      if count != len(word):
        if matrix[i][j] == word[count]:
          count += 1
          positions[matrix[i][j]] = { 'x': i, 'y': j }
      else:
        return positions

def generateFinalMatrix(matrix, positions): 
  width, height = len(matrix[0]), len(matrix)

  finalMatrix = [['.' for i in range(width)] for j in range(height)] 

  for position in positions:
    for word_position in position:
      x, y = position[word_position]['x'], position[word_position]['y']

      finalMatrix[x][y] = word_position
  
  return finalMatrix

positions = [
  checkLeftToRight(file, 'python'),
  checkRightToLeft(file, 'python')
]

board = generateFinalMatrix(file, positions)

for line in board:
  for column in line:
    print(column, end="")
  print()