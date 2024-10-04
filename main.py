from flask import Flask, render_template
import pandas as pd

app = Flask("__name__")

stations = pd.read_csv('data/stations.txt', skiprows=17)
station_data = stations[['STAID', 'STANAME                                 ']]

@app.route('/')
def home():
    return render_template('home.html', data=station_data.to_html())

@app.route("/api/v1/<station>/<date>")
def getData(station, date):
    #what zfill does is if u give it 1001 it gives a 6 digit string i.e., 001001. If you give it 99 it gives you 000099, which is the format of files
    filename = 'data/TG_STAID' + str(station).zfill(6) + '.txt'
    df = pd.read_csv(filename, skiprows=20, parse_dates=['    DATE'])
    temperature = df.loc[df['    DATE']== date]['   TG'].squeeze()/10
    return {"station": station,
            "date": date,
            "temperature": temperature }

@app.route('/api/v1/<station>')
def all_data(station):
    filename = 'data/TG_STAID' + str(station).zfill(6) + '.txt'
    df = pd.read_csv(filename, skiprows=20, parse_dates=['    DATE'])
    result = df.to_dict(orient='records')
    return result

@app.route('/api/v1/yearly/<station>/<year>')
def get_yearly_data(station, year):
    filename = 'data/TG_STAID' + str(station).zfill(6) + '.txt'
    df = pd.read_csv(filename, skiprows=20)
    df['    DATE'] = df['    DATE'].astype(str)
    result = df[df['    DATE'].str.startswith(str(year))].to_dict(orient='records')
    return result




#If the main file is executed only then run this file.
#In case some other file imports main and just uses it's functions, then __name__!=__main__, thus it won't execute
if(__name__ == "__main__"):
    app.run(debug=True)
