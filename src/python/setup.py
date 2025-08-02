from setuptools import setup, find_packages

setup(
    name="nfcflet",
    version="0.1.0",
    packages=find_packages(where="python"),
    package_dir={"": "python"},
    install_requires=["flet>=0.28.3", "flet_cli>=0.28.3"]
)
