from flask import Flask

api = Flask(__name__)

@api.route('/profile')
def my_profile():
    response_body = {
        "name": "Nagato",
        "about" :"Hello! I'm a full stack developer that loves python and javascript"
    }
    return response_body

import requests
endpoint = "https://api.assemblyai.com/v2/transcript"
json = { "audio_url": "https://bit.ly/3yxKEIY" }
headers = {
    "authorization": "0c4f094dbc8b4cbcb572420ce8d654a8",
}
response = requests.post(endpoint, json=json, headers=headers)
print(response.json())


# from flask_app.controllers import users
# from flask_app import api

# if __name__=='__main__':
#   api.run(debug=True)