import os
import site
from pathlib import Path


PROJECT_DIR = Path(__file__).resolve().parent.parent.parent
PYTHON_SOURCE_DIR = os.path.join(PROJECT_DIR, "src", "python")
HTML_ASSET_DIR = os.path.join(PROJECT_DIR, "src", "templates")
SITE_PKG_PATH = site.getsitepackages()[0]