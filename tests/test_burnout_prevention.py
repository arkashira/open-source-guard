from burnout_prevention import BurnoutPreventionSystem, Author

def test_check_burnout_risk():
    system = BurnoutPreventionSystem()
    author = Author('John', 50, 5)
    system.add_author(author)
    assert system.check_burnout_risk('John') == True

def test_check_burnout_risk_no_risk():
    system = BurnoutPreventionSystem()
    author = Author('John', 30, 15)
    system.add_author(author)
    assert system.check_burnout_risk('John') == False

def test_set_realistic_boundaries():
    system = BurnoutPreventionSystem()
    author = Author('John', 50, 5)
    system.add_author(author)
    system.set_realistic_boundaries('John', 40, 10)
    assert system.authors['John'].work_hours == 40
    assert system.authors['John'].self_care_hours == 10

def test_integrate_with_calendar():
    system = BurnoutPreventionSystem()
    author = Author('John', 0, 0)
    system.add_author(author)
    calendar_events = [
        {'type': 'work', 'duration': 8},
        {'type': 'self_care', 'duration': 2},
        {'type': 'work', 'duration': 4},
    ]
    system.integrate_with_calendar('John', calendar_events)
    assert system.authors['John'].work_hours == 12
    assert system.authors['John'].self_care_hours == 2
