from src import formatter
from edge_ai import EdgeAI

# Instantiate EdgeAI Client
edge_ai_client = EdgeAI()

# Get all rows of CSV as dict
rows = formatter.get_rows()

for row in rows:
  # Fetch prediction from API
  resp = edge_ai_client.predict(row)

  # Extract price prediction from response
  prediction = resp.get('prediction')

  print '{} --> {}:   ${:,.2f}'.format(row.get('ORIG'), row.get('DEST'), prediction)