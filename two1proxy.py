# http
from flask import Flask, request, abort
import requests

#import from the 21 Developer Library
from two1.wallet import Wallet
from two1.bitserv.flask import Payment

#helpers
from loader import load_yaml_config

# set up server side wallet
app = Flask(__name__)
wallet = Wallet()
payment = Payment(app, wallet)

# setup routes to handle services
config = load_yaml_config()

# gets fee from service definition
def get_service_fee(request):
  service_path = request.path.replace(config['prefix'],'')
  match = config['routes'].get(service_path, None)
  if match:
    print('fee:', match['price'], 'for', service_path)
    return match['price']
  else:
    print('invalid service route:',service_path)
    abort(404)

@app.route(config['prefix'], methods=['GET', 'POST'], defaults={'path': ''})
@app.route(config['prefix'] +'<path:path>', methods=['GET', 'POST'])
@payment.required(get_service_fee)
def catch_all(path):
    # check if service is handling this request
    match = config['routes'].get(path, None)
    if match:
      # call service
      if request.method == 'GET':
        service_get = 'http://' + match['service']['host'] + ':' + str(match['service']['port']) + '/' + path + '?' + request.query_string.decode("utf-8")
        r = requests.get(service_get)
        return r.text, r.status_code
      elif request.method == "POST":
        r = requests.post(
          'http://' + match['host'] + ':' + match['port'] + '/' + path,
          data = request.data
        );
        return r.text
    else:
      return 404

if __name__ == "__main__":
  app.run(debug=True,host='0.0.0.0')



