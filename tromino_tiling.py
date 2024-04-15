def tromino(n)
  n = int(input('Enter the number of dimensions')
  tromino_table = [2^n*2^n][2^n*2^n]
  if n==1
    tromino_table[1][1] = 'G'
    tromino_table[1][2] = 'X'
    tromino_table[2][1] = 'G'
  ` tromino_table[2][2] = 'G'
 elif n==2
    tromino_table[1][1] = 'B'
    tromino_table[1][2] = 'B'
    tromino_table[1][3] = 'R'
    tromino_table[1][4] = 'R'
    tromino_table[2][1] = 'B'
    tromino_table[2][2] = 'G'
    tromino_table[2][3] = 'G'
    tromino_table[2][4] = 'R'
    tromino_table[3][1] = 'R'
    tromino_table[3][2] = 'G'
    tromino_table[3][3] = 'B'
    tromino_table[3][4] = 'B'
    tromino_table[4][1] = 'R'
    tromino_table[4][2] = 'R'
    tromino_table[4][3] = 'B'
    tromino_table[4][4] = 'X'

  
  
