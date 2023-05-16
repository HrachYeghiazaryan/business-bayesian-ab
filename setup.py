from setuptools import setup, find_packages

setup(
    author='Hrach Yeghiazaryan',
    description='Implementation of Bayesian A/B testing for business cases',
    name='business_bayesian_ab',
    version='0.1.0',
    packages=find_packages(include=['business_bayesian_ab','business_bayesian_ab.*']),
    install_requires=['numpy','pandas','pyarrow','matplotlib']
)