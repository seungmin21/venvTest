from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_logs():
    try:
        with open('log.json', 'r', encoding='utf-8') as f:
            logs = f.readlines()
    except FileNotFoundError:
        return jsonify({'error': 'Log file not found'}), 404

    return jsonify({'logs': logs})

if __name__ == '__main__':
    app.run(debug=True)
