**user-stories.md**

---

## Epic 1 – Project Scope Definition & Visibility  

| # | User Story | Acceptance Criteria | Complexity |
|---|------------|----------------------|------------|
| 1 | **As a project maintainer, I want to create a formal “Scope Charter” for each release, so that contributors clearly understand the boundaries and goals of the work.** | - A wizard guides the maintainer through title, objectives, out‑of‑scope items, and success metrics.<br>- The charter is version‑controlled and displayed on the repo’s README and a dedicated dashboard page.<br>- Contributors can view the charter without authentication, but only maintainers can edit.<br>- Changes to the charter generate a changelog entry and optional Slack/Discord notification.<br>- The charter can be linked to GitHub milestones. | M |
| 2 | **As a contributor, I want to see a visual “Scope Heatmap” that highlights which areas of the codebase are in‑scope, out‑of‑scope, or under‑review, so that I can focus my effort where it matters most.** | - Heatmap is generated from the Scope Charter and current issue labels.<br>- Colors: green (in‑scope), gray (out‑of‑scope), orange (under review).<br>- Hovering a module shows a tooltip with related issues and PRs.<br>- Heatmap updates automatically on charter or label changes.<br>- Accessible via a static HTML page that can be embedded in the repo wiki. | S |
| 3 | **As a release manager, I want to lock the Scope Charter for a given milestone, so that no new out‑of‑scope work can be added after the freeze date.** | - A “freeze” toggle sets the charter to read‑only for the milestone.<br>- Attempted edits after freeze show a warning and require maintainer override.<br>- Freeze status is displayed prominently on the dashboard and in CI checks.<br>- Freeze date can be configured per milestone.<br>- Audit log records who attempted edits and when. | M |

---

## Epic 2 – Prioritization & Decision Framework  

| # | User Story | Acceptance Criteria | Complexity |
|---|------------|----------------------|------------|
| 4 | **As a maintainer, I want to assign a weighted priority score (impact × effort × risk) to each issue, so that the team can objectively rank work items.** | - UI fields for impact (1‑5), effort (1‑5), risk (1‑5).<br>- Composite score = impact × (5‑effort) × (5‑risk).<br>- Issues are automatically sorted by score on the backlog view.<br>- Scores are stored in issue metadata and exported to CSV.<br>- Score recalculates in real‑time as fields change. | S |
| 5 | **As a contributor, I want a “Decision Log” that records why a particular issue was accepted, deferred, or rejected, so that future contributors understand the rationale.** | - When a maintainer changes an issue’s status, a mandatory comment template appears (reason, data points, stakeholder).<br>- The comment is stored in a dedicated “Decision Log” tab linked to the issue.<br>- The log is searchable by keyword, date, and author.<br>- Exportable as markdown for release notes.<br>- Permissions: anyone can view; only maintainers can edit. | S |
| 6 | **As a product owner, I want to run a “What‑If” simulation that temporarily re‑weights priorities (e.g., increase impact for security bugs), so that we can explore alternative roadmaps without affecting the live backlog.** | - A sandbox mode lets the owner adjust weighting formulas.<br>- Simulation results are displayed in a separate “What‑If” view with side‑by‑side comparison to the current backlog.<br>- Changes are not persisted to the main issue data.<br>- Ability to export the simulated roadmap as PDF/PNG.<br>- Sandbox sessions are saved per user for later review. | L |

---

## Epic 3 – Burnout Prevention & Work‑load Balancing  

| # | User Story | Acceptance Criteria | Complexity |
|---|------------|----------------------|------------|
| 7 | **As a contributor, I want to see my personal “Workload Dashboard” that aggregates my assigned issues, estimated effort, and recent activity, so that I can self‑manage capacity.** | - Dashboard lists open issues with effort score and due dates.<br>- Shows weekly effort total and a “capacity gauge” (green/yellow/red) based on a configurable threshold.<br>- Highlights any issues that have been open > X days without activity.<br>- Provides a “request reassignment” button that creates a templated comment. | S |
| 8 | **As a maintainer, I want to receive automated “Burnout Alerts” when a contributor’s cumulative effort exceeds a configurable limit, so that I can intervene early.** | - System aggregates effort scores per contributor over a rolling 2‑week window.<br>- Thresholds (e.g., > 30 effort points) trigger an email/Slack notification to the maintainer and the contributor.<br>- Alert includes a list of high‑effort issues and suggested actions (reassign, split, defer).<br>- Alerts can be muted per contributor for a defined period.<br>- Historical alerts are stored for audit. | M |
| 9 | **As a release manager, I want to enforce a “Maximum Concurrent Issues” rule per contributor, so that no one is overloaded during a sprint.** | - Configurable limit (default 3 active issues).<br>- When a maintainer tries to assign a fourth issue, the UI blocks the action and shows a warning with current assignments.<br>- Option to override with justification, which is logged.<br>- Rule status displayed on the release board header.<br>- Overrides are reported in the weekly release metrics. | M |
| 10 | **As a community manager, I want to generate a “Well‑Being Report” that visualizes overall team effort distribution, overdue tasks, and burnout alerts, so that I can present health metrics to stakeholders.** | - Report includes bar charts of effort per contributor, heatmap of overdue issues, and count of active burnout alerts.<br>- Exportable as PDF and markdown.<br>- Can be scheduled to run weekly and posted to a Discord channel.<br>- Data source is the same as the workload dashboard, ensuring consistency.<br>- Report respects privacy settings (e.g., anonymize names if required). | L |

---

## Epic 4 – Integration & Automation  

| # | User Story | Acceptance Criteria | Complexity |
|---|------------|----------------------|------------|
| 11 | **As a maintainer, I want the tool to sync automatically with GitHub Issues/PRs, so that no duplicate data entry is required.** | - Bi‑directional sync: updates in Open‑Source‑Guard reflect on GitHub and vice‑versa.<br>- Supports label mapping, milestone linking, and assignee sync.<br‑| S |
| 12 | **As a CI/CD engineer, I want a pre‑merge gate that checks whether a PR touches any out‑of‑scope files, and fails the build if it does, so that scope creep is caught early.** | - Gate reads the current Scope Charter and generates a file‑level whitelist.<br>- If a PR modifies a non‑whitelisted path, the CI job fails with a clear error message and a link to the charter.<br>- Gate can be disabled per branch via a config flag.<br>- Results are posted as a status check on GitHub. | M |

---  

*All stories are written in Connextra format, grouped by logical epics, include 3‑5 acceptance criteria, and are sized for sprint planning (S = ~2 days, M = ~5 days, L = ~10 days).*