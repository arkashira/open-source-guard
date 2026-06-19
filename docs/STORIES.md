# STORIES.md  

## Project: open-source-guard  
**Goal:** Deliver a lightweight, open‑source‑friendly project‑management tool that enables maintainers and contributors to define scope, prioritize work, and protect their wellbeing.  

---  

## Epics & Backlog  

| Epic | Description | MVP Priority |
|------|-------------|--------------|
| **E1 – Project Definition & Scope** | Core data model and UI for creating a project, setting boundaries, and documenting high‑level goals. | ✅ |
| **E2 – Task Lifecycle** | Create, edit, prioritize, and track tasks (issues, features, chores). | ✅ |
| **E3 – Burnout Guard** | Automated workload monitoring and personal‑wellness nudges. | ✅ |
| **E4 – Collaboration & Permissions** | Role‑based access, contributor onboarding, and review workflow. | ✅ |
| **E5 – Integration & Export** | Sync with GitHub/GitLab, import/export data, and generate reports. | ✅ |
| **E6 – Dashboard & Analytics** | Visual overview of project health, velocity, and risk indicators. | ✅ |
| **E7 – Extensibility** | Plugin system and API for community extensions. | ✅ |
| **E8 – Documentation & Onboarding** | In‑app tutorials, help center, and contribution guide. | ✅ |

---  

## User Stories  

### Epic E1 – Project Definition & Scope  

| # | Story | Acceptance Criteria |
|---|-------|----------------------|
| **E1‑01** | **As a maintainer, I want to create a new project workspace, so that I can start tracking its scope.** | • “New Project” button opens a modal.<br>• Required fields: Project name, short description, repository URL.<br>• Optional: Tags, start date, target release date.<br>• Project appears in the workspace list after saving.<br>• Data persisted in local DB (`projects` table). |
| **E1‑02** | **As a maintainer, I want to define high‑level objectives and constraints, so that contributors understand the project’s purpose.** | • Editable “Objectives” section with rich‑text editor.<br>• Ability to add “Scope Constraints” (e.g., “No breaking API changes”).<br>• Changes are versioned (last‑edited timestamp, author). |
| **E1‑03** | **As a contributor, I want to view the project’s defined scope, so that I can assess whether my work fits.** | • Public “Scope” page displays objectives and constraints.<br>• Read‑only for users without edit permission.<br>• Link to scope from the main navigation. |

### Epic E2 – Task Lifecycle  

| # | Story | Acceptance Criteria |
|---|-------|----------------------|
| **E2‑01** | **As a maintainer, I want to create a task with priority and type, so that work can be organized.** | • “New Task” form with fields: Title, description, type (feature/bug/chore), priority (P0‑P3), estimate (hours).<br>• Validation of required fields.<br>• Task appears in the project’s task board. |
| **E2‑02** | **As a contributor, I want to claim a task, so that I can start working on it.** | • “Claim” button on each task (visible to contributors).<br>• Claim assigns the current user as `owner` and changes task status to *In Progress*.<br>• Owner can un‑claim or transfer ownership. |
| **E2‑03** | **As any user, I want to move tasks across columns (Backlog → In Progress → Review → Done), so that the workflow is visual.** | • Kanban board with draggable columns.<br>• State transition rules enforced (e.g., cannot move to *Done* without a review). |
| **E2‑04** | **As a maintainer, I want to add labels and milestones to tasks, so that I can group work for releases.** | • UI to attach existing labels or create new ones.<br>• Milestone selector that links to a release version. |
| **E2‑05** | **As a reviewer, I want to mark a task as “Ready for Review”, so that it triggers a review workflow.** | • “Ready for Review” button sets status to *Review* and notifies users with the *Reviewer* role. |

### Epic E3 – Burnout Guard  

| # | Story | Acceptance Criteria |
|---|-------|----------------------|
| **E3‑01** | **As a contributor, I want to set a weekly work‑hour limit, so that the system can warn me when I exceed it.** | • Settings page with “Weekly hour budget” (default 20h).<br>• System tracks logged time per task (manual entry).<br>• When cumulative hours > 90 % of budget, a non‑intrusive banner appears. |
| **E3‑02** | **As a maintainer, I want to see a “Burnout Risk” indicator for each contributor, so that I can intervene early.** | • Risk score calculated from hours logged, number of active tasks, and recent task churn.<br>• Color‑coded badge (Green/Yellow/Red) shown on contributor profile. |
| **E3‑03** | **As a contributor, I want periodic “well‑being” prompts, so that I can reflect on workload.** | • Configurable prompt frequency (e.g., every 3 days).<br>• Simple questionnaire (stress level 1‑5, optional comment).<br>• Responses stored for analytics (anonymous aggregate view). |

### Epic E4 – Collaboration & Permissions  

| # | Story | Acceptance Criteria |
|---|-------|----------------------|
| **E4‑01** | **As a maintainer, I want to invite users with specific roles (Contributor, Reviewer, Admin), so that access is controlled.** | • Invite dialog with email/username and role dropdown.<br>• Invitation email with token link.<br>• Role stored in `project_members` table. |
| **E4‑02** | **As a reviewer, I want to approve or request changes on a task, so that quality gates are enforced.** | • Review modal with “Approve” and “Request Changes” actions.<br>• Approve moves task to *Done*; Request Changes moves back to *In Progress* with comment. |
| **E4‑03** | **As a contributor, I want to comment on tasks, so that I can discuss implementation details.** | • Threaded comment UI with markdown support.<br>• Mentions (`@username`) trigger email notifications. |

### Epic E5 – Integration & Export  

| # | Story | Acceptance Criteria |
|---|-------|----------------------|
| **E5‑01** | **As a maintainer, I want to link a GitHub repository, so that issues can be synced automatically.** | • OAuth connection to GitHub.<br>• One‑way sync: GitHub issues → open‑source‑guard tasks (matching by title/label).<br>• Sync status indicator. |
| **E5‑02** | **As a maintainer, I want to export the current backlog as CSV, so that I can share it with external stakeholders.** | • “Export CSV” button generates file with columns: ID, Title, Type, Priority, Status, Owner, Estimate. |
| **E5‑03** | **As a contributor, I want to import tasks from a CSV template, so that bulk onboarding is fast.** | • CSV upload validates required columns and creates tasks in *Backlog* status. |
| **E5‑04** | **As a maintainer, I want a REST API endpoint to fetch project metrics, so that I can build custom dashboards.** | • `GET /api/v1/projects/{id}/metrics` returns JSON with task counts, velocity, burnout scores. Authentication via JWT. |

### Epic E6 – Dashboard & Analytics  

| # | Story | Acceptance Criteria |
|---|-------|----------------------|
| **E6‑01** | **As a maintainer, I want a project overview dashboard, so that I can quickly assess health.** | • Charts: Open tasks by priority, burndown chart for current sprint, burnout risk distribution.<br>• Refreshes automatically every 5 minutes. |
| **E6‑02** | **As a contributor, I want to see my personal workload chart, so that I can balance effort.** | • Line chart of hours logged per week for the last 8 weeks.<br>• Highlight when approaching weekly limit. |
| **E6‑03** | **As a reviewer, I want a “Review Queue” widget, so that I can pick the next task to review.** | • List of tasks with status *Review*, sorted by priority and age.<br>• One‑click “Open Review” action. |

### Epic E7 – Extensibility  

| # | Story | Acceptance Criteria |
|---|-------|----------------------|
| **E7‑01** | **As a developer, I want a plugin hook for custom task fields, so that projects can capture domain‑specific data.** | • Plugin manifest (`plugin.json`) can declare new fields (type, validation).<br>• UI renders additional fields on the task form when plugin is enabled. |
| **E7‑02** | **As a maintainer, I want to enable/disable plugins per project, so that only needed extensions run.** | • Project settings page lists installed plugins with toggle switches.<br>• Disabled plugins do not affect DB schema or UI. |
| **E7‑03** | **As an integrator, I want webhook support for task events, so that external tools can react in real time.** | • Configurable webhook URL per project.<br>• Payload sent on task creation, status change, and burnout alerts. |

### Epic E8 – Documentation & Onboarding  

| # | Story | Acceptance Criteria |
|---|-------|----------------------|
| **E8‑01** | **As a new user, I want an interactive walkthrough, so that I can start using the tool without reading docs.** | • Step‑by‑step guide that highlights UI elements (Create Project → Add Task → Claim Task).<br>• Ability to skip or replay the tour. |
| **E8‑02** | **As a contributor, I want a searchable help center, so that I can find answers to common questions.** | • Help articles stored in Markdown, indexed for full‑text search.<br>• Search bar returns relevance‑sorted results. |
| **E8‑03** | **As a maintainer, I want a contribution guide in the repo, so that external developers can submit plugins or bug fixes.** | • `CONTRIBUTING.md` with sections: code style, testing, plugin API, release process.<br>• CI checks enforce linting and unit test coverage ≥ 80 %. |

---  

## MVP Ordering (Top‑Down)  

1. **E1‑01, E1‑02, E1‑03** – Project creation & scope definition.  
2. **E2‑01, E2‑02, E2‑03, E2‑04, E2‑05** – Full task lifecycle & Kanban board.  
3. **E3‑01, E3‑02, E3‑03** – Burnout Guard core features.  
4. **E4‑01, E4‑02, E4‑03** – Role‑based collaboration.  
5. **E5‑01, E5‑02** – GitHub sync & CSV export (critical for open‑source adoption).  
6. **E6‑01, E6‑02** – Dashboard analytics for maintainers & contributors.  
7. **E8‑01, E8‑02** – Onboarding & help center to reduce friction.  
8. **E5‑03, E5‑04, E7‑01‑E7‑03, E8‑03** – Extensibility, advanced integrations, and contribution docs (post‑MVP).  

---  

*All stories are written to be independently testable, shippable, and aligned with the validated need of open‑source maintainers to manage scope while protecting contributor wellbeing.*
