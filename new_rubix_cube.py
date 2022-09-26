#Sides section
up = [['w','w','w'],
      ['w','W','w'],
      ['w','w','w']]

down = [['y','y','y'],
        ['y','Y','y'],
        ['y','y','y']]

right = [['r','r','r'],
        ['r','R','r'],
        ['r','r','r']]

left = [['o','o','o'],
         ['o','O','o'],
         ['o','o','o']]

front = [['b','b','b'],
         ['b','B','b'],
         ['b','b','b']]

back = [['g','g','g'],
        ['g','G','g'],
        ['g','g','g']]

def top_anticlock():
    #up movement(face movemnet)
    global up
    transposed_list = []
    for i in range(3):
      transposed_row=[]
      for j in range(2,-1,-1):
         a = up[j][i]
         transposed_row.append(a)
      transposed_list.append(transposed_row)
    up.clear() 
    up = transposed_list
    #sides rotation
    movment = [right[0][0:3]]
    right[0][0:3]=front[0][0:3]
    front[0][0:3]=left[0][0:3]
    left[0][0:3]=back[0][0:3]
    back[0][0:3]=movment

def top_clock():
    #up movement(face movemnet)
    global up
    transposed_list = []
    for i in range(2,-1,-1):
      transposed_row=[]
      for j in range(3):
         a = up[j][i]
         transposed_row.append(a)
      transposed_list.append(transposed_row)
    up.clear() 
    up = transposed_list
    #sides rotation
    movment = front[0][0:3]
    front[0][0:3]=right[0][0:3]
    right[0][0:3]=back[0][0:3]
    back[0][0:3]=left[0][0:3]
    left[0][0:3]=movment

def bottom_clock():
    #down movement(face movemnet)
    global down
    transposed_list = []
    for i in range(3):
      transposed_row=[]
      for j in range(2,-1,-1):
         a = down[j][i]
         transposed_row.append(a)
      transposed_list.append(transposed_row)
    down.clear() 
    down = transposed_list
    #sides rotation
    movment = right[2][0:3]
    right[2][0:3]=front[2][0:3]
    front[2][0:3]=left[2][0:3]
    left[2][0:3]=back[2][0:3]
    back[2][0:3]=movment

def bottom_anticlock():
    #down movement(face movemnet)
    global down
    transposed_list = []
    for i in range(2,-1,-1):
      transposed_row=[]
      for j in range(3):
         a = down[j][i]
         transposed_row.append(a)
      transposed_list.append(transposed_row)
    down.clear() 
    down = transposed_list
    #sides rotation
    movment = front[2][0:3]
    front[2][0:3]=right[2][0:3]
    right[2][0:3]=back[2][0:3]
    back[2][0:3]=left[2][0:3]
    left[2][0:3]=movment

def left_clock():
    global right
    #right movement(face movemnet)
    transposed_list = []
    for i in range(3):
      transposed_row=[]
      for j in range(2,-1,-1):
         a = right[j][i]
         transposed_row.append(a)
      transposed_list.append(transposed_row)
    right.clear() 
    right = transposed_list
    #sides rotation
    movment0 = front[0][0]
    movment1 = front[1][0]
    movment2 = front[2][0]
    front[0][0]=up[2][0]
    front[1][0]=up[1][0]
    front[2][0]=up[0][0]
    up[2][0]=back[0][2]
    up[1][0]=back[1][2]
    up[0][0]=back[2][2]
    back[0][2]=down[0][0]
    back[1][2]=down[1][0]
    back[2][2]=down[2][0]
    down[0][0]=movment0
    down[1][0]=movment1
    down[2][0]=movment2

def left_anticlock():
    global left
    #right movement(face movemnet)
    transposed_list = []
    for i in range(2,-1,-1):
      transposed_row=[]
      for j in range(3):
         a = left[j][i]
         transposed_row.append(a)
      transposed_list.append(transposed_row)
    left.clear() 
    left = transposed_list
    #sides rotation
    movment0 = up[0][0]
    movment1 = up[1][0]
    movment2 = up[2][0]
    up[0][0]=front[0][0]
    up[1][0]=front[1][0]
    up[2][0]=front[2][0]
    front[0][0]=down[0][0]
    front[1][0]=down[1][0]
    front[2][0]=down[2][0]
    down[0][0]=back[2][2]
    down[1][0]=back[1][2]
    down[2][0]=back[0][2]
    back[2][2]=movment0
    back[1][2]=movment1
    back[0][2]=movment2

def right_anticlock():
    global right
    #left movement(face movemnet)
    transposed_list = []
    for i in range(2,-1,-1):
      transposed_row=[]
      for j in range(3):
         a = right[j][i]
         transposed_row.append(a)
      transposed_list.append(transposed_row)
    right.clear() 
    right = transposed_list
    #sides rotation
    movment0 = front[0][2]
    movment1 = front[1][2]
    movment2 = front[2][2]
    front[0][2]=up[0][2]
    front[1][2]=up[1][2]
    front[2][2]=up[2][2]
    up[2][2]=back[0][0]
    up[1][2]=back[1][0]
    up[0][2]=back[2][0]
    back[0][0]=down[2][2]
    back[1][0]=down[1][2]
    back[2][0]=down[0][2]
    down[0][2]=movment0
    down[1][2]=movment1
    down[2][2]=movment2

def right_clock():
    global right
    #right movement(face movemnet)
    transposed_list = []
    for i in range(3):
      transposed_row=[]
      for j in range(2,-1,-1):
         a = right[j][i]
         transposed_row.append(a)
      transposed_list.append(transposed_row)
    right.clear() 
    right = transposed_list
    #sides rotation
    movment0 = up[2][2]
    movment1 = up[1][2]
    movment2 = up[0][2]
    up[0][2]=front[0][2]
    up[1][2]=front[1][2]
    up[2][2]=front[2][2]
    front[2][2]=down[2][2]
    front[1][2]=down[1][2]
    front[0][2]=down[0][2]
    down[2][2]=back[0][0]
    down[1][2]=back[1][0]
    down[0][2]=back[2][0]
    back[0][0]=movment0
    back[1][0]=movment1
    back[2][0]=movment2    

def front_anticlock():
    #front movement(face movement)
    global front
    transposed_list = []
    for i in range(2,-1,-1):
      transposed_row=[]
      for j in range(3):
         a = front[j][i]
         transposed_row.append(a)
      transposed_list.append(transposed_row)
    front.clear() 
    front = transposed_list
    #sides movement
    movment=left[0][2],left[1][2],left[2][2]
    left[2][2],left[1][2],left[0][2]=up[2][0:3]
    up[2][2::-1]=right[2][0],right[1][0],right[0][0]
    right[2][0],right[1][0],right[0][0]=down[0][0:3]
    down[0][0:3]=movment
  
def front_clock():
    #front movement(face movement)
    global front
    transposed_list = []
    for i in range(3):
      transposed_row=[]
      for j in range(2,-1,-1):
         a = front[j][i]
         transposed_row.append(a)
      transposed_list.append(transposed_row)
    front.clear() 
    front = transposed_list
    #sides movement
    movment=right[2][0],right[1][0],right[0][0]
    right[2][0],right[1][0],right[0][0]=up[2][0:3]
    up[2][0:3]=left[2][2],left[1][2],left[0][2]
    left[2][2],left[1][2],left[0][2]=down[0][0:3]
    down[0][0:3]=movment

def back_clock():
    #front movement(face movement)
    global back
    transposed_list = []
    for i in range(3):
      transposed_row=[]
      for j in range(2,-1,-1):
         a = back[j][i]
         transposed_row.append(a)
      transposed_list.append(transposed_row)
    back.clear() 
    back = transposed_list
    #sides movement
    movment=left[0][0],left[1][0],left[2][0]
    left[2][0],left[1][0],left[0][0]=up[0][0:3]
    up[0][0:3]=right[0][2],right[1][2],right[2][2]
    right[2][2],right[1][2],right[0][2]=down[2][0:3]
    down[2][0:3]=movment

def back_anticlock():
    #front movement(face movement)
    global back
    transposed_list = []
    for i in range(2,-1,-1):
      transposed_row=[]
      for j in range(3):
         a = back[j][i]
         transposed_row.append(a)
      transposed_list.append(transposed_row)
    back.clear() 
    back = transposed_list
    #sides movement
    #movment=right[2][0],right[1][0],right[0][0]
    #right[2][2],right[1][2],right[0][2]=up[0][0:3]
    #up[0][0],up[0][1],up[0][2]=left[2][0],left[1][0],left[0][0]
    #left[2][0],left[1][0],left[0][0]=down[2][0:3]
    #down[2][0:3]=movment
    movment0 = right[0][2]
    movment1 = right[1][2]
    movment2 = right[2][2]
    right[2][2] = up[0][0]
    right[1][2] = up[0][1]
    right[0][2] = up[0][2]
    up[0][0] =  left[2][0]
    up[0][1] =  left[1][0]
    up[0][2] =  left[0][0]
    left[2][0] = down[2][0]
    left[1][0] = down[2][1]
    left[0][0] = down[2][2]
    down[2][0] = movment0
    down[2][1] = movment1
    down[2][2] = movment2
run = True
while run:
  print("clock:[t,r,l,d,f,b]  anticlock:[T,R,L,D,F,B]")
  move = input("press any key from above:")
  if move == "t":
    top_clock()
  elif move == "T":
    top_anticlock()
  elif move == "r":
    right_clock()
  elif move == "R":
    right_anticlock()
  elif move == "l":
    left_clock()
  elif move == "L":
    left_anticlock()
  elif move == "d":
    bottom_clock()
  elif move == "D":
    bottom_anticlock()
  elif move == "f":
    front_clock()
  elif move == "F":
    front_anticlock()
  elif move == "b":
    back_clock()
  elif move == "B":
    back_anticlock()
  elif move == "Q":
    run = False
  elif move == "q":
    run = False
  else:
    print("invalid choice try again")
  #Print section
  #rubix_cube = [up , down , right , left , front , back]
  print("               ",up[0],"                 ")
  print("               ",up[1],"                 ")
  print("               ",up[2],"                 ")
  print(left[0],front[0],right[0],back[0])
  print(left[1],front[1],right[1],back[1])
  print(left[2],front[2],right[2],back[2])
  print("               ",down[0],"                 ")
  print("               ",down[1],"                 ")
  print("               ",down[2],"                 ")
