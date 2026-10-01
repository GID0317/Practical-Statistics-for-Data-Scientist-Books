"""Execute notebooks from a fresh kernel and save outputs; stop on any error."""
import argparse
import hashlib
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT / '.cache'
os.environ['IPYTHONDIR'] = str(CACHE / 'ipython')
os.environ['JUPYTER_CONFIG_DIR'] = str(CACHE / 'jupyter-config')
os.environ['JUPYTER_RUNTIME_DIR'] = str(CACHE / 'jupyter-runtime')
os.environ['MPLCONFIGDIR'] = str(CACHE / 'matplotlib')

import nbformat
from jupyter_client import KernelManager
from jupyter_client.kernelspec import KernelSpecManager
from nbclient import NotebookClient


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--chapter', type=int, choices=range(1, 5))
    args = parser.parse_args()
    sources = json.loads((ROOT / 'data/SOURCES.json').read_text(encoding='utf-8'))
    for item in sources['files']:
        digest = hashlib.sha256((ROOT / 'data' / item['name']).read_bytes()).hexdigest()
        if digest != item['sha256']:
            raise ValueError(f"Dataset checksum mismatch: {item['name']}")
    print('Dataset checksums verified.', flush=True)

    kernel_dir = CACHE / 'kernels' / 'matpil'
    kernel_dir.mkdir(parents=True, exist_ok=True)
    (kernel_dir / 'kernel.json').write_text(json.dumps({
        'argv': [sys.executable, '-m', 'ipykernel_launcher', '-f', '{connection_file}'],
        'display_name': 'Matpil project Python', 'language': 'python',
    }), encoding='utf-8')
    pattern = f'chapter_{args.chapter:02d}_*.ipynb' if args.chapter else 'chapter_*.ipynb'
    for path in sorted((ROOT / 'notebooks').glob(pattern)):
        print(f'Executing {path.name}', flush=True)
        notebook = nbformat.read(path, as_version=4)
        manager = KernelManager(kernel_name='matpil', kernel_spec_manager=KernelSpecManager(
            kernel_dirs=[str(kernel_dir.parent)]))
        client = NotebookClient(notebook, km=manager, timeout=600,
                                resources={'metadata': {'path': str(ROOT)}},
                                allow_errors=False)
        # Passing an explicit manager requires explicit kernel cleanup.
        try:
            client.execute()
        finally:
            if manager.has_kernel:
                manager.shutdown_kernel(now=True)
        nbformat.validate(notebook)
        errors = [o for c in notebook.cells if c.cell_type == 'code'
                  for o in c.outputs if o.output_type == 'error']
        if errors:
            raise RuntimeError(errors)
        nbformat.write(notebook, path)
        codes = [c for c in notebook.cells if c.cell_type == 'code']
        figures = sum('image/png' in o.get('data', {}) for c in codes for o in c.outputs)
        print(f'PASS: {len(codes)} code cells; {figures} figures; no errors.', flush=True)


if __name__ == '__main__':
    main()
