# OrbitScan

OrbitScan is a modular, high-performance, CLI-based security configuration auditing framework designed for cloud infrastructure. Inspired by modular recon frameworks, it allows you to dynamically load plugins to perform security checks across your AWS environment.

## Features
- **Modular Architecture:** Add new security checks by simply dropping a `.py` file into the `plugins/` directory.
- **Dynamic Discovery:** Automatically discovers your cloud resources (S3, EC2, etc.) before scanning.
- **TUI Dashboard:** A clean, interactive terminal interface (built with Textual) to monitor scans in real-time.
- **Automated Reporting:** Uses a plug-and-play plugin system to generate status reports.

## Prerequisites
- Python 3.9+
- AWS CLI configured on your machine (`aws configure`)

## Installation
1. Clone this repository:
   ```bash
   git clone [https://github.com/your-repo/orbitscan.git](https://github.com/your-repo/orbitscan.git)
   cd OrbitScan

2. Install required dependency
   ```bash
   pip install -r requirements.txt
