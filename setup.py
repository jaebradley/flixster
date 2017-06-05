from setuptools import setup, find_packages
setup(
  name="flixster",
  packages=find_packages(exclude=["tests*"]),
  install_requires=["requests"],
  version="0.0.2",
  description="Flixster Client",
  author="Jae Bradley",
  author_email="jae.b.bradley@gmail.com",
  url="https://github.com/jaebradley/flixster",
  download_url="https://github.com/jaebradley/flixster/tarball/0.1",
  keywords=["flixster", "movies"],
  classifiers=[],
)