from flask import Flask 








app = Flask(__name__)



@app.route('/') 
def hello():
    return 'Hello! this is my PT2 project'




if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=80)