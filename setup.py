from setuptools import setup, find_packages

VERSION = '0.1.0'

setup(
    name="mkdocs-br-industrial-theme",
    version=VERSION,
    url='https://github.com/brcclark/mkdocs-br-theme',
    license='BSD',
    description='Theme to match with the standard B&R Industrial Automation documentation styling.',
    author='Connor Trostel',
    author_email='connor.trostel@br-automation.com',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'mkdocs.themes': [
            'brtheme = br_theme',
        ]
    },
    zip_safe=False
)
