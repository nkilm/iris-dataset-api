from app import Flask

app = Flask(__name__)

@app.route("/")
def home_page():
    return "<h1>Logistic Regression Model-Iris Dataset</h1>"


if __name__=="__main__":
    app.run(debug=True,port = 5050)
    