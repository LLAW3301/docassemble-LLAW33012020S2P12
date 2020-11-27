import os
import sys
from setuptools import setup, find_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')
def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.LLAW33012020S2P12',
      version='1.0',
      description=('Identity Document Navigator'),
      long_description="# docassemble.LLAW33012020S2P12\r\n\r\nThis is our application for the St Vincent de Paul's Men's Crisis Centre.\r\nThe application has been written to help users in their journey to obtain identification documents relevant to them, find legal aid resources and also find basic court contacts.\r\n\r\nThe main aim of the application is to create an easy and simple platform through which the users can obtain basic information as well as further contacts and steps to follow to get where they want to go.\r\n\r\n## Authors\r\n\r\n- Helen Kremmidiotis\r\n- Henry Gill\r\n- Janelle Chaptini\r\n- Sera Pelizzari\r\n- Alia Rafferty-Warhurst\r\n",
      long_description_content_type='text/markdown',
      author='Flinders University',
      author_email='ferr0182@flinders.edu.au',
      license='All Rights Reserved',
      url='https://flinders.edu.au',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=[],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/LLAW33012020S2P12/', package='docassemble.LLAW33012020S2P12'),
     )

