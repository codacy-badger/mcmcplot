from setuptools import setup, find_packages
import codecs

def read(fname):
    with codecs.open(fname, 'r', 'latin') as f:
        return f.read()
    
# read in version number
version_dummy = {}
exec(read('mcmcplot/__version__.py'), version_dummy)
__version__ = version_dummy['__version__']
del version_dummy

setup(
    name='mcmcplot',
    version=__version__,
    description='A library to plot and analyze chains from mcmc simulations',
    url='https://github.com/prmiles/mcmcplot',
    download_url='https://github.com/prmiles/mcmcplot',
    author='Paul Miles',
    author_email='prmiles@ncsu.edu',
    license='MIT',
    package_dir={'mcmcplot': 'mcmcplot'},
    packages=find_packages(),
    zip_safe=False,
    install_requires=['numpy>=1.14', 'scipy>=1.0', 'matplotlib>=2.2.0', 'h5py>=2.7.0', 'statsmodels>=0.9.0', 'seaborn>=0.9.0'],
    extras_require = {'docs':['sphinx'], 'plotting':['matplotlib', 'seaborn'],},
    classifiers=['License :: OSI Approved :: MIT License',
                   'Natural Language :: English',
                   'Operating System :: MacOS :: MacOS X',
                   'Operating System :: POSIX :: Linux',
                   'Programming Language :: Python :: 3.6',
                   'Framework :: IPython',
                   'Intended Audience :: Science/Research',
                   'Topic :: Scientific/Engineering',
                   ]
)
