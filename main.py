from flask import Flask, jsonify, request
from routes.eventRoutes import event_api
from routes.userRoutes import user_api

app = Flask(__name__)

app.register_blueprint(event_api)
app.register_blueprint(user_api)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)