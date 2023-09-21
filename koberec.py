import tkinter as tk
# sierpinski triangle
root = tk.Tk()
canvas = tk.Canvas(root,width = 360, height = 360, bg = 'black')
canvas.pack()
a= 360

  
all_cords=[]
  
def sier(x,y,a,h):

  all_cords=[]
  for m in range(4):
    for n in range(4):
      all_cords.append((x+m*a//3,y-n*a//3))
  canvas.create_rectangle(all_cords[0],all_cords[5], outline= "lime")
  canvas.create_rectangle(all_cords[1],all_cords[6], outline= "red")
  canvas.create_rectangle(all_cords[2],all_cords[7], outline= "pink")
  canvas.create_rectangle(all_cords[4],all_cords[9], outline= "yellow")
  canvas.create_rectangle(all_cords[6],all_cords[11], outline= "turquoise")
  canvas.create_rectangle(all_cords[9],all_cords[14], outline= "orange")
  canvas.create_rectangle(all_cords[10],all_cords[15], outline= "white")
  canvas.create_rectangle(all_cords[8],all_cords[13], outline= "deepskyblue")

  if a>20:
    sier(all_cords[0][0],all_cords[0][1],a//3,4)
    sier(all_cords[1][0],all_cords[1][1],a//3,4)
    sier(all_cords[2][0],all_cords[2][1],a//3,4)
    sier(all_cords[4][0],all_cords[4][1],a//3,4)
    sier(all_cords[6][0],all_cords[6][1],a//3,4)
    sier(all_cords[8][0],all_cords[8][1],a//3,4)
    sier(all_cords[9][0],all_cords[9][1],a//3,4)
    sier(all_cords[10][0],all_cords[10][1],a//3,4)
         
    print(all_cords,len(all_cords))

sier(0,360, 360,1)

root.mainloop()
