from flask import Flask, jsonify, request
from flask import Blueprint

import controllers.eventControler as eventControler

event_api = Blueprint("event_api",__name__)

@event_api.route("/events", methods = ['GET'])
def getAllEvents():
    parameters = request.args
    events = eventControler.getAllEvents()
    for event in events:
        event.col_ekitaldi_data = event.col_ekitaldi_data.strftime('%Y/%m/%d')
        event.col_ekitaldi_ordua = event.col_ekitaldi_ordua.strftime('%H:%M')    
    return jsonify(events)


@event_api.route("/event", methods = ['GET'])
def getEvent():
    parameters = request.args
    event_id = parameters['eventID']
    events = eventControler.getEvent(event_id=event_id)
    events.col_ekitaldi_data = events.col_ekitaldi_data.strftime('%Y/%m/%d')
    events.col_ekitaldi_ordua = events.col_ekitaldi_ordua.strftime('%H:%M')
    return jsonify(events)

@event_api.route("/event", methods = ['POST'])
def addEvent():
    parameters = request.args
    name = parameters['name']
    location = parameters['location']
    date = parameters['date']
    time = parameters['time']
    result = eventControler.addEvent(name=name,
                                     location=location,
                                     date=date,
                                     time=time)
    return jsonify({'result':result})
