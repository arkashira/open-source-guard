# Business Model Canvas – open-source-guard
**Product:** open-source-guard – a lightweight, open‑source‑friendly project‑management platform that helps maintainers define scope, prioritize work, and protect developer wellbeing.

---

## 1. Value Proposition
| What we deliver | Why it matters |
|-----------------|----------------|
| **Scope‑definition wizard** – guided templates for road‑maps, release criteria, and contribution guidelines. | Reduces ambiguity, accelerates onboarding of new contributors. |
| **Priority matrix & burn‑down charts** – visual tools to rank issues/PRs by impact, effort, and risk. | Enables data‑driven triage, keeping the most valuable work visible. |
| **Burnout guard** – automated alerts when maintainers exceed configurable workload thresholds (issue count, PR review time, commit frequency). | Improves maintainer health, lowers turnover, and sustains project momentum. |
| **Seamless integration** – native plugins for GitHub, GitLab, and Gitea; syncs issues, PRs, milestones, and CI status. | No friction switching from existing tooling; data stays in the familiar VCS ecosystem. |
| **Open‑source licensing & self‑hosted option** – MIT‑licensed core, optional SaaS hosted service. | Aligns with community values while offering a managed path for larger projects. |

---

## 2. Customer Segments
| Primary | Secondary |
|---------|-----------|
| **Open‑source maintainers** (core teams of libraries, frameworks, tooling) | **Small‑to‑medium SaaS startups** that rely on open‑source components and need transparent internal tracking. |
| **Community managers** who coordinate contributors across time zones | **Enterprise open‑source programs** (e.g., Linux Foundation, CNCF) seeking governance dashboards. |
| **Individual contributors** looking for clear task ownership | **Education & research groups** using open‑source projects for collaborative development. |

---

## 3. Channels
| Channel | Description |
|---------|-------------|
| **GitHub Marketplace / GitLab Marketplace** – one‑click install of the open‑source‑guard app. |
| **Official website (open-source-guard.dev)** – documentation, demo videos, community forum (Discourse). |
| **Developer conferences & meet‑ups** – workshops, sponsorship of open‑source sprints. |
| **Content marketing** – blog posts, case studies, newsletters (via Substack). |
| **Partner integrations** – bundled with CI/CD platforms (e.g., CircleCI, GitHub Actions) and IDE extensions (VS Code). |
| **Open‑source community channels** – Reddit r/opensource, Hacker News, Twitter/X, Discord server. |

---

## 4. Revenue Streams
| Stream | Model | Pricing |
|--------|-------|---------|
| **Hosted SaaS** (open‑source‑guard.io) – fully managed, high‑availability service. | Tiered subscription (Free tier up to 5 repos, Pro $29/mo, Team $79/mo, Enterprise custom). |
| **Premium plugins & analytics** – advanced reporting, custom alerting, SSO integration. | Add‑on pricing $9–$49 per month. |
| **Support & consulting** – SLA‑backed issue triage, migration assistance, custom workflow engineering. | Hourly $150/hr or retainer packages (e.g., $2,500/quarter). |
| **Marketplace revenue share** – optional paid extensions built by third‑party developers (15 % platform cut). |
| **Training & certification** – official “Open‑Source Guard Practitioner” program. | Course fees $199–$499 per participant. |

*The core product remains free and MIT‑licensed; revenue is generated from value‑added services.*

---

## 5. Cost Structure
| Category | Typical Cost |
|----------|--------------|
| **Cloud infrastructure** – hosting SaaS (K8s clusters, DB, CDN). |
| **Development & maintenance** – salaries for core engineers, QA, UX designers. |
| **Open‑source community fund** – bounties, hackathon prizes, contributor stipends. |
| **Marketing & sales** – content creation, conference sponsorships, ad spend. |
| **Legal & compliance** – licensing audit, GDPR/CCPA compliance for hosted service. |
| **Tooling & CI/CD** – CI pipelines, monitoring (Datadog, Sentry). |
| **Partner commissions** – revenue share payouts to third‑party plugin creators. |

---

## 6. Key Resources
| Resource | Role |
|----------|------|
| **Codebase (MIT‑licensed)** – core UI, API, and integration adapters. |
| **PGVector knowledge store** – embeddings of project‑management best practices used for smart suggestions. |
| **Community contributors** – maintainers, reviewers, documentation writers. |
| **Infrastructure stack** – Kubernetes, PostgreSQL, Redis, vLLM for AI‑driven prioritization. |
| **Brand & community assets** – website, docs site, Discord/Discourse servers. |
| **Data pipelines** – ingestion of issue/PR metadata from Git platforms for analytics. |

---

## 7. Key Activities
| Activity | Frequency |
|----------|-----------|
| **Core development** – feature sprints, bug triage, security patches. |
| **AI model updates** – fine‑tune prioritization models using the company’s 18 M+ training pairs. |
| **Community engagement** – PR reviews, AMA sessions, contributor onboarding. |
| **Integration maintenance** – keep plugins compatible with GitHub/GitLab API changes. |
| **Performance & reliability ops** – monitoring, scaling, incident response for SaaS. |
| **Sales & partnership outreach** – onboarding new enterprise partners, co‑marketing. |
| **Compliance audits** – periodic security and licensing checks. |

---

## 8. Key Partners
| Partner | Contribution |
|---------|--------------|
| **GitHub, GitLab, Gitea** – API access, marketplace distribution. |
| **CI/CD providers** (CircleCI, GitHub Actions) – native action templates for guard checks. |
| **AI framework maintainers** (vLLM, SGLang) – high‑throughput inference for priority scoring. |
| **Open‑source foundations** (Linux Foundation, CNCF) – endorsement, joint events, funding. |
| **Cloud providers** (AWS, GCP, Azure) – credits for hosted SaaS, compliance certifications. |
| **Third‑party plugin developers** – ecosystem extensions (e.g., security audit bots). |
| **Educational institutions** – pilot programs for student projects, research collaborations. |

---

### Summary
open-source-guard leverages Axentx’s existing data assets and AI inference stack to deliver a purpose‑built, community‑centric project‑management solution. By keeping the core free and open‑source while monetizing managed hosting, premium analytics, and professional services, we create a sustainable revenue stream that scales with the health of the open‑source ecosystem we serve.
