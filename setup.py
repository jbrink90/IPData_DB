import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="IPData_DB",
    version="0.0.1",
    author="Jordan Brinkman",
    author_email="jbrink90@github.com",
    description="A utility to lookup and store IPData.co IP address results.",
    long_description="ipdata_db allows a user to retrieve information about an IP address without the need to waste API credits.",
    long_description_content_type="text/markdown",
    url="https://github.com/jbrink90/IPData_DB",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
	install_requires=[
		'requests',
		'pymongo'
	],
)
