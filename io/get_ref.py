import os, json

config_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'configuration.json')
with open(config_path, 'r') as f:
    config_obj = json.load(f)

def get_ref(ref):
    try:
        return config_obj[ref]
    except KeyError as e:
        print('ERROR: Reference {} not recognized!'.format(ref))
        raise
