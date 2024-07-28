from setuptools import setup, find_packages
from typing import List

HYPEN_E_DPT = '-e .'

def get_requirement(file_path:str)->List[str]:
    with open(file_path) as f:
        requirements=f.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DPT in requirements:
            requirements.remove(HYPEN_E_DPT)
    return requirements

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

__version__ = "0.0.4"
REPO_NAME = "first-mongodb-connector4539"
PKG_NAME = "momgodbautomation"
AUTHOR_USER_NAME = "koushikkonwar"
AUTHOR_EMAIL = "kosec39@gmail.com"

setup(
    name=PKG_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A python package for connecting with database.",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=get_requirement("./requirements_dev.txt")
)