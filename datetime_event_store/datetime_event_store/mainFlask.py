import requests

# Ajouter un événement
response = requests.post("http://127.0.0.1:5000/events", json={
    "at": "2025-07-05T14:30:00",
    "event": "Maintenance du serveur"
})
print("POST:", response.status_code, response.json())


