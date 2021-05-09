from app import fetch_scrape_and_send

import logging

logger = logging.getLogger()


if __name__ == '__main__':
    logger.info("Starting fetch to send reminders...")
    try:
        fetch_scrape_and_send()
    except Exception as e:
        logger.exception("Unexpected error")
