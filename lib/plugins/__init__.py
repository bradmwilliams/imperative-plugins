from __future__ import print_function

import os

PLUGINS = []

path = 'lib/plugins'

files = os.listdir(path)
for name in files:
    name, extension = os.path.splitext(name)

    if (extension == '.py' and name != '__init__'):
        PLUGINS.append(name)

__all__ = PLUGINS
