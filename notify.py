import requests
def notify():
    requests.post('http://api.mynotifier.app', {
    "apiKey": '48f21a98-f24f-42c7-b984-fae70e8aa3b9',
    "message": "ALERT!!!",
    "description": "possibility of severe flood in your area...",
    "type": "warning", # info, error, warning or success
})
 