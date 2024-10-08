import argparse
import os
from pathlib import Path
from shutil import copy2 as cp

PROJECT_DIR = Path(__file__).resolve().parent.parent.parent

DOTENV_FILES = ['dev.env', 'prod.env', 'db.env']
DOTENV_DIR_TEMPLATES = os.path.join(PROJECT_DIR, '.env', 'templates')
DOTENV_DIR = os.path.join(PROJECT_DIR, '.env')

LOCAL_FILES = ['settings.dev.py', 'settings.unittests.py']
LOCAL_DIR_TEMPLATES = os.path.join(PROJECT_DIR, 'core', 'project', 'settings', 'templates')
LOCAL_DIR = os.path.join(PROJECT_DIR, 'local')


def reset_locals():
    os.makedirs(LOCAL_DIR, exist_ok=True)
    os.makedirs(DOTENV_DIR, exist_ok=True)
    for f in LOCAL_FILES:
        src = os.path.join(LOCAL_DIR_TEMPLATES, f)
        trg = os.path.join(LOCAL_DIR, f)
        cp(src, trg)
    for f in DOTENV_FILES:
        src = os.path.join(DOTENV_DIR_TEMPLATES, f)
        trg = os.path.join(DOTENV_DIR, f)
        cp(src, trg)


def update_locals():
    os.makedirs(LOCAL_DIR, exist_ok=True)
    os.makedirs(DOTENV_DIR, exist_ok=True)
    for f in LOCAL_FILES:
        src = os.path.join(LOCAL_DIR_TEMPLATES, f)
        trg = os.path.join(LOCAL_DIR, f)
        if not os.path.isfile(trg):
            cp(src, trg)
    for f in DOTENV_FILES:
        src = os.path.join(DOTENV_DIR_TEMPLATES, f)
        trg = os.path.join(DOTENV_DIR, f)
        if not os.path.isfile(trg):
            cp(src, trg)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run the boot script.')
    parser.add_argument('--clean', action='store_true', help='Clean locals')
    args = parser.parse_args()
    if args.clean:
        reset_locals()
    else:
        update_locals()
