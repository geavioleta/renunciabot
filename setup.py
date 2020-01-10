from setuptools import setup

setup(name='renunciabot',
      version='2.1.0',
      description='',
      url='https://github.com/geavioleta/renunciabot',
      author='geavioleta',
      author_email='geavioleta@protonmail.com',
      license='GNU',
      packages=['renuncia'],
      entry_points = {
          'console_scripts': ['renunciabot=renuncia.bot:run'],
      },
      install_requires=['requests', 'pyowm', 'python-twitter'],
      python_requires='>=3.5',
      zip_safe=False)