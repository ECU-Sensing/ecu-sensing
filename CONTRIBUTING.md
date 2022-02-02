# Contributing

When contributing to this repository, please first discuss the change you wish to make via issue,
email (sawyerco21@ecu.edu), or any other method with the owners of this repository before making a change. 

Please note we have a [Code of Conduct](https://github.com/ECU-Sensing/ecu-sensing/blob/main/CODE_OF_CONDUCT.md), please follow it in all your interactions with the project.

## Contribution Process

1. [Contact us](mailto:sawyerc21@ecu.edu) to discuss your proposed additions
2. Set up a local development environment, this includes any new sensor/hardware planned to be supported by contribution
3. Complete development of additional module in the **devices directory**
4. Create test file to correspond with new module in the **tests directory**
5. Follow the additional steps to [contribute documentation](#contribute-documentation)
6. Submit pull request, make sure to identify:
   1. Your Contact (Name, Email/Phone)
   2. Short Description of the change
   3. Screenshots of successfully run test
   4. Date of last test
7. Look out for our response
   
Happy Coding :) 
   


### Contribute Documentation
We maintain set of documentation for every included module on readthedocs.org. We utilize [Sphinx]() to do so. In order to include your module in the automatic procedures of Sphinx you must adhere to a few things:

- Follow proper styling when documenting module. This includes documenting every single module you plan to include. To find more information on this coding style refer to our [DOC_STYLE.md](https://github.com/ECU-Sensing/ecu-sensing/blob/main/docs/DOC_STYLE.md)
- Sphinx will need to be installed on your local machine.
    > pip install -r sphinx sphinx_rtd_theme
- In the docs > api.rst, add a new automodule unit.
  > .. automodule:: devices.hydros
   :members:
   :show-inheritance:

  > .. automodule:: devices.[NEW_DEVICE_NAME]
   :members: LEAVE BLANK
   :show-inheritance: 

- Use Sphinx to build the html files needed:
  > make html
- You can know view the [/docs/_build/html/api.html](https://github.com/ECU-Sensing/ecu-sensing/blob/main/docs/api.rst) to check inclusion and formatting of your documentation
- Congratulations! You can now commit those changes, you have successfully added documentation to your module!
  

