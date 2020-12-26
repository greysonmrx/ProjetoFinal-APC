file = [
  ['o', 'n', 'e', 'd', 'j', 'n', 'f', 'o', 'f', 'i'],
  ['p', 'p', 'p', 'y', 't', 'h', 'o', 'n', 'd', 'n'],
  ['a', 'j', 'h', 'k', 'a', 'v', 'a', 'j', 'h', 't'],
  ['a', 's', 'm', 'a', 'o', 'v', 'a', 'o', 'v', 'j'],
  ['c', 'a', 'j', 'o', 't', 'v', 'b', 's', 'x', 'f'],
  ['n', 'd', 'a', 'g', 'a', 'a', 'a', 'v', 'c', 'o'],
  ['o', 'm', 'm', 'o', 'r', 'c', 'e', 'g', 'o', 'a'],
  ['s', 'd', 's', 'b', 'a', 'v', 'a', 'j', 'j', 'i'],
  ['j', 'g', 'o', 'l', 'a', 'v', 'a', 'c', 'l', 'v'],
  ['j', 'j', 'n', 'f', 'a', 'v', 'a', 's', 'o', 'a'],
]

# Verifica se a palavra está na horizontal da esquerda para a direita
def checkLeftToRight(matrix, word):
  for i in range(len(matrix)):
    count = 0
    positions = []

    for j in range(len(matrix[i])):
      if matrix[i][j] != word[count]:
        count = 0
        positions = []
      
      if matrix[i][j] == word[count]:
        positions.append([i, j, word[count]])
        count += 1

      if count == len(word):
        return positions

# Verifica se a palavra está na horizontal da direita para a esquerda 
def checkRightToLeft(matrix, word):
  for i in range(len(matrix) - 1, -1, -1):
    count = 0
    positions = []

    for j in range(len(matrix[i]) - 1, -1, -1):
      if matrix[i][j] != word[count]:
        count = 0
        positions = []
      
      if matrix[i][j] == word[count]:
        positions.append([i, j, word[count]])
        count += 1

      if count == len(word):
        return positions

# Verifica se a palavra está na vertical de cima para baixo
def checkTopToBottom(matrix, word):
  width, height = len(matrix[0]), len(matrix)

  for i in range(width):
    count = 0
    positions = []

    for j in range(height):
      if matrix[j][i] != word[count]:
        count = 0
        positions = []
      
      if matrix[j][i] == word[count]:
        positions.append([j, i, word[count]])
        count += 1

      if count == len(word):
        return positions

# Verifica se a palavra está na vertical de baixo para cima
def checkBottomToTop(matrix, word):
  width, height = len(matrix[0]), len(matrix)

  for i in range(width - 1, -1, -1):
    count = 0
    positions = []

    for j in range(height - 1, -1, -1):
      if matrix[j][i] != word[count]:
        count = 0
        positions = []
      
      if matrix[j][i] == word[count]:
        positions.append([j, i, word[count]])
        count += 1

      if count == len(word):
        return positions

# Verifica se a palavra está na diagonal da esquerda inferior para a direita superior
def checkBottomLeftToTopRight(matrix, word):
  width, height = len(matrix[0]), len(matrix)

  for i in range(width + height - 1):
    count = 0
    positions = []

    for j in range(width):
      if 0 <= i - j < height:
        if matrix[i - j][j] != word[count]:
          count = 0
          positions = []
        
        if matrix[i - j][j] == word[count]:
          positions.append([i - j, j, word[count]])
          count += 1

        if count == len(word):
          return positions

# Verifica se a palavra está na diagonal da direita superior para a esquerda inferior
def checkTopRightToBottomLeft(matrix, word):
  width, height = len(matrix[0]), len(matrix)

  for i in range(width + height - 2, -1, -1):
    count = 0
    positions = []

    for j in range(width - 1, -1 , -1):
      if 0 <= i - j < height:
        if matrix[i - j][j] != word[count]:
          count = 0
          positions = []
        
        if matrix[i - j][j] == word[count]:
          positions.append([i - j, j, word[count]])
          count += 1

        if count == len(word):
          return positions

# Verifica se a palavra está na diagonal da direita inferior para a esquerda superior
def checkBottomRightToTopLeft(matrix, word):
  width, height = len(matrix[0]), len(matrix)

  for i in range(width + height - 1):
    count = 0
    positions = []

    for j in range(width):
      if 0 <= width - i + j - 1 < height:
        if matrix[width - i + j - 1][j] != word[count]:
          count = 0
          positions = []
        
        if matrix[width - i + j - 1][j] == word[count]:
          positions.append([width - i + j - 1, j, word[count]])
          count += 1

        if count == len(word):
          return positions

# Verifica se a palavra está na diagonal da esquerda superior para a direita inferior
def checkTopLeftToBottomRight(matrix, word):
  width, height = len(matrix[0]), len(matrix)

  for i in range(width + height - 2, -1, -1):
    count = 0
    positions = []

    for j in range(width - 1, -1 , -1):
      if 0 <= width - i + j - 1 < height:
        if matrix[width - i + j - 1][j] != word[count]:
          count = 0
          positions = []
        
        if matrix[width - i + j - 1][j] == word[count]:
          positions.append([width - i + j - 1, j, word[count]])
          count += 1

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
  checkBottomToTop(file, 'aviao'),
  checkBottomToTop(file, 'json'),
  checkBottomLeftToTopRight(file, 'brabo'),
  checkTopRightToBottomLeft(file, 'ovo'),
  checkBottomRightToTopLeft(file, 'ava'),
  checkTopLeftToBottomRight(file, 'odo'),
]

board = generateFinalMatrix(file, positions)

for line in board:
  for column in line:
    print(column, end=" ")
  print()