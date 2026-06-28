## breakeven.md  

### 1. Cost per Active User (monthly)  

| Cost Component | Assumptions (per active user) | Monthly Cost (USD) |
|----------------|------------------------------|--------------------|
| **Compute** (2 vCPU + 4 GB RAM, auto‑scaled) | 0.05 vCPU‑hr + 0.1 GB‑hr on AWS t3.medium (≈ $0.012/vCPU‑hr, $0.0015/GB‑hr) | **$0.0015** |
| **Storage** (project metadata, issue logs, attachments) | 200 MB user‑data on S3 Standard ( $0.023/GB‑mo ) | **$0.005** |
| **Bandwidth** (API calls, web UI) | 5 GB outbound per month ( $0.09/GB ) | **$0.45** |
| **Third‑party SaaS (email, auth)** | 1,000 emails + Auth0 free tier overflow | **$0.04** |
| **Total per active user** |  | **≈ $0.50 / mo** |

> *Rounded up to $0.55 to include a 10 % safety margin for spikes and overhead.*

---

### 2. Pricing Tiers  

| Tier | Monthly Price (USD) | Core Features | Target Persona |
|------|---------------------|---------------|----------------|
| **Starter** | **$5** | • Unlimited public repo linking  <br>• Basic scope board (Kanban) <br>• 5 GB bandwidth quota <br>• Email support (24 h) | Solo maintainers / hobby projects |
| **Growth** | **$15** | • All Starter features <br>• Private repo linking <br>• Advanced prioritisation (WSJF, effort‑vs‑value) <br>• 20 GB bandwidth <br>• Slack/Discord integration <br>• Role‑based access (up to 5 members) | Small teams (2‑10 devs) |
| **Enterprise** | **$45** | • All Growth features <br>• Unlimited bandwidth <br>• Custom SLA & SSO <br>• Advanced analytics & burnout alerts <br>• Dedicated success manager <br>• Unlimited team members | Large OSS foundations / corporations |

*Assume a **gross margin** of 80 % after the $0.55 per‑user cost (i.e., 20 % of revenue goes to variable cost).*

---

### 3. Customer Acquisition Cost (CAC)  

| Channel | Cost per Lead | Conversion to Paid (%) | CAC (USD) |
|---------|---------------|------------------------|-----------|
| Content & SEO (blog, webinars) | $2 | 2 % | **$100** |
| Paid ads (dev‑focused platforms) | $5 | 1 % | **$500** |
| Community Partnerships (GitHub Sponsors, Discord) | $0 (in‑kind) | 0.5 % | **$200** |
| **Overall CAC range** | — | — | **$100 – $500** |

We will target the lower end ($150 avg) by leaning heavily on organic/community channels.

---

### 4. Lifetime Value (LTV)  

| Metric | Assumption | Calculation |
|--------|------------|-------------|
| **Average Monthly Revenue per User (ARPU)** | Weighted by tier mix (60 % Starter, 30 % Growth, 10 % Enterprise) | 0.60×$5 + 0.30×$15 + 0.10×$45 = **$9.00** |
| **Gross margin** | 80 % | $9 × 0.80 = **$7.20** |
| **Average churn** | 5 % monthly (typical SaaS churn for OSS tools) | Retention = 95 % |
| **LTV** | Gross margin × (1 / churn) | $7.20 × (1 / 0.05) = **$144** |

*Result: LTV ≈ $144, comfortably > high‑end CAC ($500) only for enterprise sales; for starter/growth CAC will be kept ≤ $100.*

---

### 5. Break‑Even Users Count  

Break‑even occurs when **Total Monthly Revenue ≥ Total Monthly Variable Cost + Fixed Overhead**.  

| Item | Amount |
|------|--------|
| **Fixed Overhead** (core team salaries, office, tooling) | **$12,000 / mo** |
| **Variable cost per user** | $0.55 |
| **Revenue needed to cover overhead** | $12,000 / 0.80 (gross margin) = **$15,000** |
| **Required ARPU** (overall) | $9 (see above) |
| **Break‑even users** | $15,000 ÷ $9 ≈ **1,667 active paying users** |

*If the tier mix shifts toward higher‑priced tiers, the required user count drops proportionally (e.g., 100 % Enterprise → 333 users).*

---

### 6. Path to $10 K MRR  

| Tier Mix (assumed) | Users Needed | Monthly Revenue |
|--------------------|--------------|-----------------|
| **All Starter** | 2,000 × $5 = **$10,000** | 2,000 users |
| **Mixed (60 % Starter, 30 % Growth, 10 % Enterprise)** | 1,667 total (see break‑even) → 1,000 S + 500 G + 167 E = **$10,005** | 1,667 users |
| **Enterprise‑focused** (30 % Growth, 70 % Enterprise) | 222 G + 156 E = **$10,020** | 378 users |

**Strategic recommendation:**  
1. **Launch with a free “core” tier** to capture community users → convert 5 % to Starter within 30 days.  
2. **Run quarterly “growth sprints”** (webinars, hackathons) to push a portion of Starter users to Growth (conversion 10 %).  
3. **Target foundations & large OSS projects** via direct outreach to sell Enterprise licenses (average 2‑3 Enterprise per quarter).  

Achieving **≈ 1,700 paying users** (mixed tier) will simultaneously cover costs and generate **$10 K + MRR**, positioning the product for the next scaling milestone (>$50 K MRR).