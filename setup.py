from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

setup(
	name="zinye_core",
	version="0.0.1",
	description="Market-agnostic ERPNext SaaS base app for Zinye",
	author="Zinye",
	author_email="dev@zinye.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires,
)
