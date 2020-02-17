import tkinter as tk
import PIL as p
import PIL.ImageTk as ptk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageEnhance
import random
import tkinter.messagebox as box



xxxx = tk.Tk()
xxxx.title('XXXX')

def check_for_win(zone):
	win = False
	if p1 == True:
		x = 1
	else:
		x = 0

	for row in range(len(gb)):
		print(gb[row])
		if (gb[row]) == [x,x,x,x]:
			win = True

	for column in range(4):
		if gb[0][column] == x and gb[1][column] == x and gb[2][column] == x  and gb[3][column] == x:
			win = True

	if gb[0][0] == x and gb[1][1] == x and gb[2][2] == x and gb[3][3] == x:
		win = True

	if gb[0][3] == x and gb[1][2] == x and gb[2][1] == x and gb[3][0] == x:
		win = True

	if 9 not in gb[0]:
			if 9 not in gb[1]:
					if 9 not in gb[2]:
							if 9 not in gb[3]:
								box.showinfo('TIE')

	if win == True:
		if x == 1:
			x = 'CROSSES'
		else:
			x = 'NOUGHTS'
		box.showinfo('GAME OVER', 'The winner is {}!'.format(x))





def initboard():

	def click(zone,r,c):
		global p1
		global gb

		zone['command'] = 0

		if p1 == False:
			zone.image = nought															
			zone.configure(image=nought)
			gb[r][c] = 0
		else:
			zone.image = cross
			zone.configure(image=cross)
			gb[r][c] = 1

		check_for_win(zone)
		p1 = not p1




	z0 = tk.Button(xxxx, image=blank, command=lambda: click(z0,0,0), borderwidth=0)
	z0.image = blank	
	z0.grid(row=0, column=0)

	z1 = tk.Button(xxxx, image=blank, command=lambda: click(z1,0,1), borderwidth=0)
	z1.image = blank	
	z1.grid(row=0, column=1)

	z2 = tk.Button(xxxx, image=blank, command=lambda: click(z2,0,2), borderwidth=0)
	z2.image = blank	
	z2.grid(row=0, column=2)

	z3 = tk.Button(xxxx, image=blank, command=lambda: click(z3,0,3), borderwidth=0)
	z3.image = blank	
	z3.grid(row=0, column=3)

	z4 = tk.Button(xxxx, image=blank, command=lambda: click(z4,1,0), borderwidth=0)
	z4.image = blank	
	z4.grid(row=1, column=0)

	z5 = tk.Button(xxxx, image=blank, command=lambda: click(z5,1,1), borderwidth=0)
	z5.image = blank	
	z5.grid(row=1, column=1)

	z6 = tk.Button(xxxx, image=blank, command=lambda: click(z6,1,2), borderwidth=0)
	z6.image = blank	
	z6.grid(row=1, column=2)

	z7 = tk.Button(xxxx, image=blank, command=lambda: click(z7,1,3), borderwidth=0)
	z7.image = blank	
	z7.grid(row=1, column=3)

	z8 = tk.Button(xxxx, image=blank, command=lambda: click(z8,2,0), borderwidth=0)
	z8.image = blank	
	z8.grid(row=2, column=0)

	z9 = tk.Button(xxxx, image=blank, command=lambda: click(z9,2,1), borderwidth=0)
	z9.image = blank	
	z9.grid(row=2, column=1)

	z10 = tk.Button(xxxx, image=blank, command=lambda: click(z10,2,2), borderwidth=0)
	z10.image = blank	
	z10.grid(row=2, column=2)

	z11 = tk.Button(xxxx, image=blank, command=lambda: click(z11,2,3), borderwidth=0)
	z11.image = blank	
	z11.grid(row=2, column=3)

	z12 = tk.Button(xxxx, image=blank, command=lambda: click(z12,3,0), borderwidth=0)
	z12.image = blank	
	z12.grid(row=3, column=0)

	z13 = tk.Button(xxxx, image=blank, command=lambda: click(z13,3,1), borderwidth=0)
	z13.image = blank	
	z13.grid(row=3, column=1)

	z14 = tk.Button(xxxx, image=blank, command=lambda: click(z14,3,2), borderwidth=0)
	z14.image = blank	
	z14.grid(row=3, column=2)

	z15 = tk.Button(xxxx, image=blank, command=lambda: click(z15,3,3), borderwidth=0)
	z15.image = blank	
	z15.grid(row=3, column=3)

blankraw = p.Image.open('bl.png')
crossraw = p.Image.open('x2.png')
noughtraw = p.Image.open('o2.png')
blank = ptk.PhotoImage(blankraw)
cross = ptk.PhotoImage(crossraw)
nought = ptk.PhotoImage(noughtraw)
p1 = True
gb = [[9,9,9,9],[9,9,9,9],[9,9,9,9],[9,9,9,9]]



initboard()


"""
canvas1 = Canvas(xxxx, width=100, height = 100, background='white')
canvas1.grid(row=0, column =0)
canvas2 = Canvas(xxxx, width=100, height = 100, background='white')
canvas2.grid(row=0, column =1)
canvas3 = Canvas(xxxx, width=100, height = 100, background='white')
canvas3.grid(row=0, column =2)
canvas4 = Canvas(xxxx, width=100, height = 100, background='white')
canvas4.grid(row=0, column =3)
canvas5 = Canvas(xxxx, width=100, height = 100, background='white')
canvas5.grid(row=1, column =0)
canvas6 = Canvas(xxxx, width=100, height = 100, background='white')
canvas6.grid(row=1, column =1)
canvas7 = Canvas(xxxx, width=100, height = 100, background='white')
canvas7.grid(row=1, column =2)
canvas8 = Canvas(xxxx, width=100, height = 100, background='white')
canvas8.grid(row=1, column =3)
canvas9 = Canvas(xxxx, width=100, height = 100, background='white')
canvas9.grid(row=2, column =0)
canvas10 = Canvas(xxxx, width=100, height = 100, background='white')
canvas10.grid(row=2, column =1)
canvas11 = Canvas(xxxx, width=100, height = 100, background='white')
canvas11.grid(row=2, column =2)
canvas12 = Canvas(xxxx, width=100, height = 100, background='white')
canvas12.grid(row=2, column =3)
canvas13 = Canvas(xxxx, width=100, height = 100, background='white')
canvas13.grid(row=3, column =0)
canvas14 = Canvas(xxxx, width=100, height = 100, background='white')
canvas14.grid(row=3, column =1)
canvas15 = Canvas(xxxx, width=100, height = 100, background='white')
canvas15.grid(row=3, column =2)
canvas16 = Canvas(xxxx, width=100, height = 100, background='white')
canvas16.grid(row=3, column =3)
"""








xxxx.mainloop()
