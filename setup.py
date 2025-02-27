from setuptools import find_packages
from setuptools import setup

setup(
    name="OpenAIAuth",
    version="0.3.2",
    license="MIT",
    author="Rawand Ahmed Shaswar and Antonio Cheong",
    author_email="acheong@student.dalat.org",
    description="OpenAI Authentication Reverse Engineered",
    packages=find_packages("src"),
    package_dir={"": "src"},
    py_modules=["OpenAIAuth"],
    url="https://github.com/acheong08/OpenAIAuth",
    project_urls={
        "Bug Report": "https://github.com/acheong08/OpenAIAuth/issues/new"
    },
    install_requires=[
        "requests",
    ],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    long_description=open("README.md", "rt", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
)
