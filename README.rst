Gemstone microservice template
==============================

A cookiecutter template for quickly generating a microservice structure

Attributes:

- ``name`` - the name of the microserivice. This will be the name of the main module so it should only contain something that is a valid
  Python module identifier (lowercase letters, underscore and maybe digits)
- ``version`` - the version of the microservice
- ``author`` - your name
- ``short_description`` - a few words about your microservice

This will generate the following structure (let's say the ``name`` attribute is ``microsvc``:

::
  
  - readme.rst # a generic readme
  - setup.py  # a minimal setup.py for easily installation if the package
  - MANIFEST.in  # for static file inclusion
  - microsvc # the main module of the service
    - cli.py  # a command-line utility script.
    - service.py  # where the main MicroService class is
    - handelers # for custom handlers
      - index.py # dummy Tornado handler for "/"
    - html
      - static # this ships with MaterializeCSS frontent framework
        - css
        - js
        - fonts
          - roboto
      - templates
        - template.html  # the base template
        - index.html    # demo greetings message to be desplayed at "/"
 
 
By default, it assumes that all the templates will be in the templates directory. If you make some restructuring in the templates and/or static directories, you have to update the MANIFEST.in file to inlclude the extra files properly.        
        
Enjoy :)
    

