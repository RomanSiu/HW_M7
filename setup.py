from setuptools import setup

setup(name="clean_folder",
      version="1",
      description="app for cleaning folder",
      url="https://github.com/RomanSiu/HW_M6.git",
      author="Roman Siusiailo",
      author_email="siusiailoroman@gmail.com",
      packages=["clean_folder"],
      entry_points={'console_scripts': ['cleanfolder = clean_folder.Sort_grbg:sort_folder']})