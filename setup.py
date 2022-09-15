import io
from os.path import abspath, dirname, join
from setuptools import find_packages, setup


HERE = dirname(abspath(__file__))
LOAD_TEXT = lambda name: io.open(join(HERE, name), encoding='UTF-8').read()
DESCRIPTION = '\n\n'.join(LOAD_TEXT(_) for _ in [
    'README.rst'
])

setup(
  name = 'satang_pro_sdk',      
  packages = ['satang_pro_sdk'], 
  version = '1.0', 
  license='MIT', 
  description = 'Python SDK for Satangpro Open API',
  long_description=DESCRIPTION,
  author = 'Satangpro',                 
  author_email = 'platforms@satangcorp.com',    
  url = 'https://github.com/satang-official/python-sdk',
  download_url = 'https://github.com/satang-official/python-sdk/archive/refs/tags/V1.0.tar.gz',  
  keywords = ['Satangpro API', 'Satangpro', 'satangpro','Satangpro python'],
  classifiers=[
    'Development Status :: 4 - Beta',     
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
    'Programming Language :: Python :: 3.12'
  ],
)