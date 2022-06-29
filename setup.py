from setuptools import setup

setup(
    name='global_gender_predictor',
    version='0.0.1',
    description='Predict gender based on first name',
    author='Rianne Klaver',
    author_email='rianne.klaver@attract.ai',
    license='MIT',
    url='https://github.com/attract-ai/global-gender-predictor',
    packages=['global_gender_predictor'],
    package_data={'global_gender_predictor': ['data/*.jsonl.gz']}
)

