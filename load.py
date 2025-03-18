import pandas as pd
import os
cwd = os.getcwd()
files_to_be_loaded = os.listdir(f'{cwd}/data')
output_dfs = {}
print('Loading files...')
if files_to_be_loaded:
    for file in files_to_be_loaded:
        output_dfs[file] = pd.read_csv(f'{cwd}/data/{file}')

print(f'Loaded files:')
for file in output_dfs:
    print('\t-',file)

