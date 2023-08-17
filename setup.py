from setuptools import setup
import os

setup(
    name='accelergy-plug-in',
    version='0.4',
    description='An energy estimation plug-in for Accelergy framework using CACTI',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Electronic Design Automation (EDA)',
    ],
    keywords='accelerator hardware energy estimation',
    author='Yannan Wu',
    author_email='nelliewu@mit.edu',
    license='MIT',
    install_requires=['pyYAML'],
    python_requires='>=3.8',
    data_files=[
        ('share/accelergy/estimation_plug_ins/accelergy-plug-in',
           ['plugin.estimator.yaml',
            'plugin_wrapper.py'])
    ],
    include_package_data=True,
    entry_points={},
    zip_safe=False,
)
