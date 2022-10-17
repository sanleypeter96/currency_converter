from flask import Flask,render_template 

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('./index.html')\

@app.route("/dispaly_page")
def index():
    data = get_Data_db()

    return render_template('./dasboard.html',args =data)


@app.route("")
def upload_


if __name__ == '__main__':
   app.run()