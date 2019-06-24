from datetime import datetime
from flask import Flask, send_from_directory, redirect
import requests, json

app = Flask(__name__)

@app.route("/style.css")
def css():
    return send_from_directory(filename="style.css", directory=".")

@app.route("/main.js")
def js():
    return send_from_directory(filename="main.js", directory=".")

def pict(name):
    return "http://openweathermap.org/img/w/" + name + ".png"


@app.route("/Wheather")
def Wheather():
    score()
    return send_from_directory(filename="index.html", directory=".")

@app.route("/Wheather.jpg")
def background_image():
    return send_from_directory(filename="Wheather.jpg", directory=".")

@app.route("/score")
def score():
    url = "https://api.openweathermap.org/data/2.5/forecast?id=501175&appid=e234bd4f6cf90feb586d37ac9c705a79"
    try:
        r = requests.get(url)
        a = r.text
        b = json.loads(a)
        now = datetime.now()
        now_hour = now.hour
        avr_temp = 0
        avr_temp_mas = []
        our_time_score = 0
        final_icons = []
        for i in range(8):
            if now_hour < 24:
                now_hour += 3
                our_time_score += 1
        for i in range(3):
            icons = []
            for j in range(our_time_score, our_time_score + 8):
                ts = b['list'][j]['main']['temp']
                avr_temp += ts
                icons.append(b['list'][j]['weather'][0]['icon'])

            avr_temp /= 8
            avr_temp -= 273.15
            avr_temp = round(avr_temp, 1)
            avr_temp_mas.append(avr_temp)
            our_time_score += 8
            final_icons.append(pict(sorted(icons, reverse=True)[0]))

        return json.dumps({"average": avr_temp_mas,'weather_type':final_icons})
    except:
        return json.dumps({"error": "unknown error"})


if __name__ == '__main__':
    app.run(host="0.0.0.0")
