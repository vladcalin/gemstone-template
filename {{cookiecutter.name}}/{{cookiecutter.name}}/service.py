import os.path

from gemstone import MicroService, public_method, private_api_method

from {{cookiecutter.name}}.handlers.index import IndexHandler
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


class {{ cookiecutter.name|capitalize }}Service(MicroService):
    name = "{{cookiecutter.name}}"

    host = "0.0.0.0"
    port = 8000
    accessible_at = ("127.0.0.1", 8000)

    static_dirs = [
        ("/static", os.path.join(ROOT_DIR, "html", "static"))
    ]
    template_dir = os.path.join(ROOT_DIR, "html", "templates")

    extra_handlers = [
        (r"/", IndexHandler)
    ]

    @public_method
    def hello_world(self):
        return "hello world"
