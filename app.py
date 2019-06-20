from flask import Flask
from flask import request
from flask import jsonify
from sense_hat import SenseHat

app = Flask(__name__)
sense = SenseHat()

@app.route('/')
def index():
    return 'Hello world'

@app.route('/api/sense/temp', methods = ['GET'])
def get_temp():
    return jsonify({
        'temp': round(sense.get_temperature(), 1)
    })

@app.route('/api/sense/humidity', methods = ['GET'])
def get_humidity():
    return jsonify({
        'humidity': round(sense.get_humidity(), 1)
    })

@app.route('/api/sense/pressure', methods = ['GET'])
def get_pressure():
    return jsonify({
        'pressure': round(sense.get_pressure(), 1)
    })

@app.route('/api/sense/sendMessage', methods = ['POST'])
def sendMessage():
    if request.is_json:
        content = request.get_json()
        msg = content['message']
        speed = content['speed']
        color = content['color']
        background = content['background']
        colorList = [int(color[1:3], 16), int(color[3:5], 16), int(color[5:7], 16)]
        backColorList = [int(background[1:3], 16), int(background[3:5], 16), int(background[5:7], 16)]

        sense.show_message(msg, speed, colorList, backColorList)

        return jsonify(1)
    else:
        return jsonify(-1)

if __name__ == '__main__':
    app.run(debug=False, host='192.168.2.109')