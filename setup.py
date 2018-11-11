from setuptools import setup

setup(
    name = "vodopad",
    packages = ["vodopad"],
    description = 'Toolkit for managing photos',
    entry_points = {
        "console_scripts": ['vodopad = vodopad.vodopad:main']
        },
    version = '0.1',
    author = "Dmitrii Topornin",
    author_email = "dtopornin@gmail.com",
    install_requires = [
        'Click',
        'face-recognition',
        'tqdm',
        'opencv-python',
        'emoji'
        ],
    license='MIT'
    )
