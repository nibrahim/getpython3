from setuptools import setup

setup(
    name="getpython3",
    version="0.1",
    description='Website for getpython3.net',
    long_description=open('README').read(),
    license='Simplified BSD',
    author='Baiju M.',
    author_email='baiju.m.mail@gmail.com',
    url='http://getpython3.net/',
    platforms=['linux', 'osx', 'win32'],
    py_modules=['py3k'],
    install_requires = ['flask', 'sqlalchemy', 'flask-sqlalchemy', 'flask-openid'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License'
        'Programming Language :: Python'],
)