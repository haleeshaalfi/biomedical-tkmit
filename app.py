from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def index():
   return render_template('index.html') 
@app.route("/home")
def home():
    return render_template('home.html')
@app.route("/contact")
def contact():
    return "okay good bye"
if(__name__=="__main__"):
    app.run(debug=True)