"""Entrypoint for the workforce monitoring scaffold.
This starter script demonstrates configuration loading and safe imports of modules.
"""
import time
import yaml
from pathlib import Path

ROOT = Path(__file__).parent


def load_config():
    cfg_file = ROOT / 'config' / 'system_config.yaml'
    if not cfg_file.exists():
        return {}
    with open(cfg_file, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def main():
    cfg = load_config()
    print('Loaded config keys:', list(cfg.keys()) if isinstance(cfg, dict) else cfg)
    print('Modules available:')
    # Try importing optional modules
    try:
        from face import face_recognizer
        print(' - face_recognizer OK')
    except Exception:
        print(' - face_recognizer missing or failed to import')
    try:
        from gesture import pose_detector
        print(' - pose_detector OK')
    except Exception:
        print(' - pose_detector missing or failed to import')
    try:
        from object_detection import object_detector
        print(' - object_detector OK')
    except Exception:
        print(' - object_detector missing or failed to import')

    print('Scaffold ready. Exiting in 1s...')
    time.sleep(1)


if __name__ == '__main__':
    main()
