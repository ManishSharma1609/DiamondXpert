from setuptools import find_packages,setup
from typing import List

"""HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements
"""

setup(
    name='DiamondPricePrediction',
    version='0.0.1',
    author='Manish Sharma',
    author_email='manishsharmachd19@gmail.com',
    install_requires=["pandas", "scikit-learn", "numpy", "seaborn", "flask", "mlflow==2.2.2", "dvc", "ipykernel", "xgboost", "pytest==7.1.3", "tox==3.25.1", "black==22.8.0", "flake8==5.0.4", "mypy==0.971"],
    packages=find_packages()
)