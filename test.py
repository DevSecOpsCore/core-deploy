import yaml

import yaml

with open('temp.yaml') as f:
    temp = yaml.safe_load_all(f)
    print(temp)