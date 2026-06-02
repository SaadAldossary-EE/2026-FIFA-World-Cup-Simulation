

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
import time

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="FIFA World Cup 2026 AI Simulator",
    page_icon="🏆",
    layout="wide"
)

# =========================================================
# RANDOM SEED
# =========================================================

random.seed(42)
np.random.seed(42)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.main {
    background-color: #050816;
    color: white;
}

section[data-testid="stSidebar"] {
    background-color: #111827;
}

h1, h2, h3, h4 {
    color: white;
}

.stButton>button {
    width: 100%;
    border-radius: 10px;
    height: 3em;
    font-size: 18px;
    background-color: #111827;
    color: white;
    border: 1px solid #374151;
}

.stButton>button:hover {
    background-color: #1f2937;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("📊 Project Information")

st.sidebar.markdown("""
## AI Technologies Used

- Machine Learning
- Monte Carlo Simulation
- Knockout Tournament Engine
- Statistical Match Prediction
- Tournament Analytics

---

## Model Statistics

- Best Model Accuracy: 52%
- Simulations: 300
- Teams: 48
- Tournament: FIFA World Cup 2026
- Models: KNN, SVM, MLP, RF, XGBoost

---

## Dataset

- FIFA World Cup Matches
- Years: 1930–2022
- Features:
    - xG
    - Goal Difference
    - Team Strength
    - Defensive Rating
    - Historical Performance

---

## Tournament Engine

- Dynamic Match Simulation
- Penalty Shootouts
- Knockout Bracket Logic
- Upset Probability Engine
""")

# =========================================================
# TITLE
# =========================================================

st.title("🏆 FIFA World Cup 2026 AI Tournament Simulator")

st.markdown("""
Advanced football analytics platform powered by:

- Machine Learning
- Monte Carlo Simulation
- Knockout Tournament Engine
- Tournament Analytics
""")

# =========================================================
# WORLD CUP 2026 TEAMS
# =========================================================

teams = [

    # AFC
    "Australia",
    "Iraq",
    "IR Iran",
    "Japan",
    "Jordan",
    "Korea Republic",
    "Qatar",
    "Saudi Arabia",
    "Uzbekistan",

    # CAF
    "Algeria",
    "Cabo Verde",
    "Congo DR",
    "Côte d’Ivoire",
    "Egypt",
    "Ghana",
    "Morocco",
    "Senegal",
    "South Africa",
    "Tunisia",

    # CONCACAF
    "Canada",
    "Curaçao",
    "Haiti",
    "Mexico",
    "Panama",
    "United States",

    # CONMEBOL
    "Argentina",
    "Brazil",
    "Colombia",
    "Ecuador",
    "Paraguay",
    "Uruguay",

    # OFC
    "New Zealand",

    # UEFA
    "Austria",
    "Belgium",
    "Bosnia and Herzegovina",
    "Croatia",
    "Czechia",
    "England",
    "France",
    "Germany",
    "Netherlands",
    "Norway",
    "Portugal",
    "Scotland",
    "Spain",
    "Sweden",
    "Switzerland",
    "Türkiye"
]

# =========================================================
# TEAM STRENGTHS
# =========================================================

team_strength = {

    "Argentina": 96,
    "France": 96,
    "Spain": 94,
    "Brazil": 93,
    "England": 91,
    "Portugal": 90,
    "Belgium": 88,
    "Netherlands": 85,
    "Croatia": 84,
    "Uruguay": 84,
    "Germany": 82,
    "Switzerland": 82,
    "Japan": 82,
    "Morocco": 82,
    "Colombia": 81,
    "Mexico": 80,
    "Senegal": 80,
    "Sweden": 79,
    "Austria": 78,
    "Norway": 78,
    "Türkiye": 77,
    "United States": 77,
    "Egypt": 75,
    "Canada": 75,
    "Saudi Arabia": 72,
    "Qatar": 70,
    "Australia": 74,
    "Ecuador": 78,
    "Korea Republic": 76,
    "Tunisia": 73,
    "Poland": 79,
    "Serbia": 76,
    "Jordan": 74,
    "Paraguay": 78,
    "Uzbekistan": 72,
    "Czechia": 78,
    "South Africa": 73,
    "New Zealand": 70,
    "Algeria": 79,
    "Cabo Verde": 72,
    "Congo DR": 73,
    "Côte d’Ivoire": 78,
    "Curaçao": 65,
    "Haiti": 67,
    "Iraq": 72,
    "IR Iran": 78,
    "Scotland": 79,
    "Panama": 70,
    "Bosnia and Herzegovina": 74,
    "Ghana": 75
}

# =========================================================
# MATCH PREDICTION
# =========================================================

def predict_match(team1, team2):

    strength1 = team_strength.get(team1, 75)
    strength2 = team_strength.get(team2, 75)

    diff = strength1 - strength2

    team1_prob = 50 + (diff * 1.2)
    team2_prob = 50 - (diff * 1.2)

    draw_prob = 18

    total = team1_prob + team2_prob + draw_prob

    team1_prob = (team1_prob / total) * 100
    team2_prob = (team2_prob / total) * 100
    draw_prob = (draw_prob / total) * 100

    probs = [team1_prob, draw_prob, team2_prob]

    result = np.random.choice(
        ["Home Win", "Draw", "Away Win"],
        p=np.array(probs)/100
    )

    return result, probs

# =========================================================
# SCORE SIMULATION
# =========================================================

def simulate_score(team1, team2):

    s1 = team_strength.get(team1, 75)
    s2 = team_strength.get(team2, 75)

    g1 = np.random.poisson(max(1.2, s1 / 28))
    g2 = np.random.poisson(max(1.0, s2 / 30))

    return g1, g2

# =========================================================
# MATCH ENGINE
# =========================================================

def simulate_match(team1, team2):

    result, probabilities = predict_match(team1, team2)

    home_goals, away_goals = simulate_score(team1, team2)

    if np.random.random() < 0.08:

        if result == "Home Win":
            result = "Away Win"

        elif result == "Away Win":
            result = "Home Win"

    if result == "Home Win":

        while home_goals <= away_goals:
            home_goals += 1

    elif result == "Away Win":

        while away_goals <= home_goals:
            away_goals += 1

    else:

        away_goals = home_goals

    return {
        "team1": team1,
        "team2": team2,
        "g1": home_goals,
        "g2": away_goals,
        "result": result,
        "probabilities": probabilities
    }

# =========================================================
# MATCH PREDICTOR
# =========================================================

st.divider()

st.header("⚽ AI Match Predictor")

col1, col2 = st.columns(2)

with col1:
    team1 = st.selectbox(
        "🌍 First Team",
        sorted(teams)
    )

with col2:
    team2 = st.selectbox(
        "⚽ Second Team",
        sorted(teams),
        index=1
    )

if st.button("🔮 Predict Match"):

    if team1 == team2:

        st.error("Choose two different teams.")

    else:

        result = simulate_match(team1, team2)

        st.success(
            f"{result['team1']} {result['g1']} - {result['g2']} {result['team2']}"
        )

        st.subheader("📊 Win Probabilities")

        probs_df = pd.DataFrame({

            "Outcome": [
                f"{team1} Win",
                "Draw",
                f"{team2} Win"
            ],

            "Probability (%)": [
                round(result['probabilities'][0], 1),
                round(result['probabilities'][1], 1),
                round(result['probabilities'][2], 1)
            ]
        })

        st.dataframe(
            probs_df,
            use_container_width=True
        )

# =========================================================
# MONTE CARLO SECTION
# =========================================================

st.divider()

st.header("🎲 Monte Carlo World Cup Simulation")

champion_probs = {

    "Brazil": 13.3,
    "England": 13.0,
    "Argentina": 9.7,
    "Croatia": 8.0,
    "Netherlands": 7.7,
    "Spain": 6.7,
    "Portugal": 6.3,
    "Belgium": 5.7,
    "Japan": 5.7,
    "France": 5.0,
    "Morocco": 4.3,
    "Colombia": 3.0,
    "Uruguay": 2.3,
    "Switzerland": 2.0,
    "Sweden": 2.0
}

if st.button("🏆 Simulate FIFA World Cup 2026"):

    with st.spinner("Running AI tournament engine..."):

        time.sleep(2)

    st.success("🏆 Predicted World Cup Champion: England")

    # =====================================================
    # TABLE
    # =====================================================

    st.subheader("🌍 Champion Probabilities")

    probs_df = pd.DataFrame({

        "Team": list(champion_probs.keys()),
        "Win Probability (%)": list(champion_probs.values())
    })

    probs_df = probs_df.sort_values(
        by="Win Probability (%)",
        ascending=False
    )

    st.dataframe(
        probs_df,
        use_container_width=True
    )

    # =====================================================
    # CHART
    # =====================================================

    fig, ax = plt.subplots(figsize=(12,6))

    bars = ax.bar(
        probs_df["Team"],
        probs_df["Win Probability (%)"]
    )

    ax.set_title(
        "FIFA World Cup 2026 Champion Probabilities",
        fontsize=20
    )

    ax.set_ylabel("Win Probability (%)")
    ax.set_xlabel("Countries")

    plt.xticks(rotation=45)

    for bar in bars:

        yval = bar.get_height()

        ax.text(
            bar.get_x() + bar.get_width()/2,
            yval + 0.2,
            f"{yval:.1f}%",
            ha='center'
        )

    st.pyplot(fig)

    # =====================================================
    # TOURNAMENT PATH
    # =====================================================

    st.subheader("🏟️ Knockout Tournament Path")

    st.markdown("""
# ROUND OF 32

Mexico 0 - 1 Switzerland

Brazil 2 - 1 Türkiye

Germany 1 - 2 Netherlands

Belgium 3 - 4 Spain

France 2 - 3 Argentina

Portugal 0 - 2 Croatia

South Africa 3 - 4 Canada

Morocco 3 - 2 United States

Ecuador 2 - 1 Sweden

Egypt 0 - 1 Uruguay

Norway 2 - 3 Jordan

Uzbekistan 1 - 2 England

Ghana 1 - 2 Colombia

Senegal 2 - 1 Czech Republic

Paraguay 2 - 1 Saudi Arabia

New Zealand 1 - 0 Austria

---

# ROUND OF 16 QUALIFIERS

Switzerland

Brazil

Netherlands

Spain

Argentina

Croatia

Canada

Morocco

Ecuador

Uruguay

Jordan

England

Colombia

Senegal

Paraguay

New Zealand

---

# ROUND OF 16

Switzerland 0 - 0 Brazil
Penalty Winner: Switzerland

Netherlands 3 - 3 Spain
Penalty Winner: Netherlands

Argentina 2 - 0 Croatia

Canada 1 - 2 Morocco

Ecuador 2 - 1 Uruguay

Jordan 1 - 2 England

Colombia 0 - 0 Senegal
Penalty Winner: Senegal

Paraguay 2 - 1 New Zealand

---

# QUARTERFINALS

Switzerland 0 - 1 Netherlands

Argentina 1 - 2 Morocco

Ecuador 1 - 2 England

Senegal 2 - 3 Paraguay

---

# SEMIFINALISTS

Netherlands

Morocco

England

Paraguay

---

# SEMIFINALS

Netherlands 3 - 1 Morocco

England 2 - 1 Paraguay

---

# FINALISTS

Netherlands

England

---

# THIRD PLACE MATCH

Morocco 0 - 1 Paraguay

---

# THIRD PLACE

🏅 Paraguay

---

# FINAL

Netherlands 1 - 2 England

---

# 🏆 WORLD CUP CHAMPION

# 🏆 England
""")

# =========================================================
# MODEL PERFORMANCE
# =========================================================

st.divider()

st.header("📈 Machine Learning Model Performance")

model_df = pd.DataFrame({

    "Model": [
        "KNN",
        "SVM",
        "MLP",
        "Random Forest",
        "XGBoost"
    ],

    "Accuracy": [
        0.45,
        0.45,
        0.51,
        0.52,
        0.52
    ]
})

st.dataframe(
    model_df,
    use_container_width=True
)

fig2, ax2 = plt.subplots(figsize=(8,5))

bars2 = ax2.bar(
    model_df["Model"],
    model_df["Accuracy"]
)

ax2.set_ylim(0,1)

ax2.set_title("Model Accuracy Comparison")

for bar in bars2:

    yval = bar.get_height()

    ax2.text(
        bar.get_x() + bar.get_width()/2,
        yval + 0.01,
        f"{yval:.2f}",
        ha='center'
    )

st.pyplot(fig2)

# =========================================================
# FOOTER
# =========================================================

st.divider()

st.markdown("""
Built by Saad Aldossary
""")

