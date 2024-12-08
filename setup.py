from setuptools import setup, find_packages

setup(
    name="adaptive-power-neurons",
    version="0.1.3.2.0",
    description="A neural network library using Adaptive Power Neurons.",
    author="Dedeep Vasireddy",
    packages=find_packages(),
    install_requires=["numpy"],
    python_requires=">=3.6",
)
