from distutils.core import setup
from lru import __version__ as version

setup(
    name='lru',
    version=version,
    description='A simple LRU cache implementation',
    author='Jared Kuolt',
    author_email='luckythetourist@gmail.com',
    url='http://github.com/luckythetourist/lru',
    py_modules=['lru'],
    license='MIT License',
    platforms=['any'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python', 
        'Topic :: Software Development', 
        'Topic :: Software Development :: Libraries', 
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
