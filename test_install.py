"""Smoke-check real installations in temporary directories; never touch user skills."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parent
NAMES = sorted(item['name'] for item in json.loads((ROOT / 'sources.json').read_text())['skills'])


def run(dest, *args, ok=True):
    result = subprocess.run([sys.executable, str(ROOT / 'install.py'), '--dest', str(dest), *args],
                            capture_output=True, text=True)
    assert (result.returncode == 0) == ok, result.stdout + result.stderr
    return result.stdout + result.stderr


with tempfile.TemporaryDirectory() as folder:
    temp = Path(folder)
    assert run(temp / 'unused', '--list').splitlines() == NAMES
    run(temp / 'preview', '--dry-run')
    assert not (temp / 'preview').exists(), 'Dry run wrote files'
    run(temp / 'all')
    assert sorted(p.name for p in (temp / 'all').iterdir()) == NAMES
    count = 0
    for name in NAMES:
        source = ROOT / 'skills' / name
        for path in source.rglob('*'):
            installed = temp / 'all' / name / path.relative_to(source)
            if path.is_file():
                assert installed.read_bytes() == path.read_bytes(), installed
                count += 1
    run(temp / 'selected', 'ponytail', 'ponytail')
    assert [p.name for p in (temp / 'selected').iterdir()] == ['ponytail']
    sentinel = temp / 'selected' / 'ponytail' / 'local-edit.txt'
    sentinel.write_text('keep my edits')
    assert 'Already exists' in run(temp / 'selected', 'diagnosing-bugs', 'ponytail', ok=False)
    assert sentinel.read_text() == 'keep my edits'
    assert not (temp / 'selected' / 'diagnosing-bugs').exists(), 'Conflict caused a partial install'
    assert 'Unknown skills' in run(temp / 'invalid', '../escape', ok=False)
    assert not (temp / 'invalid').exists()
    for line in (ROOT / 'checksums.sha256').read_text().splitlines():
        expected, relative = line.split('  ', 1)
        assert hashlib.sha256((ROOT / relative).read_bytes()).hexdigest() == expected, relative
    print(f'PASS: all four skills installed; {count} files compared byte for byte; '
          'selection, duplicates, dry run, conflict protection, invalid names and checksums verified.')
