import logging
from fast_API_base import app
from animal_methods.the_zoo import get_enclosure
from user_methods import read_user, read_user_me

logger = logging.getLogger()