#Prabhat Panwar
#TSF TASK 5:Color detection using OpenCV
#Computer Vision and IOT

import cv2           #importing libraries
import pandas as pd

clicked = False              #global variables
r = g = b = xpos = ypos = 0

img_path = 'color.jpg'
csv_path = 'colors.csv'

# Reading csv file
index = ['color', 'color_name', 'hex', 'R', 'G', 'B']
df = pd.read_csv(csv_path, names=index, header=None)

img = cv2.imread(img_path)
img = cv2.resize(img, (800,600))

def get_color(R,G,B):                            # function to calculate minimum distance from all colors
	minimum = 1000
	for i in range(len(df)):
		d = abs(R - int(df.loc[i,'R'])) + abs(G - int(df.loc[i,'G'])) + abs(B - int(df.loc[i,'B']))
		if d <= minimum:
			minimum = d
			cname = df.loc[i, 'color_name']

	return cname

def draw(event, x, y, flags, params):           # function to get x,y coordinates of mouse double click
	if event == cv2.EVENT_LBUTTONDBLCLK:
		global b, g, r, xpos, ypos, clicked
		clicked = True
		xpos = x
		ypos = y
		b,g,r = img[y,x]
		b = int(b)
		g = int(g)
		r = int(r)

cv2.namedWindow('img')
cv2.setMouseCallback('img', draw)

while True:
	cv2.imshow('img', img)
	if clicked:
		cv2.rectangle(img, (20,20), (600,60), (b,g,r), -1)

		text = get_color(r,g,b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)
		cv2.putText(img, text, (50,50), 2,0.8, (255,255,255),2,cv2.LINE_AA)


		if r+g+b >=600:
			cv2.putText(img, text, (50,50), 2,0.8, (0,0,0),2,cv2.LINE_AA)

	if cv2.waitKey(20) & 0xFF == 27:
		break

cv2.destroyAllWindows()