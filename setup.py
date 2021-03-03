from setuptools import setup

import resty

with open("README.md") as readme_file:
    readme = readme_file.read()

requirements = [r.strip() for r in open('requirements.txt')]

setup_requirements = ["pytest-runner"]
test_requirements = ["pytest>=3"]

setup(
    author="alecor Dev",
    author_email="alecor.dev@gmail.com",
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3.8",
    ],
    description="resty - Python REST Client Framework",
    install_requires=requirements,
    long_description=readme,
    include_package_data=True,
    keywords="resty",
    name="resty",
    version=resty.__version__,
    packages=["resty"],
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/alecordev/resty",
    zip_safe=False,
)
