from setuptools import find_packages, setup
from typing import List


HYPHEN_E_DOT = '-e .'
def get_requirenments(file_path:str)->List[str]:
    '''
    This funtion will return the list of requirenments
    '''
    requirenments = []
    with open(file_path) as file_obj:
        requirenments = file_obj.readlines()
        requirenments = [req.replace("\n","")for req in requirenments]

        if HYPHEN_E_DOT in requirenments:
            requirenments.remove(HYPHEN_E_DOT)
            
    return requirenments


setup(
name = 'mlproject',
version = '0.0.1',
author = 'Neha',
author_email = 'nehakankekar436@gmail.com',
packages = find_packages(),
install_requires = get_requirenments('requirenments.txt')



)
