import logging

from app.constants import reminder_receivers
from app.gmail import send_email
from app.scraper import scrape

logger = logging.getLogger()


def _generate_email_body(event, all_events):
    body = \
f"""https://www.friendsarena.se/evenemang

Event tomorrow at Friends Arena on {event.date}: {event.title}.

Current schedule for Friends:
"""
    for event in all_events:
        body += f"{event.date}: {event.title}\n"
    
    return body


def fetch_scrape_and_send():
    events = scrape()
    for event in events:
        if not event.is_tomorrow():
            continue
        for receiver in reminder_receivers:
            result = send_email(
                receiver,
                f"Event tomorrow at Friends on {event.date.isoformat()}: {event.title}",
                _generate_email_body(event, events)
            )
            if result:
                logger.info(f"Successfully sent email for upcoming event to {receiver}")
        break
    else:
        logger.info("No upcoming event tomorrow...")
