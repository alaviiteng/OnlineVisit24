from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/page2')
def page2():
    return send_from_directory('.', 'page2.html')

@app.route('/page3')
def page3():
    return send_from_directory('.', 'page3.html')

@app.route('/page4')
def page4():
    return send_from_directory('.', 'page4.html')

@app.route('/submit', methods=['POST'])
def save_data():
    data = request.json['data']
    with open('static/customers.txt', 'a') as file:
        file.write(data + "\n")
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

