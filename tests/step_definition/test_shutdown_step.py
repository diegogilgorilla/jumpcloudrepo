from pytest_bdd import given, when, then, scenarios, parsers
from tests.utils.utils import Utils
import requests
import time


scenarios('../features/shutdown.feature')


@given('I call POST shutdown service')
def application_put_status_response(get_data):
    url = get_data['url'].format('hash')
    get_data['request'] = requests.post(url, data='shutdown')
