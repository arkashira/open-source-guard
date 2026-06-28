## partner‑targets.md  
**Product:** open‑source‑guard – a lightweight project‑management layer for open‑source maintainers (scope definition, priority matrix, burnout‑guard).  
**Goal:** Accelerate adoption by plugging into the SaaS tools that maintainers already use, surface data automatically, and open revenue‑share channels for Axentx.

| # | SaaS / API | Core Use‑Case for OSS‑Guard | Free‑Tier Limits (as of 2026‑06) | Integration Effort* | Value‑Add (User Job) | Affiliate / Rev‑Share Potential |
|---|------------|----------------------------|--------------------------------|---------------------|----------------------|---------------------------------|
| 1 | **GitHub Projects (Beta) / GitHub Issues API** | Pull issue metadata, milestones, and project boards directly into OSS‑Guard’s scope canvas; auto‑sync status changes. | 2 k API calls / hour, unlimited public repo access. | **S** (OAuth, webhook subscription) | *Define scope* – map issues to “scope items” and track progress without leaving GitHub. | GitHub Marketplace revenue‑share (15 % on paid add‑ons). |
| 2 | **GitLab Issue Tracker API** | Same as GitHub but for GitLab‑hosted projects; supports self‑hosted instances via token. | 10 k requests / minute for public projects. | **S** (OAuth, webhook) | *Prioritize tasks* – import labels, weight, and due dates. | GitLab Partner Program – 10 % referral fee on paid tier upgrades. |
| 3 | **Linear API** | Pull high‑velocity issue data (sprints, cycles) for maintainers that already use Linear for road‑mapping. | 1000 requests / month free. | **M** (OAuth, webhook, data model mapping) | *Prioritize & plan* – sync Linear cycles into OSS‑Guard’s “burnout heat‑map”. | Linear’s affiliate program (20 % of first‑year subscription). |
| 4 | **Slack / Discord Bot API** | Push daily “scope health” digests, burnout alerts, and allow quick status updates via slash‑commands. | Free tier: 10 k messages / month, 1 bot per workspace. | **S** (bot token, event subscription) | *Stay aligned* – keep contributors informed without checking the UI. | No direct rev‑share, but partner co‑marketing (high PR value). |
| 5 | **OpenAI / Anthropic LLM API** | Generate automatic “scope‑definition” drafts from README or issue comments; suggest priority based on sentiment analysis. | 5 M tokens / month free (OpenAI) / 2 M (Anthropic). | **M** (API key, prompt engineering, rate‑limit handling) | *Define scope* – AI‑assisted backlog creation reduces manual triage. | Revenue‑share via usage‑based referral (5 % of spend). |
| 6 | **Sentry / Sentry.io API** | Pull error‑rate and performance alerts to feed into burnout‑risk scoring (high error spikes → higher stress). | 5 k events / month free. | **M** (OAuth, webhook) | *Prevent burnout* – surface operational pain points in the same view. | Sentry partner program – 10 % of paid plan upgrades. |
| 7 | **Calendly / Google Calendar API** | Auto‑schedule “focus‑time” blocks for maintainers based on workload heat‑map; sync with personal calendars. | 1 k events / month free. | **L** (OAuth, recurring event creation) | *Manage workload* – enforce protected time to avoid over‑commit. | Affiliate via Calendly referral (30 % of first‑month fee). |
| 8 | **GitHub Sponsors / OpenCollective API** | Show real‑time sponsorship health; tie funding levels to “burnout budget” alerts. | Unlimited public data; 100 req/min. | **S** (OAuth, webhook) | *Sustainability* – link financial support to workload caps. | Direct revenue‑share on sponsor payouts (2 % fee). |

\*Effort rating (S = Small ≈ 1 wk dev, M = Medium ≈ 2‑3 wks, L = Large ≈ 4‑6 wks).  

### Integration Roadmap (Quarterly)

| Quarter | Target(s) | Milestones | Success Metrics |
|---------|-----------|------------|-----------------|
| **Q1 2026** | GitHub Issues, Slack Bot | • OAuth flow & webhook listener <br>• Two‑way sync of issues ↔️ scope items <br>• Daily health digest in Slack | 80 % of beta users have GitHub linked; 30 % Slack adoption. |
| **Q2 2026** | GitLab, Linear | • Unified issue importer (GitHub + GitLab) <br>• Linear cycle sync & priority auto‑ranking <br>• UI toggle to select source | 50 % of GitLab‑based projects onboarded; 20 % of Linear users active. |
| **Q3 2026** | OpenAI/Anthropic LLM, Sentry | • AI‑draft scope generation (README → backlog) <br>• Burnout‑risk scoring using Sentry alerts <br>• Beta “auto‑prioritize” button | 40 % of active projects use AI draft; 25 % of users see reduced burnout alerts. |
| **Q4 2026** | Calendly, GitHub Sponsors | • Calendar block auto‑creation from workload heat‑map <br>• Sponsorship‑linked budget overlay <br>• Revenue‑share reporting dashboard | 15 % of users schedule focus blocks; 10 % of projects show sponsor‑driven budget caps. |
| **2027 H1** | Affiliate expansion & partner co‑marketing | • Formal affiliate contracts with GitHub Marketplace, Linear, Calendly <br>• Joint webinars & case studies <br>• Referral tracking UI | $150k incremental ARR from affiliate fees; 5 % conversion lift from co‑marketing. |

**Prioritisation rationale**  
1. **High adoption overlap** – GitHub/GitLab cover > 80 % of open‑source repos.  
2. **Revenue‑share density** – Linear, Calendly, and GitHub Marketplace offer the highest affiliate percentages.  
3. **Strategic lock‑in** – Slack/Discord keep the community in the loop, boosting stickiness.  
4. **Differentiation** – AI‑assisted scope definition and burnout‑risk scoring are unique value levers not present in existing Axentx tools.  

---  
*Prepared by Business‑Synthesis – Open‑Source‑Guard partner integration plan.*