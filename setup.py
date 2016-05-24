from setuptools import setup, find_packages

setup(
    name="trivia-wars",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'pyglet>=1.2.4'
    ],
    url='https://github.com/tenakova/trivia-wars',
    author="Tina Nakova",
    author_email="tinna.nakova@gmail.com",
    description="Python networking multiplayer quiz game.",
    license="GNU GPL v3",
    keywords="trivia wars network game quiz multiplayer",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Topic :: Games/Entertainment :: Board Games",
        "Topic :: Games/Entertainment :: Turn Based Strategy",
        "Programming Language :: Python :: 3.5",
        "Operating System :: Microsoft :: Windows",
        "Natural Language :: English",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
    ],
    entry_points={
          'console_scripts': [
              'trivia-wars = trivia-wars.__main__:main'
          ]
      }
)
