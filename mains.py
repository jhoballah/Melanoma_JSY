from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'holla at ya girl, flaskapps are simple'

if __name__=="__main__":
	app.run(port="5900",host="0.0.0.0")
