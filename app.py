from bs4 import BeautifulSoup
from flask import Flask, jsonify, Response, request
import requests
import json
from routes.data import get_data
from routes.weather import get_weather,get_weather_house

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, Flask!!'

@app.route('/name')
def hello1():
    return 'Hello, 곰돌이사육사!!'


app.add_url_rule('/api/data', 'get_data', get_data, methods=['GET'])
app.add_url_rule('/api/weather', 'get_weather', get_weather, methods=['GET'])
app.add_url_rule('/api/weather-house', 'get_weather_house', get_weather_house, methods=['GET'])





# GET 요청 시 쿼리파라미터 사용하기
@app.route('/api/query', methods=['GET'])
def get_query():
    output = ""
    item_type = request.args.get('type', default=None, type=None)
    item_color = request.args.get('color', default=None, type=None)
    output += f"<h1>{item_type}</h1>"
    output += f"<h1>{item_color}</h1>"
    return output

# 경로 변수 사용하기
@app.route('/api/item/<item_id>', methods=['GET'])
def get_path_item(item_id):
    output = ""
    output += f"<h1>{item_id}</h1>"
    return output

# POST 방식 사용
@app.route('/api/register', methods=['POST'])
def post_register():
    data = request.get_json()
    username = data.get('username', None)
    password = data.get('password', None)
    return jsonify(data)


if __name__ == '__main__':
    app.run()
