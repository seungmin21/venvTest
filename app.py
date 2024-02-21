from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def index():
    #반환으로 template에 index.html파일을 지정
    return render_template('index.html')
@app.route('/submit', methods=['POST'])
def submit():
    data = request.form.get('text_bar')

    with open('log.json', 'a', encoding='utf-8') as f:
        f.write(data + '\n')

    return jsonify({'message': 'Data received and logged successfully!'})

if __name__ == '__main__':
    app.run(debug=True)
