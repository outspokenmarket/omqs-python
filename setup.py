from setuptools import setup, find_packages

setup(
    name='omqs',
    version='0.1.0',
    description='Client for OMQS Trading Signals API',
    author='Outspoken Market',
    author_email='info@outspokenmarket.com',
    url='https://github.com/outspokenmarket/omqs-python',
    packages=find_packages(),
    install_requires=[
        'requests',
        'python-dotenv'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
