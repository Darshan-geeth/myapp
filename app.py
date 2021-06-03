from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def hello():
    #return render_template('home.html')
    return "Flask inside Docker!! and pushed into docker hub repo"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6000))
    app.run(debug=True,host='0.0.0.0',port=port)
