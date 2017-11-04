import json
from src.definitions import basedir


def get_rows():
  with open('{}/rows.json'.format(basedir)) as f:
    return json.load(f)