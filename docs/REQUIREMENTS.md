# REQUIREMENTS.md

## Project Overview
**Open‑Source‑Guard** is an Axentx product that provides a lightweight, web‑based project‑management platform tailored for open‑source maintainers and contributors.  
Its core purpose is to help maintainers **define and manage project scope**, **prioritize tasks**, and **prevent burnout** by surfacing workload insights and encouraging sustainable contribution practices.

The system will be released as **open‑source** under the Apache‑2.0 license and will integrate with common OSS tooling (GitHub, GitLab, Gitea, Slack/Discord, and email).

---

## 1. Functional Requirements

| ID | Description |
|----|-------------|
| **FR‑1** | **User Authentication & Authorization** – Users must be able to sign‑in via OAuth (GitHub, GitLab, Google) or email/password. Role‑based access control (Owner, Maintainer, Contributor, Viewer) governs permissions on all resources. |
| **FR‑2** | **Project Import** – A maintainer can import an existing OSS repository by providing a repository URL or connecting the OAuth app. The system automatically fetches repository metadata (issues, PRs, milestones, labels, contributors). |
| **FR‑3** | **Scope Definition** – Users can create **Scope Items** (features, epics, technical debt) with attributes: title, description, estimated effort (story points), target release, and dependencies. |
| **FR‑4** | **Task Prioritization Engine** – The platform must compute a **Priority Score** for each Scope Item based on configurable factors: effort, deadline proximity, contributor availability, and community impact (e.g., stars, issue comments). Users can adjust weighting. |
| **FR‑5** | **Burnout Dashboard** – Visualize per‑contributor workload (open issues/PRs, estimated effort, recent activity) and flag contributors exceeding a configurable “burnout threshold”. |
| **FR‑6** | **Kanban Board** – Provide a drag‑and‑drop board with columns: Backlog, To‑Do, In‑Progress, Review, Done. Cards represent Scope Items or individual Issues/PRs synced from the upstream repo. |
| **FR‑7** | **Sync with Upstream** – Two‑way synchronization: changes made in Open‑Source‑Guard (e.g., status, labels) are reflected in the upstream repository via API, and vice‑versa. Conflict resolution UI must be provided. |
| **FR‑8** | **Notification System** – Send real‑time notifications (WebSocket + email/Slack webhook) for: new high‑priority items, burnout alerts, status changes, and upcoming release deadlines. |
| **FR‑9** | **Reporting & Export** – Generate PDF/CSV reports for: sprint summaries, workload distribution, and release readiness. Exportable data must include raw JSON for downstream tooling. |
| **FR‑10** | **Extensibility Plugins** – Provide a plugin interface (Node.js/TypeScript) allowing community‑built extensions (e.g., custom metrics, third‑party integrations). |
| **FR‑11** | **Audit Log** – Immutable, tamper‑evident log of all critical actions (project import, role changes, priority recalculations). Must be queryable via UI and API. |
| **FR‑12** | **Multi‑Language UI** – Support English and at least one additional language (e.g., Spanish) with i18n files; UI strings must be externalized. |
| **FR‑13** | **API** – Fully documented RESTful API (OpenAPI 3.0) covering all core features for headless usage and CI/CD integration. |
| **FR‑14** | **Installation Options** – Provide Docker‑Compose and Helm charts for self‑hosted deployment; also a one‑click deployment script for popular PaaS (Render, Fly.io). |
| **FR‑15** | **Data Privacy Controls** – Users can request deletion of personal data; the system must purge related records within 48 hours. |

---

## 2. Non‑Functional Requirements

| ID | Description |
|----|-------------|
| **NFR‑1** | **Performance** – UI page load < 2 s on a typical 3G connection; API latency ≤ 150 ms for read operations, ≤ 300 ms for write operations under 500 concurrent users. |
| **NFR‑2** | **Scalability** – System must horizontally scale to support up to 10 000 active projects and 200 000 users. Stateless services (API, WebSocket) should be container‑ready. |
| **NFR‑3** | **Security** – All external traffic must be TLS 1.3 encrypted. OAuth tokens stored using encrypted at‑rest secrets. Follow OWASP Top 10; run static analysis (Bandit, ESLint) in CI. |
| **NFR‑4** | **Reliability** – 99.9 % uptime SLA for the hosted version. Deployments must be zero‑downtime using rolling updates. |
| **NFR‑5** | **Data Consistency** – Use PostgreSQL with ACID guarantees for core data; eventual consistency is acceptable for cache layers (Redis). |
| **NFR‑6** | **Observability** – Export Prometheus metrics (request latency, error rates, sync lag). Provide Grafana dashboards and structured logs (JSON) with correlation IDs. |
| **NFR‑7** | **Backup & Disaster Recovery** – Daily automated backups of PostgreSQL and Redis; ability to restore to any point within the last 30 days. |
| **NFR‑8** | **Accessibility** – UI must meet WCAG 2.1 AA criteria (keyboard navigation, ARIA labels, color contrast). |
| **NFR‑9** | **Internationalization** – All user‑visible strings externalized; locale files must be UTF‑8. |
| **NFR‑10** | **License Compliance** – All third‑party dependencies must be compatible with Apache‑2.0. A SPDX‑SBOM must be generated for each release. |
| **NFR‑11** | **Maintainability** – Codebase must achieve ≥ 80 % test coverage (unit + integration). CI pipeline must enforce linting, type‑checking, and security scanning. |
| **NFR‑12** | **Resource Efficiency** – Docker images ≤ 200 MB; container memory limit default 256 MiB for API service, 128 MiB for worker processes. |
| **NFR‑13** | **Extensibility** – Plugin API must be versioned (semantic) and sandboxed (Node VM with limited globals). |
| **NFR‑14** | **Compliance** – GDPR‑ready: consent management UI, data export, and deletion mechanisms. |

---

## 3. Constraints

1. **Technology Stack** – Must use the Axentx‑verified frameworks where applicable:  
   - Backend: **FastAPI** (Python 3.11) with **SQLModel** for ORM.  
   - Frontend: **React 18** with **TypeScript** and **Vite**.  
   - Real‑time: **WebSocket** via **Starlette**; optional fallback to **Server‑Sent Events**.  
   - Database: **PostgreSQL 15**; caching via **Redis 7**.  
2. **Open‑Source Guard** must be released under **Apache‑2.0** and hosted in the `arkashira/open-source-guard` GitHub repo.  
3. **Deployment** – Must be container‑first; no reliance on proprietary PaaS services (except optional one‑click scripts).  
4. **Data Sources** – Only official public APIs (GitHub REST/GraphQL, GitLab API, Slack webhook, Discord API) may be used; no screen‑scraping.  
5. **Team Capacity** – Initial MVP to be delivered by a single cross‑functional squad (PM, 2 backend engineers, 2 frontend engineers, 1 QA) within 12 weeks.  

---

## 4. Assumptions

| ID | Assumption |
|----|------------|
| **A‑1** | Maintainers already have OAuth apps registered on their source‑code platforms; client IDs/secrets will be supplied during onboarding. |
| **A‑2** | Contributors will consent to workload monitoring; the burnout dashboard respects privacy settings (opt‑out per user). |
| **A‑3** | The majority of target users operate on modern browsers (Chrome ≥ 108, Firefox ≥ 107, Edge ≥ 108). |
| **A‑4** | Existing Axentx infrastructure (pgvector vector store, CI/CD pipelines) will be leveraged for model‑based priority scoring if needed. |
| **A‑5** | The open‑source community will contribute plugins; core team will provide documentation and a vetted plugin marketplace. |
| **A‑6** | Network latency to third‑party APIs is bounded (< 200 ms average) and rate‑limits are respected via exponential back‑off. |
| **A‑7** | Legal team has approved the use of user‑generated content (issues, PRs) for analytics under the repository’s open‑source license. |

---

## 5. Acceptance Criteria (Sample)

- **AC‑1**: A maintainer can import a GitHub repo, see all open issues synced, and edit their status from the Kanban board.  
- **AC‑2**: When a contributor’s estimated effort exceeds the configured burnout threshold, a red badge appears on the dashboard and an email alert is sent.  
- **AC‑3**: All API endpoints return proper HTTP status codes and conform to the OpenAPI spec; `swagger-ui` is accessible at `/api/docs`.  
- **AC‑4**: Load test (k6) shows 95th‑percentile response time ≤ 200 ms under 500 concurrent users.  
- **AC‑5**: Security scan (OWASP Dependency‑Check) reports no critical/high vulnerabilities.  

--- 

*Document version: 1.0 – 2026‑06‑19*
