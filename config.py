URL_russia = 'http://188.170.32.94:82/mjpg/video.mjpg'
MODE = 'http'


def validity_condition(LINE_X1,LINE_Y1,LINE_X2,LINE_Y2,x,y,w,h,sensitivity):
	x_list = []
	y_list = []
	for i in range(LINE_X1 - w//sensitivity,LINE_X2 + w//sensitivity):
		x_list.append(i)
	for j in range(LINE_Y1 - h//sensitivity,LINE_Y2 + h//sensitivity):
		y_list.append(j)
	if x in x_list and y in y_list:
		return True
	else:
		False
