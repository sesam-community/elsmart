from flask import Flask, request, Response
import requests
import os
import logging
import sys

app = Flask(__name__)

API_ENDPOINT = os.environ.get('API_ENDPOINT')
USER = os.environ.get('USERNAME')
PSW = os.environ.get('PASSWORD')

def is_2xx_status(response):
    return 200 <= response.status_code < 300


@app.route('/receiver', methods=['POST'])
def receiver():
    # get entities from request and write each of them to a file
    headers = {"content-type": "application/json"}
    if User != None and PSW != None:
        r = requests.post(API_ENDPOINT, data=request.data, headers=headers, auth=(USER, PSW))
    else:
        r = requests.post(API_ENDPOINT, data=request.data, headers=headers)

    if not is_2xx_status(r):
        return Response("The endpoint '%s' returned a non-OK error code '%s' (%s)! "
                        "The returned response was:\n%s" % (API_ENDPOINT, r.status_code, r.reason, r.text),
                        mimetype='text/plain', status=r.status_code)

    # Even if the status code was 200 we need to check the JSON body to see if it really is ok

    try:
        return_data = r.json()
        if not return_data:
            raise AssertionError
    except:
        return Response("The endpoint '%s' returned a blank or non-JSON response! "
                        "The returned response was:\n%s" % (API_ENDPOINT, r.text),
                        mimetype='text/plain', status=400)

    if "Status" not in return_data:
        return Response("The endpoint '%s' returned a unexpected result in the JSON response! Expected key "
                        "'Status' not found. The returned response was:\n%s" % (API_ENDPOINT, r.text),
                        mimetype='text/plain', status=400)

    states = return_data["Status"]

    if not isinstance(states, list):
        states = [states]

    for return_code in states:
        if "code" not in return_code:
            return Response("The endpoint '%s' returned a unexpected result in the JSON response! Expected key "
                            "'code' missing in the 'Status' key of the response."
                            "The returned response was:\n%s" % (API_ENDPOINT, r.text),
                            mimetype='text/plain', status=400)

        status_code = return_code["code"]
        if status_code not in ["100"]:
            return Response("The endpoint '%s' returned a non-OK error code '%s'! The returned response "
                            "was:\n%s" % (API_ENDPOINT, status_code, r.text),
                            mimetype='text/plain', status=400)

    # create the response
    return Response(r.text, mimetype='application/json')


if __name__ == '__main__':

    # Set up logging
    format_string = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logger = logging.getLogger('elsmart-workorder-microservice')

    # Log to stdout
    stdout_handler = logging.StreamHandler()
    stdout_handler.setFormatter(logging.Formatter(format_string))
    logger.addHandler(stdout_handler)

    logger.setLevel(logging.DEBUG)

    if not API_ENDPOINT:
        logger.error("API endpoint has not been configured!")
        sys.exit(1)

    app.run(debug=True, host='0.0.0.0', port=5001)
