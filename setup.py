from setuptools import setup

setup(
   name='rep',
   version='1.0',
   description='LIS Meeting',
   author='Alex LaGrassa',
   author_email='lagrassa@cmu.edu',
   packages=['rep'],  #same as name
   install_requires=['matplotlib', 'numpy', 'mdp', 'Pillow', 'IPython', 'scipy','jupyter'],
   )
