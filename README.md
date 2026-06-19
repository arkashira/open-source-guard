<h3 align="center">🛡️ open-source-guard</h3>

<div align="center">
  <a href="https://github.com/your-org/open-source-guard/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License: MIT"></a>
  <a href="https://github.com/your-org/open-source-guard"><img src="https://img.shields.io/github/languages/top/your-org/open-source-guard?color=orange" alt="Language"></a>
  <a href="https://github.com/your-org/open-source-guard/actions"><img src="https://img.shields.io/github/workflow/status/your-org/open-source-guard/CI?label=build" alt="Build Status"></a>
  <a href="https://github.com/your-org/open-source-guard/stargazers"><img src="https://img.shields.io/github/stars/your-org/open-source-guard?style=social" alt="Stars"></a>
</div>

---

# 🚀 open-source-guard
**Protect developers and enterprises by automatically detecting risky open‑source dependencies.**  
A lightweight, language‑agnostic CLI that scans your codebase, flags vulnerable or non‑compliant licenses, and generates actionable remediation reports.

## Why open-source-guard?
- **Instant risk visibility** – Detect license violations and known CVEs in seconds, reducing audit time by up to 80 %.
- **Built for CI/CD pipelines** – Zero‑config mode works out‑of‑the‑box with GitHub Actions, GitLab CI, and Jenkins.
- **Language‑agnostic** – Works with JavaScript, Python, Go, Rust, Java, and more via a simple file‑pattern config.
- **Actionable reports** – Generates SARIF, JSON, and HTML reports that integrate with security dashboards.
- **Open‑source friendly** – Fully MIT‑licensed, community‑driven rules engine, and extensible plugin system.
- **Enterprise‑grade** – Supports custom policy bundles, SSO authentication for private registries, and audit‑ready PDFs.

## Feature Overview

| Feature | Description |
|---------|-------------|
| **Dependency Graph** | Builds a full dependency tree across multiple languages. |
| **License Scanning** | Detects GPL, AGPL, MPL, and other copyleft licenses. |
| **Vulnerability Lookup** | Queries the NVD and OSV databases in real time. |
| **Policy Engine** | Customizable rule sets (allow/deny lists, severity thresholds). |
| **Report Formats** | SARIF, JSON, HTML, and PDF for compliance teams. |
| **CI Integration** | Ready‑made GitHub Action, Docker image, and CLI flags for pipelines. |
| **Extensible Plugins** | Add support for new ecosystems via a simple plugin API. |

## Tech Stack
*The technology decisions are currently being finalized. This section will be updated once the tech‑stack lock is in place.*

## Project Structure

```
open-source-guard/
├─ business/          # Business‑logic modules (policy engine, report generators)
├─ docs/              # Documentation, design artifacts, and roadmap
└─ README.md          # This file
```

## Getting Started

> **Prerequisites**  
> - Python 3.10+ (or Docker if you prefer container execution)  
> - Git 2.30+  

```bash
# Clone the repository
git clone https://github.com/your-org/open-source-guard.git
cd open-source-guard

# (Optional) Create a virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt   # <-- will be added once the stack is locked

# Run a quick scan on the current directory
open-source-guard scan . --output report.html
```

### Running Tests

```bash
# Assuming pytest is the chosen test runner (to be confirmed)
pytest tests/
```

## Deploy

*Deployment instructions will be added once the final tech‑stack (Docker, binary releases, etc.) is locked.*

## Status
🟢 **Active development** – latest commit `398a651` adds full startup artifact suite (PRD, BMC, ROADMAP, etc.).

## Contributing
We welcome contributions! Please read our [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to propose changes, report bugs, and submit pull requests.

## License
This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.