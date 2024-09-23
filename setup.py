from setuptools import find_packages, setup
from typing import List

HYPE_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements.
    '''
    requirements = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file_obj:
            # Read all lines and remove newlines
            requirements = file_obj.readlines()
            requirements = [req.strip() for req in requirements]
            
            # Remove '-e .' if present
            if HYPE_E_DOT in requirements:
                requirements.remove(HYPE_E_DOT)
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    
    return requirements

setup(
    name='Mlproject',
    version='0.0.1',
    author='Prajwal and Sumanth',
    author_email="prajwalkumar2228@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
