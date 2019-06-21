from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=['GET'])
def main():
  data = request.form
  data.title = 'main'
  return render_template("main.html", result = data)



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000)
 
