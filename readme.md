OrbitScan
> Modular, CLI-based security configuration auditing framework for AWS infrastructure.
![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=flat-square)
![AWS](https://img.shields.io/badge/Cloud-AWS-orange?style=flat-square)
![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
OrbitScan lets you run focused security checks across your AWS environment through a plugin system — add a `.py` file to `plugins/`, and it gets picked up automatically. A real-time TUI dashboard (built with Textual) shows scan results as they come in.
---
Features
Modular plugins — each security check lives in its own `.py` file inside `plugins/`
Auto-discovery — finds your AWS resources (S3, EC2, etc.) before scanning
TUI dashboard — real-time PASS/FAIL view built with Textual
Plugin factory — scaffold new plugins from your rules database via `factory.py`
---
Prerequisites
Python 3.9+
AWS CLI configured (`aws configure`)
---
Installation
```bash
git clone https://github.com/TheSudoLab/orbitscan.git
cd orbitscan
pip install -r requirements.txt
```
---
Usage
```bash
python main.py
```
This opens the TUI dashboard. Press `s` to trigger a full audit. Results update in real-time with a `PASS` or `FAIL` for each discovered resource.
---
Project Structure
```
orbitscan/
├── core/           # Discovery engine and shared utilities
├── plugins/        # Security check modules — add yours here
├── main.py         # Entry point
└── factory.py      # Generates new plugin templates
```
---
Writing a Plugin
Create a file in `plugins/` and follow this structure:
```python
# plugins/s3_encryption_check.py

PLUGIN_NAME   = "s3_encryption_check"
RESOURCE_TYPE = "s3"
SEVERITY      = "HIGH"
DESCRIPTION   = "Checks that all S3 buckets have server-side encryption enabled."

def run(resource: dict) -> dict:
    bucket_name = resource["name"]
    encryption_enabled = check_bucket_encryption(bucket_name)

    return {
        "status": "PASS" if encryption_enabled else "FAIL",
        "message": f"Bucket '{bucket_name}' — SSE {'enabled' if encryption_enabled else 'not configured'}.",
    }
```
OrbitScan automatically loads any plugin it finds in the `plugins/` directory on startup.
To scaffold a plugin from the factory:
```bash
python factory.py --rule s3_encryption --output plugins/
```
---
Contributing
OrbitScan is in active development and we'd love your help. The easiest way to contribute is by writing new plugins for AWS services that aren't covered yet.
Good first contributions:
New plugins for IAM, RDS, CloudTrail, Lambda, VPC
Improving the discovery engine to support more resource types
Adding tests for existing plugins
Documentation and examples
To get started:
Fork the repo
Create a branch (`git checkout -b plugin/iam-mfa-check`)
Write your plugin following the template above
Open a pull request with a short description of what it checks
If you're not sure where to start, open an issue and we'll point you in the right direction.
---
License
MIT — see LICENSE for details.
---
Developed by TheSudoLab.
