from setuptools import setup, find_packages
from typing import List

# Create a function to get the requirements from the requiements.txt file
def get_requirements() -> List[str]:
    with open("requirements.txt") as f:
        return f.read().splitlines()


setup(
    name="Sensor-Fault-Detection",
    version="0.0.1",
    author="Shubham Aware",
    author_email="imawareshubh18@gmail.com",
    packages=find_packages(),
)