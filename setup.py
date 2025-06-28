from setuptools import setup, find_packages
setup(
    name="omqs",
    version="0.1.0",  # <- ESSA LINHA É OBRIGATÓRIA
    packages=["omqs"],
    install_requires=[
        "requests",
        "python-dotenv"
    ],
    author="Outspoken Market",
    author_email='info@outspokenmarket.com',
    description="Official Python client for OMQS Quant Signals API",
    license="MIT",
    keywords=["quant", "api", "trading", "omqs", "signals"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
)
