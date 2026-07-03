# 📊 Institutional Risk & Client Engagement Platform
### *Strategic Retention Management Dashboard • Unified Mentor Hub (ECB Framework)*

An institutional-grade **Streamlit** data analytics dashboard engineered to shift retail banking retention strategy from static demographic features to dynamic, behavior-driven client utilization analytics.

---

## 📖 Project Overview & Business Context
Traditional banking risk frameworks often focus purely on absolute asset values or credit worthiness, creating a false sense of security. Many clients with high net worth silently drift away long before explicit account closure due to operational friction or forced cross-selling. 

This platform uses predictive customer metrics like the **Relationship Strength Index (RSI)** to continuously track account behavior. It uncovers underlying retention trends, identifies premium accounts facing structural **Silent Churn**, and delivers clear, actionable insights to optimize portfolio stability.

---

## 🧬 Core Analytical Architecture

1. **The Product Saturation Paradox:** Empirical data shows a non-linear relationship between retention and product depth. While single-product users are highly vulnerable to attrition, the optimal stability zone is exactly **2 products** (the target sweet spot). Beyond this, holding **3 or 4 products triggers a sharp, exponential spike in churn** caused by administrative clutter and operational friction.
2. **The Engagement Variance Gap:** High asset concentrations ($>100,000) do not guarantee structural loyalty. Inactive high-balance accounts are highly volatile liabilities that can shift capital rapidly when competitor yields fluctuate.

---

## 🚀 Key Platform Features

- **Interactive Metric Blocks (KPIs):** Custom-styled HTML/CSS component containers presenting *Global Defection Rate, Engagement Variance Risk Gaps, Optimal Product Benchmarks,* and *Premium Silent Churn Rates*.
- **Dynamic Exploration Panels:** Granular multiselect matrix filtering across Geography (France, Germany, Spain), Salary Range Sliders, and custom Asset Liquidity Floors.
- **Advanced Plotly Interfaces:** - *Cohort Deconstruction Matrix:* Dynamic horizontal bar visualization tracking churn behavior by tailored engagement profiles.
  - *Product Saturation Elasticity Curve:* Predictive regression visualization mapping non-linear product utility trends.
- **Early-Warning Registry:** A real-time data-grid engine with targeted toast alerts tracking high-yield dormant accounts for proactive outreach.

---

## 🛠️ Technology Stack

- **Language:** Python 3.10+
- **Frontend Dashboard App:** Streamlit
- **Data Engineering:** Pandas, NumPy
- **Interactive Visualizations:** Plotly Express, Plotly Graph Objects

---

## 💻 Technical Setup & Local Deployment

### 1. Clone the Repository
```bash
git clone [https://github.com/your-username/banking-retention-analytics.git](https://github.com/your-username/banking-retention-analytics.git)
cd banking-retention-analytics
