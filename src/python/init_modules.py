import os
from path import SITE_PKG_PATH, PYTHON_SOURCE_DIR



#Module registry
MODULE_REG = [
    os.path.join(SITE_PKG_PATH, PYTHON_SOURCE_DIR),
    os.path.join(SITE_PKG_PATH, PYTHON_SOURCE_DIR, "components"),
    os.path.join(SITE_PKG_PATH, PYTHON_SOURCE_DIR, "tools"),
    os.path.join(SITE_PKG_PATH, PYTHON_SOURCE_DIR, "utils"),
]

def init_modules():
    pth_file = SITE_PKG_PATH + os.path.sep + "sra.pth"
    with open(pth_file, "w") as f:
        for module in MODULE_REG:
            f.write(module + "\n")