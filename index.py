from flask import Flask, request, Response
from plivo import plivoxml

app = Flask(__name__)

@app.route('/voice.xml', methods=['GET'])
def answer_call():
    # Set the content type of the response to 'text/xml'
    response = Response(content_type='text/xml')

    # Generate the XML response that Plivo will use to handle the call
    response_data = plivoxml.Response()
    response_data.addSpeak("Hello, this is a message from Plivo. Thank you for using our service. Goodbye!")
    response_data.addHangup()

    # Set the XML response as the content of the Flask response
    response.data = str(response_data)

    # Return the Flask response
    return response

if __name__ == '__main__':
    app.run(debug=True)
