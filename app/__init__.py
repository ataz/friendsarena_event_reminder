from .controller import fetch_scrape_and_send

import logging

logger = logging.basicConfig(
    filename='reminder.log',
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s')
