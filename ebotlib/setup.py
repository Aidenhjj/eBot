from distutils.core import setup

setup(
    name = 'ebot',
    version = '0.1.0',
    author = 'Abhishek Gupta',
    author_email = "abhishek@sutd.edu.sg",
    packages=['ebotlib'],
    url='',
    license='LICENSE.txt',
    description='eBot library.',
    long_description=open('README.txt').read(),
    install_requires=["PySerial>=2.7"]
)
