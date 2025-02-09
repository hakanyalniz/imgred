from setuptools import setup

setup(
    name="imgred",
    version="1.0",
    description="A simple image compression tool done as a small project",
    author="Hakan",
    py_modules=['imgred'],
    install_requires=[
        "pillow>=11.1.0",
    ],
    entry_points={
        'console_scripts': [
            'imgred=imgred:main',
        ],
    },
    classifiers=[ 
        "Programming Language :: Python :: 3",
    ],
)