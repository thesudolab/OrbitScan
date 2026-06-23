import csv
import os

def create_modules(csv_file):
    if not os.path.exists('plugins'):
        os.makedirs('plugins')

    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            filename = f"plugins/{row['service']}_{row['rule_name']}.py"
            content = f'''
import subprocess

class {row['rule_name'].capitalize()}:
    def __init__(self):
        self.cmd = "{row['cli_command']}"
    
    def run(self):
        try:
            # Executes the AWS CLI command directly
            result = subprocess.check_output(self.cmd, shell=True)
            return {{"status": "SUCCESS", "output": result.decode('utf-8')}}
        except subprocess.CalledProcessError as e:
            return {{"status": "FAIL", "error": str(e)}}
'''
            with open(filename, 'w') as f:
                f.write(content)
            print(f"Generated: {filename}")

if __name__ == "__main__":
    create_modules('rules.csv')