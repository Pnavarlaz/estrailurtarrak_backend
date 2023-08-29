from flask import Flask, jsonify, request
from flask import Blueprint

import controllers.userControler as userControler
import controllers.eventControler as eventControler
user_api = Blueprint("user_api",__name__)

@user_api.route("/user", methods = ['GET'])
def getUser():
    parameters = request.args
    userID = parameters['userID']
    user = userControler.getUser(userID=userID)
    return jsonify(user)


@user_api.route("/user", methods = ['POST'])
def putUser():
    parameters = request.args
    name = parameters['name']
    surname = parameters['surname']
    result = userControler.addUser(name=name,surname=surname)
    return jsonify({'result': result})

@user_api.route("/eventuser", methods = ['GET'])
def getEventUsers():
    parameters = request.args
    eventID = parameters['eventID']
    participants, observers = eventControler.getEventParticipants(event_id=eventID)
    return jsonify({'participants' : participants,'observers': observers})

@user_api.route("/eventuser" , methods = ['POST'])
def addUserToEvent():
    parameters = request.args
    eventID = parameters['eventID']
    userID = parameters['userID']
    participationType = parameters['participationType']
    result = eventControler.putEventParticipant(event_id=eventID,
                                                user_id=userID,
                                                participation_type=participationType)
    return jsonify({'result': result})