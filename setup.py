from setuptools import setup

with open ("README.md", "r", encoding="utf-8") as fh:
           long_description = fh.read() 

AUTHOR_NAME = 'okanolgun'
SRC_REPO = 'C:\Users\oknol\projects\movieRecommendationSystem'
LIST_OF_REQUIREMENTS = ['streamlit'] 

setup(
    name = SRC_REPO,
    author = AUTHOR_NAME,
    package = [SRC_REPO],
    install_requires = LIST_OF_REQUIREMENTS
)

