from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='Virtual PC',
    url='https://github.com/buhron/virtualpc',
    author='buhron',
    author_email='mbh90180@gmail.com',
    # Needed to actually package something
    packages=['virtual-env-pc'],
    # Needed for dependencies
    install_requires=['numpy'],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='MIT',
    description='Run Virtual PC on python!',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)
