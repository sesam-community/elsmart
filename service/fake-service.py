from flask import Flask, request, Response
import logging
import json

app = Flask(__name__)


@app.route('/receiver', methods=['POST'])
def receiver():
    # get entities from request and write each of them to a file

    return_data = {
      "Status": [
        {
          "detail": None,
          "code": "101",
          "detailcode": -1,
          "description": "Update workorder succeded for elsmartorderid: ACA3BE1CEFF2A3E9C1257EE600296D80 ( refnr: HNAO02331)",
          "ExternalID": "",
          "FieldSystemID": "",
          "SystemID": "",
          "ExternalParentID": None
        }
      ],
      "ComStatusCode": "",
      "ComStatusDescription": ""
    }

    # create the response
    return Response(json.dumps(return_data), mimetype='application/json')


if __name__ == '__main__':

    # Set up logging
    format_string = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logger = logging.getLogger('elsmart-workorder-fake-service')

    # Log to stdout
    stdout_handler = logging.StreamHandler()
    stdout_handler.setFormatter(logging.Formatter(format_string))
    logger.addHandler(stdout_handler)

    logger.setLevel(logging.DEBUG)

    app.run(debug=True, host='0.0.0.0', port=5002)
