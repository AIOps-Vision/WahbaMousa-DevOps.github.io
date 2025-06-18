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

# Apply protection for each branch
for branch in data.get("branches", []):
    branch_name = branch.get("pattern")
    branch_config = branch.get("protection")
    if not branch_name or not branch_config:
        continue

    # Check required keys
    required_keys = ["required_pull_request_reviews", "required_status_checks"]
    for key in required_keys:
        if key not in branch_config:
            print(f"[{branch_name}] Missing required key: {key}")
            continue

    # Build payload
    payload = {
        "enforce_admins": branch_config.get("enforce_admins", True),
        "required_pull_request_reviews": {
            "required_approving_review_count": branch_config["required_pull_request_reviews"].get("required_approving_review_count", 1),
            "dismiss_stale_reviews": branch_config["required_pull_request_reviews"].get("dismiss_stale_reviews", True),
            "require_code_owner_reviews": branch_config["required_pull_request_reviews"].get("require_code_owner_reviews", False)
        },
        "required_status_checks": {
            "strict": branch_config["required_status_checks"].get("strict", True),
            "contexts": branch_config["required_status_checks"].get("contexts", [])
        },
        "restrictions": None,
        "allow_force_pushes": branch_config.get("allow_force_pushes", False),
        "allow_deletions": branch_config.get("allow_deletions", False)
    }

    # Save to temp JSON
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.json') as tmp:
        json.dump(payload, tmp, indent=2)
        tmp_path = tmp.name

    # Apply protection via GitHub CLI
    repo = os.environ.get("GITHUB_REPOSITORY")
    if not repo:
        print("GITHUB_REPOSITORY env var is not set")
        sys.exit(1)

    cmd = [
        "gh", "api", "-X", "PUT",
        f"repos/{repo}/branches/{branch_name}/protection",
        "--input", tmp_path
    ]

    print(f"🔐 Applying protection for branch: {branch_name}")
    try:
        subprocess.run(cmd, check=True)
        print(f"Protection applied successfully for {branch_name}")
    except subprocess.CalledProcessError:
        print(f"Failed to apply protection for {branch_name}")
