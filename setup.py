from setuptools import find_packages , setup
from typing import List




hypen_e_dot ='-e .'
def get_requirement_text(file_path:str)-> List[str]:
    '''
    fetches the requirement.txt
    '''
    requirement=[]
    with open(file_path) as file_obj:
        requirement=file_obj.readlines()
        requirement=[req.replace('/n','') for req in requirement]
        if hypen_e_dot in requirement:
            requirement.remove('-e .')

        return requirement


setup(
    name='shreya',
    version='0.0.1',
    author='shreya',
    author_email='shreyaprao153@gmail.com',
    packages=find_packages(),
    # install_requires=['pandas','numpy','seaborn']
    install_requires=get_requirement_text('requirement.txt')
)