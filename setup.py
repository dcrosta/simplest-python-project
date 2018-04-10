from setuptools import setup


setup(
    name="pointless_project",
    py_modules=["module"],
    setup_requires=["vcversioner"],
    vcversioner={"version_module_paths" : ["_version.py"]},
)
