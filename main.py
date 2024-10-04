from flask import Flask, render_template
import pandas as pd

app = Flask("__name__")

@app.route('/')
def home():
    return render_template('home.html')

@app.route("/api/v1/<station>/<date>")
def getData(station, date):
    #what zfill does is if u give it 1001 it gives a 6 digit string i.e., 001001. If you give it 99 it gives you 000099, which is the format of files
    filename = 'data/TG_STAID' + str(station).zfill(6) + '.txt'
    df = pd.read_csv(filename, skiprows=20, parse_dates=['    DATE'])
    temperature = df.loc[df['    DATE']== date]['   TG'].squeeze()/10
    return {"station": station,
            "date": date,
            "temperature": temperature }

#If the main file is executed only then run this file.
#In case some other file imports main and just uses it's functions, then __name__!=__main__, thus it won't execute
if(__name__ == "__main__"):
    app.run(debug=True)
