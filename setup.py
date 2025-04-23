from setuptools import find_packages, setup

def get_requirements(file_path:str) -> list[str]:
    requirements = []
    with open(file_path, "r") as f:
        requirements = f.read().splitlines()
    return requirements[:-1] if "-e ." in requirements else requirements


setup(
    name="podcast-listening-time-predictor",
    version="0.0.1",
    author="Naseef",
    author_email="muhammednaseef03@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)
