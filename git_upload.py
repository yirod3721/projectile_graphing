import os
import subprocess

# 1️⃣ Ask for GitHub repository URL
repo_url = input("Enter your GitHub repository HTTPS URL (e.g., https://github.com/username/repo.git): ").strip()

# 2️⃣ Optional: commit message
commit_msg = input("Enter initial commit message (default: 'Initial commit'): ").strip()
if not commit_msg:
    commit_msg = "Initial commit"

# 3️⃣ Create a .gitignore for Python projects
gitignore_content = """
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# VS Code settings
.vscode/

# Distribution / packaging
build/
dist/
*.egg-info/
.eggs/

# Environment
.env
venv/
"""

with open(".gitignore", "w") as f:
    f.write(gitignore_content.strip())
print("✅ .gitignore created.")

# 4️⃣ Initialize Git repo
subprocess.run(["git", "init"])

# 5️⃣ Add all files
subprocess.run(["git", "add", "."])

# 6️⃣ Commit
subprocess.run(["git", "commit", "-m", commit_msg])

# 7️⃣ Set branch to main
subprocess.run(["git", "branch", "-M", "main"])

# 8️⃣ Add remote
subprocess.run(["git", "remote", "add", "origin", repo_url])

# 9️⃣ Push to GitHub
subprocess.run(["git", "push", "-u", "origin", "main"])

print("🚀 Project uploaded to GitHub successfully!")
