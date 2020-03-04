from flask import Flask, render_template, request, Response
import fitbit
import gather_keys_oauth2 as Oauth2
import datetime
import json

CLIENT_ID = "22BGK4"
CLIENT_SECRET = "d36ea1aa94b45cf71782776f05c08e91"
# app = Flask(__name__)
server = Oauth2.OAuth2Server(CLIENT_ID, CLIENT_SECRET)
server.browser_authorize()
ACCESS_TOKEN = str(server.fitbit.client.session.token['access_token'])
REFRESH_TOKEN = str(server.fitbit.client.session.token['refresh_token'])
fitbit = fitbit.Fitbit(CLIENT_ID, CLIENT_SECRET, oauth2=True, access_token=ACCESS_TOKEN, refresh_token=REFRESH_TOKEN)

# print(datetime.datetime.now())
# print(datetime.datetime.now().year)
# print(datetime.datetime.now().month)

@app.route('/sleep', methods=['GET'])
def returnSleepData():
    day = request.args.get('subject', 'My Default')
    return getSleepPattern(day)


# if __name__ == '__main__':
#     app.run(port=3001, debug=True, host='0.0.0.0')

# input month:day:year
def getSleepPattern(day):
    dateOfSleep = datetime.datetime.strptime(day, '%m:%d:%Y')
    sleep = fitbit.get_sleep(dateOfSleep)
    return(
        json.dumps(sleep)
    )

print(getSleepPattern("03:04:2020"))
