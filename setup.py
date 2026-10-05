from setuptools import setup

with open("requirements.txt") as file:
    requitments = file.read().splitlines()

setup(
    name="Ayumu",
    version="0.0.1",
    description="Segmentation Image",
    install_requires=requitments,
    python_requires=">=3.10",
    license="MIT License",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
)
