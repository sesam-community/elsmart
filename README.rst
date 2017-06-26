==============================
Elsmart workorder microservice
==============================

A python micro service template for receiving a JSON entity stream from a Sesam service instance and forwarding it
to a Elsmart workorder endpoint. The return JSON payload is then inspected to generate proper HTTP error codes in case
something has gone wrong.

::

  $ python3 service/datasink-service.py
   * Running on http://0.0.0.0:5001/ (Press CTRL+C to quit)
   * Restarting with stat
   * Debugger is active!
   * Debugger pin code: 260-787-156

The service listens on port 5001.

JSON entities can be posted to 'http://localhost:5001/receiver'.
