from horizon_py import DeepHorizon

dh_client = DeepHorizon()

features = {
  'some-feature': 'some-val'
}

resp = dh_client.predict(features)

if resp.get('ok'):
  prediction = resp['prediction']
  print('Got Prediction: {}'.format(prediction))
else:
  err = resp['error']
  print('Prediction Error: {}'.format(err))