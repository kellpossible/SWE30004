# SWE30004 Assignment 1

## Setup/Install Instructions
Ensure python 3 is available and pip is installed.

`pip install -r requirements.txt`

The app server can be run with:

`APP_SETTINGS=config.DevelopmentConfig python3 main.py`

## Deployment with heroku

Use the Heroku CLI and git to deploy the code to Heroku. 

## Deployment with vagrant/ansible

Vagrant is configured to create a new VM that is configured with Ansible.

The VM can be created with: `vagrant up`

Ansible playbooks and required templates are located in the `ansible/` directory.
