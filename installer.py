#!/usr/bin/env python3
import os, sys, shutil, subprocess

# 1) Create and Activate venv
VENV_DIR = 'venv'
if not os.path.isdir(VENV_DIR):
    print("🔧 Creating virtualenv…")
    subprocess.check_call([sys.executable, '-m', 'venv', VENV_DIR])

# 2) Install requirements
pip_exe = os.path.join(VENV_DIR, 'bin', 'pip') if os.name!='nt' else os.path.join(VENV_DIR, 'Scripts', 'pip.exe')
print("📦 Installing dependencies…")
subprocess.check_call([pip_exe, 'install', '--upgrade', 'pip'])
subprocess.check_call([pip_exe, 'install', '-r', 'requirements.txt'])

# 3) Copy default configs if they don't exist
CONFIG_DIR = 'config'
defaults = {
    'blocking_sites.json': '[\n  "youtube.com",\n  "facebook.com",\n  "instagram.com",\n  "reddit.com",\n]\n',
}
os.makedirs(CONFIG_DIR, exist_ok=True)
for fname, content in defaults.items():
    path = os.path.join(CONFIG_DIR, fname)
    if not os.path.exists(path):
        print(f"📝 Creating default {fname}")
        with open(path, 'w') as f:
            f.write(content)

# 4) Final instructions
print("\n✅ Setup complete!")
print("▶️  To start the app:")
print(f"    source {VENV_DIR}/bin/activate  # (or .\\{VENV_DIR}\\Scripts\\activate on Windows)")
print("    python main.py")
print("\n⚠️  Don’t forget to install the mitmproxy CA cert so HTTPS filtering works:")
print("    https://docs.mitmproxy.org/stable/concepts-certificates/")

# chmod +x installer.py