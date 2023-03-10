from datacube_alchemist.worker import Alchemist
import os
from fnmatch import fnmatch

root = './dev/services/alchemist'
pattern = '*.yaml'

for path, subdirs, files in os.walk(root):
    for name in files:
        if fnmatch(name, pattern):
            alchemist = Alchemist(config_file=os.path.join(path, name))
