#!/usr/bin/python
import json

discovered_data = []
metrics = ["metrics1", "metrics2", "metrics3"]

for metric in metrics:
    discovered_data.append({"{#OTUSMETRICS}": metric})

JSON = json.dumps(discovered_data)

print(JSON)

