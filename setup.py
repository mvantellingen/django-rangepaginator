from setuptools import find_packages, setup

install_requires = [
    'Django>=1.7',
    'six>=1.1',
]

docs_require = [
    'sphinx>=1.4.0',
]

tests_require = [
    'pytest==3.0.1',
    'pytest-cov==2.3.1',
    'pytest-django==3.0.0',
    'pytest-sugar==0.7.1',

    # Linting
    'isort==4.2.5',
    'flake8==3.0.4',
    'flake8-blind-except==0.1.1',
    'flake8-debugger==1.4.0',
]

setup(
    name='django-rangepaginator',
    version='1.1.0',
    description="Nice paginator for Django",
    long_description=open('README.rst', 'r').read(),
    url='https://github.com/mvantellingen/django-rangepaginator',
    author="Michael van Tellingen",
    author_email="michaelvantellingen@gmail.com",
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={
        'docs': docs_require,
        'test': tests_require,
    },
    use_scm_version=True,
    entry_points={},
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    zip_safe=False,
)
