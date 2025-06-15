from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

## This could be modified
REPO_NAME = "ML Smart Books Recommender System"
AUTHOR_USER_NAME = "Sam"
SRC_REPO = "books_suggester"
LIST_OF_REQUIREMENTS = []


setup(
    name=SRC_REPO,
    version="0.0.1",
    author="Sam",
    description="Smart books recommendations ML package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/samfolbs/smart-book-recommendation",
    author_email="samfolbs@gmail.com",
    packages=find_packages(),
    license="MIT",
    python_requires=">=3.7",
    install_requires=LIST_OF_REQUIREMENTS
)