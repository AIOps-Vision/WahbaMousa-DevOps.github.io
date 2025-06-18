import os
import yaml
import json
import tempfile
import subprocess
import sys

# Load YAML config
RULESET_FILE = ".github/branch-protection.yml"

try:
    with open(RULESET_FILE, "r") as f:
        data = yaml.safe_load(f)
except Exception as e:
    print(f"Failed to read YAML: {e}")
    sys.exit(1)

# Extract main branch protection
try:
    branch_config = data["branches"][0]["protection"]
except (KeyError, IndexError) as e:
    print(f"Invalid YAML structure: {e}")
    sys.exit(1)

# Ensure required top-level keys are present
required_keys = ["required_pull_request_reviews", "required_status_checks"]
for key in required_keys:
    if key not in branch_config:
        print(f"Missing required key: {key}")
        sys.exit(1)

# Construct full payload
payload = {
    "enforce_admins": branch_config.get("enforce_admins", True),
    "required_pull_request_reviews": {
        "required_approving_review_count": branch_config["required_pull_request_reviews"].get("required_approving_review_count", 1),
        "dismiss_stale_reviews": True,
        "require_code_owner_reviews": False
    },
    "required_status_checks": {
        "strict": True,
        "contexts": branch_config["required_status_checks"].get("contexts", [])
    },
    "restrictions": None,
    "allow_force_pushes": branch_config.get("allow_force_pushes", False),
    "allow_deletions": branch_config.get("allow_deletions", False)
}

# Save to a temporary JSON file
with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.json') as tmp:
    json.dump(payload, tmp, indent=2)
    tmp_path = tmp.name

# Apply with GitHub CLI
repo = os.environ.get("GITHUB_REPOSITORY")
if not repo:
    print("GITHUB_REPOSITORY env var is not set")
    sys.exit(1)

cmd = [
    "gh", "api", "-X", "PUT",
    f"repos/{repo}/branches/main/protection",
    "--input", tmp_path
]

print(f"Applying branch protection from: {RULESET_FILE}")
try:
    subprocess.run(cmd, check=True)
    print("Branch protection applied successfully.")
except subprocess.CalledProcessError as e:
    print("Failed to apply branch protection.")
    sys.exit(e.returncode)
