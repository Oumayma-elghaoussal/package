from setuptools import setup, find_packages

setup(
    name="CSTC",
    version="1.0.0",
    author="oumayma",
    author_email="elghaoumayma201@gmail.com",
    description="Un package Python simple pour des outils divers.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Oumayma-elghaoussal/CSTC.com",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[],  # Ajouter des dépendances si nécessaire
)
