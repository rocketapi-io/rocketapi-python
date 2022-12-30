import setuptools


setuptools.setup(
    name="rocketapi",
    version="1.0.1",
    author="RocketAPI",
    author_email="developer@rocketapi.io",
    description="RocketAPI Python SDK",
    packages=["rocketapi"],
    url="https://github.com/rocketapi-io/rocketapi-python",
    download_url="https://github.com/rocketapi-io/rocketapi-python/archive/refs/tags/v1.0.1.tar.gz",
    install_requires=["requests"]
)
