from typing import List

from setuptools import find_packages, setup


def get_requirements(file_path: str) -> List[str]:
    """
    This function will return the list of requirements
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if "-e ." in requirements:
            requirements.remove("-e .")
    return requirements


setup(
    name="mlproject",
    version="0.0.1",
    packages=find_packages(),
    author="Abai",
    author_email="abairajpoinachi@gmail.com",
    install_requires=get_requirements("requirements.txt"),
)
