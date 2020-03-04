from flask import Flask, render_template, request, Response

app = Flask(__name__)

@app.route('/search', methods=['GET'])
def returnData():

if __name__ == '__main__':
    app.run(port=3001, debug=True, host='0.0.0.0')
