'''
The setup.py file is an essential part of packaging and 
distributing Python project. It is used by setup tools
to define the configuration of the project, such as metadata , dependencies, and other details.'''

from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    """
    This function reads the requirements.txt file and returns its contents as a list.
    """
    try:
        with open('requirements.txt', 'r') as file:
            # Read lines from the file
            lines = file.readlines()
            # Initialize the list to store requirements
            requirement_lst = [
                line.strip() for line in lines 
                if line.strip() and line.strip() != '-e .'
            ]
    except FileNotFoundError:
        print('Requirements file not found.')
        return []
        
    return requirement_lst

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Susanta",
    author_email="susantabaidya20133@gmail.com",
    packages=find_packages(),  # Corrected from package to packages
    install_requires=get_requirements(),
)
