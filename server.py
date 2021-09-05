from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
	packet = {}
	
	f = open("buffer.txt","r")
	data = f.readline()
	
	l = data.split(',')
	
	packet['total_count'] = l[0]
	packet['instant_count'] = l[1]
	packet['frame_rate'] = l[2]
	packet['active'] = l[3]
	
	return packet

if __name__ == '__main__':
	app.run(debug=True)