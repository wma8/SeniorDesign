# System Information

## RHEL VM

The Red Hat Enterprise Linux system can be accessed at `152.14.85.171` using unity credentials.

## DDVE

The DDVE System can be accessed through the RHEL system at `192.168.41.52` using username `sysadmin` and password `sdcTeam21`.

# Development
This project makes use of pip and venv to manage imported packages and dependencies.

## Setting up a development environment

1. `git clone https://github.ncsu.edu/engr-csc-sdc/2019SpringTeam26.git`
2. `cd 2019SpringTeam26`
3. `git checkout develop`
4. `./setup.sh`

If the steps above were followed correctly, you should have a `.env` directory inside the repo. This directory maintains installed packages specific to the project's virtual environment.

## Activating the virtual environment

Make sure you have followed the instructions in [environment setup](#setting-up-a-development-environment)

To use the correct versions of packages and their dependencies, you must activate the virtual environment:

`source venv/bin/activate`

After running the command above, `python --version` should return 3.6.3 and `pip list` should return a list of the installed packages that matches the `requirements.txt` file.

## Deactivating the virtual environment

Run `deactivate`

## Installing a new package

Make sure you have followed the instructions in [activating the virtual environment](#activating-the-virtual-environment)

1. `pip install <package-name>`
2. `pip freeze > requirements.txt`

This will update the `requirements.txt` file with the newly installed packages and dependencies. Please commit these updates to the repo.

## Updating your installed packages

If a package cannot be found, it could mean that there are new dependencies in `requirements.txt` that have not been installed in your virtual environment. Run the following commands to fix this:

1. `source .env/bin/activate`
2. `pip install -r requirements.txt`

This will install all packages in `requirements.txt` in your virtual environment.

## Reinstalling your virtual environment

1. `rm -rf .env`
2. `./setup.env`

# Automated Execution

Make sure you have followed the instructions in [activating the virtual environment](#activating-the-virtual-environment)

To keep the process running in the background (even after ssh disconnection), we use the `screen` command.

## Start Execution in Background

1. `screen` 
2. `python -m main <operation_list.auto> e.x: automation/test-1.auto`
3. press `ctrl+a` followed by `d` to detach the screen from the current shell

If done correctly, `screen -list` will show something like this: `6931.pts-0.sd-vm21  (Detached)` where `6931` is the screen identifier. At this point, you can safely exit your ssh session and the python program will run in the background on the VM until completion.

## Reattach to Screen

1. `screen -l` will return something like this: `6931.pts-0.sd-vm21  (Detached)` where `6931` is the screen identifier
2. `screen -r 6931` will reattach the screen

At this point, you can send signals to the process like you normally would in ssh.

# Testing

Make sure you have followed the instructions in [activating the virtual environment](#activating-the-virtual-environment)

To run all unit tests and generate a coverage report:

`python -m pytest --cov-report html --cov-config=.coveragerc --cov=readop tests/`

This will generate coverage documents in htmlcov/ directory.

# Documentation Generation

Make sure you have followed the instructions in [activating the virtual environment](#activating-the-virtual-environment)

## Folder Structure

Documentation exists in `2019SpringTeam26/readop/docs`

`../docs/build` contains all generated documentation data.

`../docs/source` contains the .rst files that determine the generated documentation structure. These are initially generated but can be edited manually if necessary.

## Generating .rst Source Files

Run the following when a module/file is created or renamed:

1. `cd readop/docs`
2. `sphinx-apidoc -e -o source/ ../readop`, use `-f` if you want to overwrite existing files

Results will be in `source/`

## Generating HTML Documentation

Run the following when changes have been made to python documentation in source code:

1. `cd readop/docs`
2. `make html`

Results will be in `build/html/`

## Cleaning the Build Folder

This removes the generated html.

1. `cd readop/docs`
2. `make clean`
