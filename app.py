from flask import Flask, render_template
import requests
import json

app = Flask(__name__)


@app.route('/' )
def hello():
    return '<h1>Hello, World!</h1>'

@app.route('/graph')
def graph():
    res = requests.get("https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m")
    response = json.loads(res.text)

    return render_template('graph.html'
                           ,osax=response['hourly']['time']
                           , osay=response["hourly"]["temperature_2m"])

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
