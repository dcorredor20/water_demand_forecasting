# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['water_demand_forecasting']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.1.2,<8.0.0',
 'lint>=1.2.1,<2.0.0',
 'matplotlib=3.1.3',
 'numpy>=1.19.5,<2.0.0',
 'pandas>=0.24.0',
 'pyyaml>=5.3.1,<6.0.0',
 'sklearn>=0.0,<0.1']

entry_points = \
{'console_scripts': ['water_demand_forecasting = '
                     'water_demand_forecasting.cli:main']}

setup_kwargs = {
    'name': 'water-demand-forecasting',
    'version': '0.0.1',
    'description': 'Water demand forecasting',
    'long_description': None,
    'author': 'Diego Corredor',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)

