import csv
import subprocess
import secrets
from pathlib import Path

def generate_password():
    return secrets.token_hex(8)

cwd = Path.cwd()

with open ("new_users.csv", "r") as input_csv, open("new_users_with_passwd.csv", "w", newline='') as output_csv:
    reader = csv.DictReader(input_csv)
    writer = csv.DictWriter(output_csv, reader.fieldnames)
    writer.writeheader()
    for user in reader:
        user["password"] = generate_password()
        useradd_cmd = ["/sbin/useradd",
                       "-c", user["fullname"],
                       "-m",
                       "-G", "users",
                       "-p", user["password"],
                       user["username"]]
        subprocess.run(useradd_cmd, check=True)
        writer.writerow(user)