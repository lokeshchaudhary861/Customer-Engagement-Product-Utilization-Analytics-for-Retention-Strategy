import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# 1. PAGE CONFIGURATION & THEME SETUP
st.set_page_config(
    page_title="Executive Retention & Utilization Analytics",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Perfect Borders, Professional Padding & Container Aesthetics
st.markdown("""
    <style>
        /* Global Background styling tweak */
        .reportview-container {
            background: #f8f9fa;
        }
        /* Custom Executive Card styling with perfect borders */
        .kpi-card {
            background-color: #ffffff;
            border: 1px solid #e0e6ed;
            border-radius: 8px;
            padding: 20px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
            margin-bottom: 15px;
            transition: all 0.3s ease-in-out;
        }
        .kpi-card:hover {
            border-color: #4A90E2;
            box-shadow: 0 6px 12px rgba(74, 144, 226, 0.15);
        }
        .kpi-title {
            font-size: 14px;
            color: #6c757d;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        .kpi-value {
            font-size: 28px;
            color: #1a252c;
            font-weight: 700;
            margin-top: 5px;
        }
        .kpi-subtitle {
            font-size: 12px;
            color: #28a745;
            margin-top: 5px;
            font-weight: 500;
        }
        .kpi-subtitle.danger {
            color: #dc3545;
        }
        /* Chart container panels */
        .chart-container {
            background-color: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 10px;
            padding: 15px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.02);
        }
    </style>
""", unsafe_allow_html=True)

# 2. OPTIMIZED DATA PIPELINE
@st.cache_data
def load_and_analyze_bank_data():
    # Ingesting the verbatim dataset
    df = pd.read_csv("European_Bank.csv")
    
    # Mathematical Framework for Engagement Classification
    def classify_behavior(row):
        if row['IsActiveMember'] == 1 and row['NumOfProducts'] >= 2:
            return 'Active Engaged'
        elif row['IsActiveMember'] == 0 and row['NumOfProducts'] == 1:
            return 'Inactive Disengaged'
        elif row['IsActiveMember'] == 1 and row['NumOfProducts'] == 1:
            return 'Active Low-Product'
        elif row['IsActiveMember'] == 0 and row['Balance'] > 100000:
            return 'Inactive High-Balance'
        else:
            return 'Standard Profile'
            
    df['EngagementProfile'] = df.apply(classify_behavior, axis=1)
    return df

try:
    df = load_and_analyze_bank_data()
except FileNotFoundError:
    st.error("🚨 Critical Error: 'European_Bank.csv' file missing from workspace root directory.")
    st.stop()

# 3. CONTROL SIDEBAR PANEL
st.sidebar.markdown("## 🛠️ Global Parameters")
st.sidebar.markdown("---")

selected_geography = st.sidebar.multiselect(
    "Market Geography Filter",
    options=df['Geography'].unique(),
    default=df['Geography'].unique()
)

salary_cutoff = st.sidebar.slider(
    "Annual Estimated Salary Range",
    float(df['EstimatedSalary'].min()),
    float(df['EstimatedSalary'].max()),
    (float(df['EstimatedSalary'].min()), float(df['EstimatedSalary'].max()))
)

min_balance = st.sidebar.number_input(
    "Asset Liquidity Floor (Balance ≥)",
    min_value=0.0,
    value=0.0,
    step=25000.0
)

# Apply Filters dynamically
filtered_df = df[
    (df['Geography'].isin(selected_geography)) &
    (df['EstimatedSalary'].between(salary_cutoff[0], salary_cutoff[1])) &
    (df['Balance'] >= min_balance)
]

# 4. APPLICATION BRAND HEADER
st.markdown("# 📊 Institutional Risk & Client Engagement Platform")
st.markdown("##### *Strategic Retention Management Dashboard • Unified Mentor Hub (ECB Framework)*")
st.markdown("---")

# 5. PROFESSIONAL DATA-DRIVEN METRIC BLOCKS (HTML-Powered Perfect Borders)
c1, c2, c3, c4 = st.columns(4)

with c1:
    global_churn = filtered_df['Exited'].mean() * 100
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-title">Global Defection Rate</div>
            <div class="kpi-value">{global_churn:.2f}%</div>
            <div class="kpi-subtitle danger">📊 Active Portfolio Attrition</div>
        </div>
    """, unsafe_allow_html=True)

with c2:
    active_c = filtered_df[filtered_df['IsActiveMember'] == 1]['Exited'].mean() * 100
    inactive_c = filtered_df[filtered_df['IsActiveMember'] == 0]['Exited'].mean() * 100
    delta = inactive_c - active_c
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-title">Engagement Variance</div>
            <div class="kpi-value">+{delta:.1f}%</div>
            <div class="kpi-subtitle danger">⚠️ High Inactive Risk Gap</div>
        </div>
    """, unsafe_allow_html=True)

with c3:
    sweet_spot_churn = filtered_df[filtered_df['NumOfProducts'] == 2]['Exited'].mean() * 100
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-title">2-Product Benchmark</div>
            <div class="kpi-value">{sweet_spot_churn:.2f}%</div>
            <div class="kpi-subtitle">✅ Optimal Target Depth</div>
        </div>
    """, unsafe_allow_html=True)

with c4:
    premium_silent_churn = filtered_df[(filtered_df['Balance'] > 100000) & (filtered_df['IsActiveMember'] == 0)]['Exited'].mean() * 100
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-title">Premium Silent Churn</div>
            <div class="kpi-value">{premium_silent_churn:.2f}%</div>
            <div class="kpi-subtitle danger">🚨 Dormant Assets At Risk</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# 6. ADVANCED GRAPHICAL INTERFACES (PLOTLY INTERACTIVE SHAPES)
chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    st.markdown("### 🧬 Cohort Deconstruction Matrix")
    prof_stats = filtered_df.groupby('EngagementProfile')['Exited'].agg(['count', 'mean']).reset_index()
    prof_stats['Churn Rate (%)'] = round(prof_stats['mean'] * 100, 2)
    prof_stats = prof_stats.sort_values(by='Churn Rate (%)', ascending=True)
    
    fig_profile = px.bar(
        prof_stats,
        x='Churn Rate (%)',
        y='EngagementProfile',
        orientation='h',
        text='Churn Rate (%)',
        color='Churn Rate (%)',
        color_continuous_scale='RdYlBu_r',
        template='plotly_white'
    )
    fig_profile.update_layout(
        margin=dict(l=20, r=20, t=10, b=10),
        height=380,
        showlegend=False
    )
    st.plotly_chart(fig_profile, use_container_width=True)

with chart_col2:
    st.markdown("### 📉 The Product Saturation Elasticity Curve")
    prod_stats = filtered_df.groupby('NumOfProducts')['Exited'].mean().reset_index()
    prod_stats['Churn Rate (%)'] = round(prod_stats['Exited'] * 100, 2)
    
    fig_curve = go.Figure()
    fig_curve.add_trace(go.Scatter(
        x=prod_stats['NumOfProducts'],
        y=prod_stats['Churn Rate (%)'],
        mode='lines+markers+text',
        text=prod_stats['Churn Rate (%)'],
        textposition="top center",
        line=dict(color='#dc3545', width=3, shape='spline'),
        marker=dict(size=10, color='#1a252c', symbol='circle')
    ))
    fig_curve.update_layout(
        xaxis=dict(tickmode='linear', dtick=1, title="Number of Bank Products Held"),
        yaxis=dict(title="Calculated Churn Rate (%)", range=[-5, 110]),
        template='plotly_white',
        margin=dict(l=20, r=20, t=10, b=10),
        height=380
    )
    st.plotly_chart(fig_curve, use_container_width=True)

st.markdown("---")

# 7. EARLY-WARNING AT-RISK PREMIUM REGISTRY
st.markdown("### ⚡ Priority Retain Targets: High-Asset Dormant Clients")
st.markdown("The register displays currently active clients with assets exceeding **\$100,000** who maintain low product volume and zero active account interaction flags.")

flagged_premium_targets = filtered_df[
    (filtered_df['Balance'] > 100000) &
    (filtered_df['IsActiveMember'] == 0) &
    (filtered_df['NumOfProducts'] == 1) &
    (filtered_df['Exited'] == 0)
].sort_values(by='Balance', ascending=False)[['CustomerId', 'Surname', 'Geography', 'CreditScore', 'Balance', 'EstimatedSalary']]

if not flagged_premium_targets.empty:
    st.dataframe(
        flagged_premium_targets.style.format({
            'Balance': '${:,.2f}',
            'EstimatedSalary': '${:,.2f}'
        }),
        use_container_width=True,
        hide_index=True
    )
    st.toast(f"System identified {len(flagged_premium_targets)} high-yield customer profiles for proactive outreach.", icon="🚩")
else:
    st.info("Excellent! No unmitigated high-value dormant assets currently detected with the selected global filters.")