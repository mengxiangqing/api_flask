
from distutils.core import setup

from Cython.Build import cythonize

from distutils.extension import Extension


sourcefiles = ['Test.pyx', 'main.c']


extensions = [Extension("libTest", sourcefiles,

                        include_dirs=['/Library/Java/JavaVirtualMachines/jdk1.8.0_191.jdk/Contents/Home/include',

                                      '/Library/Java/JavaVirtualMachines/jdk1.8.0_191.jdk/Contents/Home/include/darwin/',

                                      '/Library/Frameworks/Python.framework/Versions/3.6/include/python3.6m'],

                        library_dirs=[
                            '/Library/Frameworks/Python.framework/Versions/3.6/lib/'],

                        libraries=['python3.6m'])]


setup(ext_modules=cythonize(extensions, language_level=3))
