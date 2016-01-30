from setuptools import find_packages, setup

from tagcloud import __version__ as version

setup(
    name='django_tagcloud',
    version=version,
    license='BSD',
    author='Sam Kingston',
    author_email='sam@sjkwi.com.au',
    description='A simple Django templatetag for generating tagclouds',
    url='https://github.com/sjkingo/django_tagcloud',
    install_requires=[
        'Django',
    ],
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
    ],
)
