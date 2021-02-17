import json

from Config import Global

js = {'o': {'max': 0.5, 'min': 0.5}, 's': {'max': 0.5, 'min': 0.5}}
Global.r.set('v', json.dumps(js))

Global.r.save()
