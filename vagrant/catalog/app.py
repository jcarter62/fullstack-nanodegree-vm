from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=['GET'])
def main():
  return render_template('main.html')



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000)
 
