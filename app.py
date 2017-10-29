import os
import json
from horizon_py import DeepHorizon


dh_client = DeepHorizon(
  app_token=os.environ.get('DEEP_HORIZON_TOKEN'),
  app_secret=os.environ.get('DEEP_HORIZON_SECRET')
)

resp = dh_client.predict()
resp_body = json.loads(resp.content)

if resp_body.get('ok'):
  price = resp_body['prediction']
  print price