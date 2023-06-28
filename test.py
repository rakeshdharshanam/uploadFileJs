from flask import Flask,request,flash,session
import sys,os,json
from flask_cors import CORS,cross_origin 

app = Flask(__name__)
CORS(app)
app.secret_key  = 'test'

@app.route('/',methods = ["GET","POST"])
@cross_origin(origins='*')
def hello():
	flash("flash message")
	print(sys.getsizeof(request))
	if request.method == "GET":
		return "its GET method"
	print(request.data)
	return str(request.data)

@app.route("/upload",methods = ["GET","POST"])
def upload():
	if request.method == "POST":
		#print(request.data)
		data = request.data
		data = data.decode('ascii')
		print(type(data))
		data = json.loads(data)
		print((data['data']))
		with open(os.getcwd()+"/amshul.txt","wb") as f:
			f.write(request.data)
		return "not uploaded"

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=888,debug=True)
