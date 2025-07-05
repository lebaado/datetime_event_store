from flask import Flask, request, jsonify
from datetime import datetime
import time

app = Flask(__name__)

class DatetimeEventStore:
    def __init__(self):
        self._store = {}

    def store_event(self, at, data):
        if not isinstance(at, datetime):
            raise ValueError("at must be a datetime object")
        ts = at.timestamp()
        if ts not in self._store:
            self._store[ts] = []
        self._store[ts].append(data)

    def get_events(self, start, end):
        if start > end:
            raise ValueError("start must be before end")
        start_ts = start.timestamp()
        end_ts = end.timestamp()
        result = []
        for ts in sorted(self._store):
            if start_ts <= ts <= end_ts:
                result.extend(self._store[ts])
        return result

store = DatetimeEventStore()

@app.route('/events', methods=['POST'])
def add_event():
    data = request.json
    try:
        at = datetime.fromisoformat(data['at'])
        event = data['event']
        store.store_event(at, event)
        return jsonify({"message": "Event stored successfully."}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/events', methods=['GET'])
def get_events():
    try:
        start_str = request.args.get('start')
        end_str = request.args.get('end')
        start = datetime.fromisoformat(start_str)
        end = datetime.fromisoformat(end_str)
        events = store.get_events(start, end)
        return jsonify(events)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
