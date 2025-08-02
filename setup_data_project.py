import os
import sys
import subprocess
from pathlib import Path

# === Usage Check ===
if len(sys.argv) < 2 or len(sys.argv) > 3:
    print("❌ Usage: python setup_data_project.py <github_repo_url> [optional: target_directory]")
    sys.exit(1)

github_url = sys.argv[1]
project_name = github_url.rstrip('/').split('/')[-1].replace('.git', '')

# === Determine Target Directory ===
if len(sys.argv) == 3:
    target_dir = os.path.abspath(sys.argv[2])
else:
    # Use the directory where this script is located
    target_dir = os.path.dirname(os.path.abspath(__file__))

# === Navigate to the parent folder ===
print(f"📂 Switching to parent folder: {target_dir}")
os.makedirs(target_dir, exist_ok=True)
os.chdir(target_dir)

# === Step 1: Clone GitHub repo ===
print(f"📥 Cloning {github_url} into {target_dir}")
subprocess.run(["git", "clone", github_url])

# === Step 2: Change into the project folder ===
os.chdir(project_name)

# === Step 3: Create folders and files ===
print("📁 Creating folder structure and initial files...")
for folder in ["data", "notebooks", "visuals", "outputs"]:
    os.makedirs(folder, exist_ok=True)

Path("README.md").touch()
Path("requirements.txt").touch()

# === Step 4: Create virtual environment ===
print("🐍 Setting up virtual environment...")
subprocess.run([sys.executable, "-m", "venv", "venv"])

# === Step 5: Install dependencies ===
print("📦 Installing standard Python packages...")
pip_exe = os.path.join("venv", "Scripts", "pip")
subprocess.run([pip_exe, "install", "--upgrade", "pip"])
subprocess.run([pip_exe, "install", "pandas", "numpy", "matplotlib", "seaborn", "scikit-learn", "jupyter"])
with open("requirements.txt", "w") as f:
    subprocess.run([pip_exe, "freeze"], stdout=f)

# === Step 6: Commit to Git ===
print("🗂 Committing initial project structure...")
subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", "Initial project setup"])
subprocess.run(["git", "push", "origin", "main"])

# === Done ===
print(f"\n✅ Project '{project_name}' created at {os.path.join(target_dir, project_name)}")
print("💡 To get started:")
print(f"   cd \"{os.path.join(target_dir, project_name)}\"")
print("   venv\\Scripts\\activate")
print("   jupyter notebook")
