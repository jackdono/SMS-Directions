from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from directions import getroute

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():

    body = request.values.get('Body', None)

    resp = MessagingResponse()

    # Split addresses on the word 'to' (body => ... to ...)
    start_addr = body.upper().split(' TO ')[0]
    end_addr = body.upper().split(' TO ')[1]

    # Get route
    route = getroute(start_addr, end_addr)

    resp.message(route)

    return str(resp)

if __name__ == '__main__':
    app.run(debug=True)

