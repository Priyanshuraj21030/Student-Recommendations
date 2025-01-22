from setuptools import setup, find_packages

setup(
    name="quiz_analyzer",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "dataclasses>=0.6",
        "typing>=3.7.4",
        "python-dateutil>=2.8.2",
    ],
    python_requires=">=3.7",
    author="Your Name",
    description="A quiz performance analysis and recommendation system",
) 