import json
from dataclasses import dataclass
from datetime import datetime, timedelta

@dataclass
class Author:
    name: str
    work_hours: int
    self_care_hours: int

class BurnoutPreventionSystem:
    def __init__(self):
        self.authors = {}

    def add_author(self, author):
        self.authors[author.name] = author

    def check_burnout_risk(self, author_name):
        author = self.authors.get(author_name)
        if author:
            work_hours = author.work_hours
            self_care_hours = author.self_care_hours
            if work_hours > 40 and self_care_hours < 10:
                return True
        return False

    def set_realistic_boundaries(self, author_name, work_hours, self_care_hours):
        author = self.authors.get(author_name)
        if author:
            author.work_hours = work_hours
            author.self_care_hours = self_care_hours

    def integrate_with_calendar(self, author_name, calendar_events):
        author = self.authors.get(author_name)
        if author:
            work_hours = 0
            self_care_hours = 0
            for event in calendar_events:
                if event['type'] == 'work':
                    work_hours += event['duration']
                elif event['type'] == 'self_care':
                    self_care_hours += event['duration']
            author.work_hours = work_hours
            author.self_care_hours = self_care_hours
