
# pylint: disable=odoo-addons-relative-import
# we are testing, we want to test as we were an external consumer of the API
from odoo.addons.queue_job.jobrunner import channels

from .common import load_doctests

load_tests = load_doctests(channels)
