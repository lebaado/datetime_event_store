import datetime

class DatetimeEventStore:
    def __init__(self):
        self._store = {}

    def store_event(self, at: datetime.datetime, data):

        timestamp = at.timestamp()

        if timestamp not in self._store:
            self._store[timestamp] = []

        self._store[timestamp].append(data)

    def get_events(self, start: datetime.datetime, end: datetime.datetime):
        if start > end:
                raise ValueError("`start` doit être inférieur à `end`")
        
        start_ts = start.timestamp()
        end_ts = end.timestamp()

        result = []

        for unts in sorted(self._store):
                if start_ts <= unts <= end_ts:
                    result.extend(self._store[unts])
        return result