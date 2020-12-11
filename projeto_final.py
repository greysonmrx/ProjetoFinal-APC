file = [
  ['o', 'n', 'e', 'd', 'j', 'n', 's', 'e', 'f', 'i'],
  ['p', 't', 'p', 'y', 't', 'h', 'o', 'n', 'd', 'n'],
  ['a', 'j', 'j', 'k', 'a', 'v', 'a', 'j', 'h', 't'],
  ['g', 's', 'm', 'j', 'a', 'v', 'a', 'a', 'v', 'j'],
  ['c', 'w', 'j', 'h', 'a', 'v', 'a', 's', 'x', 'f'],
  ['a', 'd', 'v', 'g', 'a', 'v', 'a', 'v', 'c', 'o'],
  ['r', 'a', 'm', 'o', 'r', 'c', 'e', 'g', 'o', 'a'],
  ['r', 'd', 's', 'a', 'a', 'v', 'a', 'j', 'v', 'i'],
  ['o', 'g', 'o', 'l', 'a', 'v', 'a', 'c', 'l', 'v'],
  ['a', 'j', 'n', 'f', 'a', 'v', 'a', 's', 'o', 'a'],
]

# Verifica se a palavra está na horizontal da esquerda para a direita
def checkLeftToRight(matrix, word):
  for i in range(len(matrix)):
    count = 0
    positions = []

    for j in range(len(matrix[i])):
      if matrix[i][j] == word[count]:
        positions.append([i, j, word[count]])
        count += 1
      elif count > 0 and count != len(word):
        count = 0
        positions = []

      if count == len(word):
        return positions

# Verifica se a palavra está na horizontal da direita para a esquerda 
def checkRightToLeft(matrix, word):
  for i in range(len(matrix) - 1, -1, -1):
    count = 0
    positions = []

    for j in range(len(matrix[i]) - 1, -1, -1):
      if matrix[i][j] == word[count]:
        positions.append([i, j, word[count]])
        count += 1
      elif count > 0 and count != len(word):
        count = 0
        positions = []

      if count == len(word):
        return positions

# Verifica se a palavra está na vertical de cima para baixo
def checkTopToBottom(matrix, word):
  width, height = len(matrix[0]), len(matrix)

  for i in range(width):
    count = 0
    positions = []

    for j in range(height):
      if matrix[j][i] == word[count]:
        positions.append([j, i, word[count]])
        count += 1
      elif count > 0 and count != len(word):
        count = 0
        positions = []

      if count == len(word):
        return positions

# Verifica se a palavra está na vertical de baixo para cima
def checkBottomToTop(matrix, word):
  width, height = len(matrix[0]), len(matrix)

  for i in range(width - 1, -1, -1):
    count = 0
    positions = []

    for j in range(height - 1, -1, -1):
      if matrix[j][i] == word[count]:
        positions.append([j, i, word[count]])
        count += 1
      elif count > 0 and count != len(word):
        count = 0
        positions = []

      if count == len(word):
        return positions
    
# Gera a matriz com as palavras encontradas
def generateFinalMatrix(matrix, words_coords): 
  width, height = len(matrix[0]), len(matrix)

  finalMatrix = [['.' for i in range(width)] for j in range(height)]

  for word_coords in words_coords:
    for letter_coords in word_coords:
      x, y, letter = letter_coords

      finalMatrix[x][y] = letter

  return finalMatrix

positions = [
  checkTopToBottom(file, 'opa'),
  checkTopToBottom(file, 'int'),
  checkLeftToRight(file, 'python'),
  checkLeftToRight(file, 'morcego'),
  checkRightToLeft(file, 'cavalo'),
  checkRightToLeft(file, 'java'),
  checkRightToLeft(file, 'if'),
  checkBottomToTop(file, 'aviao')
]

board = generateFinalMatrix(file, positions)

for line in board:
  for column in line:
    print(column, end="")
  print()