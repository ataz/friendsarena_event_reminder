from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Tuple

import requests
from bs4 import BeautifulSoup

from app.constants import MONTH_MAP


@dataclass
class Event:
    date: datetime.date
    title: str

    def is_tomorrow(self):
        return (datetime.now() + timedelta(days=1)).date() == self.date


def create_event(event: list) -> Event:
    day, month, year, title, *_ = event
    event_date = datetime(int(year), MONTH_MAP[month.lower()], day=int(day)).date()
    return Event(event_date, title)


def scrape() -> Tuple[Event]:
    response = requests.get(
        'http://www.friendsarena.se/evenemang',
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT x.y; rv:10.0) Gecko/20100101 Firefox/10.0'
        }
    )
    soup = BeautifulSoup(response.content, 'html.parser')
    all_raw_events = []
    for raw_event in soup.find_all("div", {"class": "info clearfix"}):
        all_raw_events.append([t.strip() for t in raw_event.strings if t and t.strip()])

    processed_events = []
    for raw_event in all_raw_events:
        if raw_event[2] == '-' or raw_event[1] == '-':
            pass
        else:
            created_event = create_event(raw_event)
            processed_events.append(created_event)

    return tuple(processed_events)
