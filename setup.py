from setuptools import setup

exec (open('dash_callback_chain/version.py').read())

setup(
    name='dash_callback_chain',
    version=__version__,
    author='nicolaskruchten',
    packages=['dash_callback_chain'],
    include_package_data=True,
    license='MIT',
    description='Dash component to visualize callback chains',
    install_requires=[]
)
