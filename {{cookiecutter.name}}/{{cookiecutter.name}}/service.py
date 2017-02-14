import os.path

from gemstone import MicroService, public_method, private_api_method
from gemstone.auth.validation_strategies.header_strategy import HeaderValidationStrategy
from gemstone.event.transport import RabbitMqEventTransport
from gemstone.config.configurable import Configurable
from gemstone.config.configurator import CommandLineConfigurator

from {{cookiecutter.name}}.handlers.index import IndexHandler

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


class {{cookiecutter.name | capitalize}}Service(MicroService):
    name = "{{cookiecutter.name}}"

    # accessibility
    host = "0.0.0.0"
    port = 8000
    accessible_at = ("127.0.0.1", 8000)
    endpoint = "/api"

    # webapp configuration
    static_dirs = [
        ("/static", os.path.join(ROOT_DIR, "html", "static"))
    ]
    template_dir = os.path.join(ROOT_DIR, "html", "templates")

    # add extra request handlers here
    extra_handlers = [
        (r"/", IndexHandler)
    ]

    # validation strategies
    validation_strategies = [
        HeaderValidationStrategy("X-Api-Token")
    ]

    # service auto discovery
    service_registry_urls = []
    service_registry_ping_interval = 30

    # periodic tasks
    periodic_tasks = [

    ]

    # event transports
    event_transports = [
        # RabbitMqEventTransport(host="127.0.0.1", port=5672, username="root", password="root")
    ]

    # configurable framework
    skip_configuration = False
    configurables = [
        Configurable("port", type=int, mappings={"random": lambda _: random.randint(8000, 65000)}),
        Configurable("host"),
        Configurable("accessible_at"),
        Configurable("endpoint"),
        Configurable("service_registry_urls", template=lambda s: s.split(","))
    ]
    configurators = [
        CommandLineConfigurator()
    ]

    #######################
    # The exposed methods #
    #######################

    @public_method
    def hello_world(self):
        return "hello world"



def start_service():
    service = {{cookiecutter.name | capitalize}}Service()
    service.start()

if __name__ == '__main__':
    start_service()
