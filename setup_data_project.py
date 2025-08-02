import os
import sys
import subprocess
from pathlib import Path

# === CONFIG: Your preferred parent project folder ===
DEFAULT_PARENT_DIR = r"C:\Users\gabri\Documents\Project\Data analytics"

# === Argument check ===
if len(sys.argv) != 2:
    print("❌ Usage: python setup_data_project.py <github_repo_url>")
    sys.exit(1)

github_url = sys.argv[1]
project_name = github_url.rstrip('/').split('/')[-1].replace('.git', '')

# === Navigate to your central Data Projects folder ===
print(f"📂 Switching to parent folder: {DEFAULT_PARENT_DIR}")
os.chdir(DEFAULT_PARENT_DIR)

# === Step 1: Clone GitHub repo ===
print(f"📥 Cloning {github_url} into {DEFAULT_PARENT_DIR}")
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
subprocess.run(["venv\\Scripts\\pip", "install", "--upgrade", "pip"])
subprocess.run(["venv\\Scripts\\pip", "install", "pandas", "numpy", "matplotlib", "seaborn", "scikit-learn", "jupyter"])
subprocess.run(["venv\\Scripts\\pip", "freeze"], stdout=open("requirements.txt", "w"))

# === Step 6: Commit to Git ===
print("🗂 Committing initial project structure...")
subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", "Initial project setup"])
subprocess.run(["git", "push", "origin", "main"])

# === Done ===
print(f"\n✅ Project '{project_name}' created at {DEFAULT_PARENT_DIR}\\{project_name}")
print("💡 To get started:")
print(f"   cd \"{DEFAULT_PARENT_DIR}\\{project_name}\"")
print("   venv\\Scripts\\activate")
print("   jupyter notebook")
