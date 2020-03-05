import os
from bottle import Bottle, request, run, route
import sentry_sdk  
from sentry_sdk.integrations.bottle import BottleIntegration  

sentry_sdk.init(
    dsn="https://081b8f4f22a142a380f03e5bf72f9d9b@sentry.io/3720938",
    integrations=[BottleIntegration()]
)   

@route('/success')
def success():
    return    

@route('/fail')
def fail():    
    raise RuntimeError("There is an error!")


if os.environ.get("APP_LOCATION") == "heroku":
    run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        server="gunicorn",
        workers=3,
    )
else:
    run(host="localhost", port=8080, debug=True)
