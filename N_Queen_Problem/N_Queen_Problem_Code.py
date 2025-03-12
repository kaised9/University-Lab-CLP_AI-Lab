def isSafe(board,row,col,N):

  for i in range(col):
    if board[row][i]==1:
      return False

  for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
    if board[i][j]==1:
      return False

  for i,j in zip(range(row,N,1),range(col,-1,-1)):
    if board[i][j]==1:
      return False
  return True

def solveNQUtility(board,col,N):
  if col >= N:
    return True

  for i in range (N):
    if isSafe(board,i,col,N):
      board[i][col]=1

      if solveNQUtility(board,col+1,N):
        return True
      board[i][col]=0

  return False

def printSolution(N):
  board=[[0]*N for _ in range(N)]

  if not solveNQUtility(board,0,N):
    print("Solution Doesnot Exist !!!")
    return False

  print("Solution Found For",n,"Queens.")
  for i in range(N):
      for j in range(N):
        print(board[i][j],end=" ")
      print()
  return True


n=int (input("Enter Number Of Queen = "))
printSolution(n)
