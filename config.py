URL_russia = 'http://188.170.32.94:82/mjpg/video.mjpg'
MODE = 'http'


def validity_condition(LINE_X1,LINE_Y1,LINE_X2,LINE_Y2,x,y):
	x_list = []
	y_list = []
	for i in range(LINE_X1,LINE_X2):
		x_list.append(i)
	for j in range(LINE_Y1,LINE_Y2):
		y_list.append(j)
	if x in x_list and y in y_list:
		return True
	else:
		False
