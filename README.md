**🛠️ Open-Source-Guard**


<div align="center">
  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT">
  </a>
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3.10-blue.svg" alt="Python 3.10">
  </a>
  <a href="https://github.com/axentx/open-source-guard">
    <img src="https://img.shields.io/github/stars/axentx/open-source-guard.svg?style=social" alt="Stars: 0">
  </a>
</div>

---

# 🚀 Open-Source-Guard

**Power your open-source project with visibility and burnout prevention.** Open-Source-Guard is a Python CLI tool that generates a plain-text dashboard showing the health of a project's scope and its milestone status.

## Why Open-Source-Guard?

* **Real-time scope visibility**: Get a clear view of your project's open issues, PRs, and feature requests with weighted "scope-risk" scores.
* **Burnout prevention metrics**: Automate workload heat-maps per maintainer to prevent burnout.
* **Easy to use**: A simple Python CLI tool with a minimal learning curve.
* **Offline capable**: No web UI or advanced analytics required.
* **Customizable**: Define your scope and milestones in JSON files.

## Feature Overview

| Feature | Description |
| --- | --- |
| Scope Visibility | Real-time view of open issues, PRs, and feature requests with weighted "scope-risk" scores. |
| Burnout Prevention Metrics | Automated workload heat-maps per maintainer to prevent burnout. |
| Customizable Scope | Define your scope and milestones in JSON files. |
| Plain-Text Dashboard | A textual report summarising scope health and milestone progress. |

## Tech Stack

* Python

## Project Structure

* `business/`
* `docs/`
* `src/`
* `tests/`

## Getting Started

1. Install the required dependencies:
```bash
pip install poetry
```
2. Clone the repository:
```bash
git clone https://github.com/axentx/open-source-guard.git
```
3. Install the project dependencies:
```bash
poetry install
```
4. Run the tool:
```bash
poetry run src/dashboard.py
```

## Deploy

To deploy the tool, simply run the `src/dashboard.py` script.

## Status

Last updated: 2026-06-23T05:20:50.857746Z
Commit: 2ec59b6 feat(open-source-guard): real, sandbox-tested implementation

## Contributing

Please see the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines on how to contribute to this project.

## License

Open-Source-Guard is licensed under the MIT License.