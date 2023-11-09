import setuptools


with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name="PySide6-Fluent-Widgets",
    version="1.3.6",
    keywords="pyqt fluent widgets",
    author="zhiyiYo",
    author_email="shokokawaii@outlook.com",
    description="A fluent design widgets library based on PySide6",
    long_description=long_description,
    long_description_content_type='text/markdown',
    license="GPLv3",
    url="https://github.com/zhiyiYo/PyQt-Fluent-Widgets/tree/PySide6",
    packages=setuptools.find_packages(),
    install_requires=[
        "PySide6<=6.4.2",
        "PySideSix-Frameless-Window>=0.3.1",
        "darkdetect",
    ],
    extras_require = {
        'full': ['scipy', 'pillow<=9.4.0', 'colorthief']
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent'
    ],
    project_urls={
        'Documentation': 'https://qfluentwidgets.com/',
        'Source Code': 'https://github.com/zhiyiYo/PyQt-Fluent-Widgets/tree/PySide6',
        'Bug Tracker': 'https://github.com/zhiyiYo/PyQt-Fluent-Widgets/issues',
    }
)
