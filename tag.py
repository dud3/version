import json
from pprint import pprint
import subprocess
import shlex

with open('version.json') as data_file:
    data = json.load(data_file)

version = float(data['version']);
version += 0.001

data['version'] = version;

jdata = json.dumps(data, indent=2);

with open("version.json", "w") as text_file:
    text_file.write(jdata)

subprocess.call(shlex.split('./version.sh ' + str(version)))
