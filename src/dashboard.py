import json
from dataclasses import dataclass
from typing import List
import argparse
import os

@dataclass
class Milestone:
    title: str
    completed: bool

@dataclass
class Scope:
    title: str
    covered: bool

def load_scope_document(file_path: str) -> List[Scope]:
    with open(file_path, 'r') as file:
        data = json.load(file)
    return [Scope(title=item['title'], covered=item['covered']) for item in data]

def load_milestones(file_path: str) -> List[Milestone]:
    with open(file_path, 'r') as file:
        data = json.load(file)
    return [Milestone(title=item['title'], completed=item['completed']) for item in data]

def generate_dashboard(scope: List[Scope], milestones: List[Milestone]) -> str:
    scope_coverage = sum(1 for item in scope if item.covered) / len(scope) * 100 if scope else 0
    milestone_completion = sum(1 for item in milestones if item.completed) / len(milestones) * 100 if milestones else 0
    return f'Scope coverage: {scope_coverage:.2f}%\nMilestone completion: {milestone_completion:.2f}%'

def save_dashboard(dashboard: str, output_file: str) -> None:
    with open(output_file, 'w') as file:
        file.write(dashboard)

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--scope', help='Path to scope document')
    parser.add_argument('--milestones', help='Path to milestones document')
    parser.add_argument('--output', help='Path to output file')
    args = parser.parse_args()
    scope = load_scope_document(args.scope)
    milestones = load_milestones(args.milestones)
    dashboard = generate_dashboard(scope, milestones)
    save_dashboard(dashboard, args.output)

if __name__ == '__main__':
    main()
