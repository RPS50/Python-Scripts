from googlefinance import getQuotes
import json
Print json.dumps(getQuotes('AAPL'), indent=2)
