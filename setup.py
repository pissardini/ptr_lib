from setuptools import setup, find_packages
 
setup(name='ptr_lib',
      version='0.0.1',
      url='https://github.com/pissardini/ptr_lib',
      license='MIT',
      author='R.S.Pissardini, Alex Boava',
      author_email='pissardini@usp.br,alex.boava@usp.br',
      description='A library of resources for Transportation, Geomatics and GNSS Analysis.',
      maintainer="Laboratory of Topography and Geodesy - University of Sao Paulo",
      packages=find_packages(exclude=['tests']),
      long_description=open('README.md').read(),
      classifiers=[
          'Environment :: Console',
          'Intended Audience :: End Users/Desktop',
          'License :: OSI Approved :: MIT License',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Topic :: Communications :: Geomatics'
          ],
      zip_safe=False)
