import setuptools

with open("README.md","r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"


REPO_NAME = "PYTHON-PACKAGE"
AUTHOR_USER_NAME = "Fahdmoh01"
SRC_REPO= "PTHON-PACKAGE"
AUTHOR_EMAIL = "fahdmoh.1@gmail.com"

setuptools.setup(
    name= SRC_REPO,
    version= __version__,
    author= AUTHOR_USER_NAME,
    author_email= AUTHOR_EMAIL,
    description= "My python package to setup my Data Science Projects",
    long_description= long_description,
    long_description_content = "text/markdown",
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages= setuptools.find_packages(where="src")
)