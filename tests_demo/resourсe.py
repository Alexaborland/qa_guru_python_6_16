import os
from pathlib import Path

import tests


def path(file_name):
    dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
    return os.path.join(dir,'tests', 'picture', file_name)