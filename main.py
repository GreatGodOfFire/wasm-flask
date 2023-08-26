from flask import Flask, render_template, Response, send_from_directory
import os.path

app = Flask(__name__)

@app.route("/")
def hello_world():
   return render_template('index.html')

@app.route('/wasm.js')
def wasm_js():
    return send_from_directory("wasm/pkg/", "wasm.js", mimetype="application/javascript")

@app.route('/wasm_bg.wasm')
def wasm():
    return send_from_directory("wasm/pkg/", "wasm_bg.wasm", mimetype="application/webassembly")

if __name__ == '__main__':
   app.run()
