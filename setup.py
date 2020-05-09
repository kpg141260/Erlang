import fnmatch
from setuptools import find_packages, setup
from setuptools.command.build_py import build_py as build_py_orig

excluded = [
    '.git*',
    '.vscode',
    '*workspace',
]

class build_py(build_py_orig):
    def find_package_modules(self, package, package_dir):
        modules = super().find_package_modules(package, package_dir)
        return [
            (pkg, mod, file)
            for (pkg, mod, file) in modules
            if not any(fnmatch.fnmatchcase(file, pat=pattern) for pattern in excluded)
        ]

setup(name='Erlang',
    classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Web Environment',
          'Intended Audience :: Developers',
          'Operating System :: MacOS :: MacOS X',
          'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)'
          'Programming Language :: Python',
          'Topic :: Forecasting :: Erlang :: Erlang-B :: Erlang-C',
          'Topic :: Contact Center :: Call Center',
          ],
      version='0.9',
      url='https://github.com/kpg141260/erlang',
      author='Peter Gossler',
      author_email='kpg141260@live.de',
      description='Provides Erlang calculations and methodologies for contact center forecasting',
      packages=find_packages() , 
      long_description=open('README.md').read(),
      cmdclass={'build_py': build_py},
      zip_safe=False)