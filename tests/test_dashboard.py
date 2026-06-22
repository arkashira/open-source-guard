from src.dashboard import load_scope_document, load_milestones, generate_dashboard, save_dashboard
import json
import os
import pytest

def test_load_scope_document():
    scope_data = '[{"title": "Scope 1", "covered": true}, {"title": "Scope 2", "covered": false}]'
    with open('scope.json', 'w') as file:
        file.write(scope_data)
    scope = load_scope_document('scope.json')
    assert len(scope) == 2
    assert scope[0].title == 'Scope 1'
    assert scope[0].covered
    assert not scope[1].covered
    os.remove('scope.json')

def test_load_milestones():
    milestones_data = '[{"title": "Milestone 1", "completed": true}, {"title": "Milestone 2", "completed": false}]'
    with open('milestones.json', 'w') as file:
        file.write(milestones_data)
    milestones = load_milestones('milestones.json')
    assert len(milestones) == 2
    assert milestones[0].title == 'Milestone 1'
    assert milestones[0].completed
    assert not milestones[1].completed
    os.remove('milestones.json')

def test_generate_dashboard():
    scope = [type('Scope', (object,), {'title': 'Scope 1', 'covered': True})()]
    milestones = [type('Milestone', (object,), {'title': 'Milestone 1', 'completed': True})()]
    dashboard = generate_dashboard(scope, milestones)
    assert 'Scope coverage: 100.00%' in dashboard
    assert 'Milestone completion: 100.00%' in dashboard

def test_save_dashboard(tmp_path):
    dashboard = 'Scope coverage: 100.00%\nMilestone completion: 100.00%'
    output_file = tmp_path / 'dashboard.txt'
    save_dashboard(dashboard, str(output_file))
    with open(output_file, 'r') as file:
        assert file.read() == dashboard

def test_main(tmp_path, monkeypatch):
    scope_data = '[{"title": "Scope 1", "covered": true}]'
    milestones_data = '[{"title": "Milestone 1", "completed": true}]'
    with open(tmp_path / 'scope.json', 'w') as file:
        file.write(scope_data)
    with open(tmp_path / 'milestones.json', 'w') as file:
        file.write(milestones_data)
    output_file = tmp_path / 'dashboard.txt'
    monkeypatch.setattr('sys.argv', ['main.py', '--scope', str(tmp_path / 'scope.json'), '--milestones', str(tmp_path / 'milestones.json'), '--output', str(output_file)])
    from src.dashboard import main
    main()
    with open(output_file, 'r') as file:
        content = file.read()
    assert 'Scope coverage: 100.00%' in content
    assert 'Milestone completion: 100.00%' in content
