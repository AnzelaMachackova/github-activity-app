from flask import Flask, jsonify
from github_events import calculate_average_time  # Make sure to have this function accessible

app = Flask(__name__)

@app.route('/api/stats', methods=['GET'])
def get_stats():
    stats = calculate_average_time()
    return jsonify(stats)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)