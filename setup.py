from setuptools import setup, find_packages

setup(
    name='eeHelpers',
    packages=find_packages(),
    include_package_data=True,
    version='0.0.1',
    description='Helper functions for GEE',
    url='https://github.com/BuddyVolly/eeHelpers',
    author='Andreas Vollrath',
    author_email='andreas.vollrath[at]fao.org',
    license='MIT License',
    keywords=['Earth Observation', 'Remote Sensing', 'Google Earth Engine'],
    zip_safe=False,
)