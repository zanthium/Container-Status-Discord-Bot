import yaml

with open('config.yml','r') as file:
    driver = yaml.safe_load(file)
    containers = driver['docker']['containers']
print(containers)