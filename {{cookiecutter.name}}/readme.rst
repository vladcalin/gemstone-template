{{cookiecutter.name}}
=====================

Welcome to {{cookiecutter.name}}!

This is a microservice that is powered by the `gemstone <https://github.com/vladcalin/gemstone>`_ library.


Starting the service
--------------------

```
    
    python -m {{cookiecutter.name}}.service [--port=...][--host=...][--accessible_at=...][--service_registry_urls=ip[,ip[...]]]


```

Getting the current configuration
---------------------------------

```

    python -m {{cookiecutter.name}}.configuration


```
