import json

in_path = r'tweets.json'

with open(in_path, 'r') as inF:
    for line in inF:
        line = line.strip()
        data = json.loads(line)

        date = data['created_at']
        text = data['text']

        print(date, text)
        print()