from datacube_alchemist.worker import Alchemist
import os
from fnmatch import fnmatch

alchemist_service_paths = [
    './dev/services/alchemist',
    './prod/services/alchemist'
]

alchemist_config_file_extensions = [
    '*.yaml',
    '*.yml'
]
for alchemist_path in alchemist_service_paths:
    for path, subdirs, files in os.walk(alchemist_path):
        for name in files:
            if any(fnmatch(name, file_extension) for \
                   file_extension in alchemist_config_file_extensions):
                alchemist = Alchemist(config_file=os.path.join(path, name))
