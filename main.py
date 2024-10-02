from flask import Flask, render_template

app = Flask("__name__")

@app.route('/')
def home():
    return render_template('home.html')

@app.route("/api/v1/<station>/<date>")
def about(station, date):
    temperature = 23
    return {"station": station,
            "date": date,
            "temperature": temperature }

#If the main file is executed only then run this file.
#In case some other file imports main and just uses it's functions, then __name__!=__main__, thus it won't execute
if(__name__ == "__main__"):
    app.run(debug=True)
