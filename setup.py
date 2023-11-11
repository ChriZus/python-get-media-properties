from pathlib import Path
from setuptools import find_packages, setup

README = Path(__file__).resolve().parent / 'README.md'

if __name__ == '__main__':
    setup(
        name='get-media-properties',

        version='0.1.1',

        description='Get media properties',
        long_description=README.read_text(encoding='utf-8'),
        long_description_content_type='text/markdown',

        url='https://github.com/ChriZus/python-get-media-properties',

        author='Chris',
        author_email='chrizus@gmail.com',

        license='MIT',

        classifiers=[
            'Intended Audience :: Developers',
            'Intended Audience :: End Users/Desktop',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3 :: Only',
            'Topic :: Multimedia :: Sound/Audio',
            'Topic :: Multimedia :: Video',
        ],

        keywords='ffprobe video audio subtitle',

        packages=find_packages(),
        include_package_data=True,

        entry_points={
            'console_scripts': [
                'videoprops=mediaprops:run',
                'audioprops=mediaprops:run2',
                'subtitleprops=mediaprops:run3',
            ],
        },
    )
