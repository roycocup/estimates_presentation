import json
import pprintpp as pp

filename = 'estimation_presentation_transcript.json'
with open(filename, 'r') as f:
    raw_data = f.read()

data = json.loads(raw_data)

for results in data['response']['results']:
    for alternative in results['alternatives']:
        print(alternative['transcript'], "\n\r")

