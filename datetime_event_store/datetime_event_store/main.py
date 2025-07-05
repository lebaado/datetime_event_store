import datetime
import random
from storage import DatetimeEventStore

store = DatetimeEventStore()

# Génère des événements entre 2000 et 2020
start_ts = datetime.datetime(2000, 1, 1).timestamp()
end_ts = datetime.datetime(2020, 1, 1).timestamp()

for i in range(10000):
    dt = datetime.datetime.fromtimestamp(
        random.randint(int(start_ts), int(end_ts)) 
    )
    store.store_event(at=dt, data="Event number %d." % i)

# Récupère et affiche les événements de janvier 2018
for event in store.get_events(
    start=datetime.datetime(year=2018, month=1, day=1),
    end=datetime.datetime(year=2018, month=2, day=1)
):
    print(event)
