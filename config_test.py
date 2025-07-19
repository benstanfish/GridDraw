from configparser import *

config = ConfigParser()
# config['DEFAULT'] = {'ServerAliveInterval': '45',
#                      'Compression': 'yes',
#                      'CompressionLevel': '9'}
# config['forge.example'] = {}
# config['forge.example']['User'] = 'hg'
# config['topsecret.server.example'] = {}
# topsecret = config['topsecret.server.example']
# topsecret['Port'] = '50022'     # mutates the parser
# topsecret['ForwardX11'] = 'no'  # same here
# config['DEFAULT']['ForwardX11'] = 'yes'
# with open('example.ini', 'w') as configfile:
#   config.write(configfile)

config.read('example.ini')
# for key in config['seismic.high']:
#     print(key)

print(config['seismic.high']['ground_fault'])

config['seismic.high']['ground_fault'] = 'maybe'
print(config['seismic.high']['ground_fault'])

with open('example.ini', 'w') as configfile:
  config.write(configfile)