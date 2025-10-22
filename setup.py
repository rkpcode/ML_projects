from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """Reads the requirements from a file and returns them as a list."""
    requirements = []
    with open(file_path) as file:
        requirements = [req.strip() for req in file.readlines()]
        requirements = [req for req in requirements if req != '-e .']
    return requirements

setup(
    name='mlproject',
    version='0.1.0',
    author='Rahul Kumar Pradhan',
    author_email='',
    description='Machine Learning Project',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
