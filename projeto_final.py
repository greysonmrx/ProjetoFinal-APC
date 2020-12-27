# Pega as palavras de um arquivo
def getWords(file):
  file = open(file, 'r')
  words = []
  canReadWords = False

  for line in file:
    if line[0].isdigit():
      canReadWords = True
    else:
      if canReadWords:
        words.append(line.split()[0])
  
  return words

# Pega a matriz de um arquivo
def getMatrix(file):
  file = open(file, 'r')
  matrix = []
  canReadWords = False

  for line in file:
    if line[0].isdigit():
      break
    else:
      matrix.append(line.split())

  return matrix

# Verifica se a palavra está na horizontal
def checkWordHorizontally(matrix, word, reverse = False):
  if reverse:
    word = word[::-1]

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
  
  return False

# Verifica se a palavra está na vertical
def checkWordVertically(matrix, word, reverse = False):
  width, height = len(matrix[0]), len(matrix)

  if reverse:
    word = word[::-1]

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
  
  return False

# Verifica se a palavra está nas diagonais em direção à diagonal secundária
def checkWordDiagonallyTowardsTheSecondaryDiagonal(matrix, word, reverse = False):
  width, height = len(matrix[0]), len(matrix)

  if reverse:
    word = word[::-1]

  for i in range(width + height - 1):
    count = 0
    positions = []

    for j in range(width):
      row = i - j

      if 0 <= row < height:
        if matrix[row][j] != word[count]:
          count = 0
          positions = []
        
        if matrix[row][j] == word[count]:
          positions.append([row, j, word[count]])
          count += 1

        if count == len(word):
          return positions
    
  return False

# Verifica se a palavra está nas diagonais em direção à diagonal principal
def checkWordDiagonallyTowardsTheMainDiagonal(matrix, word, reverse = False):
  width, height = len(matrix[0]), len(matrix)

  if reverse:
    word = word[::-1]

  for i in range(width + height - 1):
    count = 0
    positions = []

    for j in range(width):
      row = width - i + j - 1

      if 0 <= row < height:
        if matrix[row][j] != word[count]:
          count = 0
          positions = []
        
        if matrix[row][j] == word[count]:
          positions.append([row, j, word[count]])
          count += 1

        if count == len(word):
          return positions
    
  return False

# Procura uma palavra em todas as direções na matriz
def getWordPosition(matrix, word):
  for i in range(2):
    horizontalPositions = checkWordHorizontally(matrix, word, i == 1)
    verticalPositions = checkWordVertically(matrix, word, i == 1)
    secondaryDiagonalPositions = checkWordDiagonallyTowardsTheSecondaryDiagonal(matrix, word, i == 1)
    mainDiagonalPositions = checkWordDiagonallyTowardsTheMainDiagonal(matrix, word, i == 1)
    
    if horizontalPositions:
      return horizontalPositions
    elif verticalPositions:
      return verticalPositions
    elif secondaryDiagonalPositions:
      return secondaryDiagonalPositions
    elif mainDiagonalPositions:
      return mainDiagonalPositions
  
  return False

# Gera a matriz com as palavras encontradas
def generateFinalMatrix(matrix, words_coords): 
  width, height = len(matrix[0]), len(matrix)

  finalMatrix = [['.' for i in range(width)] for j in range(height)]

  for word_coords in words_coords:
    for letter_coords in word_coords:
      x, y, letter = letter_coords

      finalMatrix[x][y] = letter

  return finalMatrix

# Escreve o quadro com as palavras encontradas em um arquivo
def writeFile(matrix, positions, file_name):
  file = open(file_name, 'w')

  board = generateFinalMatrix(matrix, positions)

  for line in board:
    for column in line:
      print(column, end=" ")
      print(column, end=" ", file=file)

    file.write('\n')
    print()

  file.close()
  print()

def main():
  files = ['arq1', 'arq2', 'arq3']

  for file in files:
    words = getWords(file + '.in')
    matrix = getMatrix(file + '.in')
    positions = []

    for word in words:
      wordPosition = getWordPosition(matrix, word)

      if wordPosition:
        positions.append(wordPosition)

    writeFile(matrix, positions, file + '.res')

main()