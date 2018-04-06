from setuptools import setup


setup(
    name="pointless_project",
    py_modules=["module"],
    entry_points={"tox": ["docker = tox_docker"]},
)
