#!/usr/bin/env python3
"""Install this repository's skill directories using only Python's standard library."""
import argparse
import os
from pathlib import Path
import shutil


ROOT = Path(__file__).resolve().parent


def main(argv=None):
    available = sorted(p.name for p in (ROOT / 'skills').iterdir()
                       if p.is_dir() and (p / 'SKILL.md').is_file())
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('skills', nargs='*', help='Names to install; defaults to all four')
    parser.add_argument('--list', action='store_true', help='List available skill names')
    parser.add_argument('--dry-run', action='store_true', help='Check and show the copy plan')
    parser.add_argument('--dest', type=Path, help='Override the destination skills directory')
    args = parser.parse_args(argv)
    if args.list:
        print('\n'.join(available))
        return
    names = list(dict.fromkeys(args.skills or available))
    unknown = set(names) - set(available)
    if unknown:
        parser.error('Unknown skills: ' + ', '.join(sorted(unknown)))
    codex_dir = Path(os.environ.get('CODEX_HOME') or Path.home() / '.codex')
    dest = (args.dest or codex_dir / 'skills').expanduser().resolve()
    for name in names:
        source = ROOT / 'skills' / name
        target = dest / name
        if target.exists() or target.is_symlink():
            parser.error(f'Already exists: {target}. Back it up or choose another --dest.')
        if target.is_relative_to(source.resolve()):
            parser.error(f'Destination cannot be inside the source skill: {target}')
    for name in names:
        target = dest / name
        print(f'{"Would install" if args.dry_run else "Installing"} {name} -> {target}')
        if not args.dry_run:
            shutil.copytree(ROOT / 'skills' / name, target)
    if not args.dry_run:
        print('Done. Start a new Codex conversation to load the installed skills.')


if __name__ == '__main__':
    try:
        main()
    except OSError as error:
        raise SystemExit(str(error)) from error
