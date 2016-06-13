import yaml
import os
config_dir = os.getenv('CONFIG_DIR', "config/")

def load_yaml_config():
  with open(config_dir + "config.yaml", 'r') as stream:
    try:
      config = yaml.load(stream)
      return remap_services(config);
    except yaml.YAMLError as exc:
      print(exc)

# reformats config to we can easily look up
# service urls by incoming request route
def remap_services(config):
  config['routes'] = {}
  for s in config['service']:
    for route in s['routes']:
      route['service'] = { 'host': s['host'], 'port': s['port'] }
      config['routes'][route['route']] = route
  return config
