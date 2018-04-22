from flask import Flask, render_template, request, redirect, jsonify
from subprocess import Popen, PIPE
import sys

app = Flask(__name__)

gkey = "" # add key here for Google SignIn integration

@app.route("/")
def home():
    return render_template('login.html', key = gkey)

@app.route("/main")
def main():
    return render_template('main.html', key = gkey)

@app.route("/editor/<name>")
def editor(name):
    fname = 'demo-'+str(name)+'.html'
    return render_template(fname, key = gkey)

@app.route("/run/c", methods=['POST'])
def runC():
    executeC(request.form["code"], request.form["input"])
    Popen('docker build ./gcc -t gcc/cin:latest', shell=True, stdout=PIPE, stderr=PIPE)
    p = Popen('docker run --rm gcc/cin:latest', shell=True, stdout=PIPE, stderr=PIPE)
    res = (p.communicate()[0].decode(sys.stdout.encoding)).split("--")
    err = (p.communicate()[1].decode(sys.stderr.encoding))
    if(err == ""):
        return res[1].strip()
    return err.strip()

def executeC(codemain, inputmain):
    f0 = open('./gcc/src/main.c', 'r+')
    f0.truncate()
    f0.write(str(codemain))
    f0.close()
    f1 = open('./gcc/src/in.txt', 'r+')
    f1.truncate()
    f1.write(str(inputmain))
    f1.close()

@app.route("/run/java", methods=['POST'])
def runJava():
    executeJava(request.form["code"], request.form["input"])
    Popen('docker build ./java -t java/cin:latest', shell=True, stdout=PIPE, stderr=PIPE)
    p = Popen('docker run --rm java/cin:latest', shell=True, stdout=PIPE, stderr=PIPE)
    res = (p.communicate()[0].decode(sys.stdout.encoding)).split("--")
    res = (p.communicate()[0].decode(sys.stdout.encoding)).split("--")
    err = (p.communicate()[1].decode(sys.stderr.encoding))
    if(err == ""):
        return res[1].strip()
    return err.strip()

def executeJava(codemain, inputmain):
    f0 = open('./java/Main.java', 'r+')
    f0.truncate()
    f0.write(str(codemain))
    f0.close()
    f1 = open('./java/in.txt', 'r+')
    f1.truncate()
    f1.write(str(inputmain))
    f1.close()

@app.route("/run/py", methods=['POST'])
def runPy():
    executePy(request.form["code"], request.form["input"], request.form["require"])
    Popen('docker build ./python3 -t py/cin:latest', shell=True, stdout=PIPE, stderr=PIPE)
    p = Popen('docker run --rm py/cin:latest', shell=True, stdout=PIPE, stderr=PIPE)
    res = (p.communicate()[0].decode(sys.stdout.encoding)).split("--")
    err = (p.communicate()[1].decode(sys.stderr.encoding))
    if(err == ""):
        return res[0].strip()
    return err.strip()

def executePy(codemain, inputmain, require):
    f0 = open('./python3/main.py', 'r+')
    f0.truncate()
    f0.write(str(codemain))
    f0.close()
    f1 = open('./python3/in.txt', 'r+')
    f1.truncate()
    f1.write(str(inputmain))
    f1.close()
    f1 = open('./python3/requirements.txt', 'r+')
    f1.truncate()
    f1.write(str(require))
    f1.close()

@app.route("/error401")
def unauthorized():
    return render_template('error401.html')

if __name__=='__main__':
    app.run(debug=True)