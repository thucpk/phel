# __init__.py

from importlib import resources
try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib

# Version of the realpython-reader package
__version__ = "1.0.0"

# Read URL of the Real Python feed from config file
_cfg = tomllib.loads(resources.read_text("phel", "config.toml"))
URL = _cfg["feed"]["url"]
