from os.path import join, dirname
from setuptools import setup, find_packages

HERE = dirname(__file__)


def get_version():
    fh = open(join(HERE, "piwik", "__init__.py"))
    try:
        for line in fh.readlines():
            if line.startswith("__version__ ="):
                return line.split("=")[1].strip().strip('"')
    finally:
        fh.close()


setup(
    name="django-piwik",
    version=get_version(),
    description="Application to add Piwik analytics to a Django site",
    long_description=(open(join(HERE, "README.md")).read() + "\n\n" +
                      open(join(HERE, "LICENSE.txt")).read()),
    author="Benjamin Hell",
    author_email="b@bhell.net",
    url="https://github.com/bhell/django-piwik/",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.4",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Framework :: Django",
    ],
    zip_safe=True,
    tests_require=["Django>=1.2"],
    test_suite="tests"
)