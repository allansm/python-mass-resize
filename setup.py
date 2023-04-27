from setuptools import setup, find_packages
import platform

modules=[
    "Pillow"
]

setup(
    name="mass-resize",
    version="2023.4.26",
    packages=find_packages(),

    install_requires=modules,

    entry_points={
        'console_scripts': [
            'mass-resize = allansm.mass_resize:run',
        ],
    }

)
