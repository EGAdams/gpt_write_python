import os
import subprocess
from pathlib import Path

import docker
from docker.errors import ImageNotFound

from autogpt.commands.command import command
from autogpt.config import Config
from autogpt.logs import logger

CFG = Config()