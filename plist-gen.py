import sys
import argparse
import plistlib
from ruamel.yaml import YAML

'''
Reads values from a yaml file and writes them to a plist.

psobolik Nov 2019
'''

parser = argparse.ArgumentParser(description='Generate plist file from yaml '
                                             'file')
parser.add_argument('yaml', metavar='FILE', help='yaml input file')

args = parser.parse_args()

yaml = YAML()

infile = open(args.yaml, 'r')
settings_raw = yaml.load(infile)

settings = {}
for key in settings_raw:
    if settings_raw[key] is not None:
        settings[key] = settings_raw[key]

plist_string = plistlib.dumps(settings, sort_keys=False)
print(plist_string.decode("utf-8"))
