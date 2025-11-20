import streamlit as st
import numpy as np
import joblib
import pandas as pd
import matplotlib.pyplot as plt



# PAGE CONFIG & BASIC STYLING

st.set_page_config(
    page_title="AI Student Stress Analyzer",
    page_icon="🧠",
    layout="wide"
)

st.markdown("""
    <style>
        .main {background-color: #f8f9fa;}
        .title {text-align: center; font-size: 40px; color: #2c3e50; font-weight: bold;}
        .sub {text-align: center; font-size: 20px; color: #34495e;}
    </style>
""", unsafe_allow_html=True)



# LOAD MODELS


rf_model = joblib.load("rf_model.pkl")
xgb_model = joblib.load("xgb_model.pkl")



# PAGE TITLE


st.markdown("<div class='title'> AI-Based Student Stress Prediction System</div>", unsafe_allow_html=True)
st.markdown("<div class='sub'>Predict stress level using behavioral and academic indicators</div><br>", unsafe_allow_html=True)



# SIDEBAR USER INPUT


st.sidebar.title(" Input Student Details")

sleep = st.sidebar.slider("Sleep Quality (1–5)", 1, 5, 3)
acad = st.sidebar.slider("Academic Performance (1–5)", 1, 5, 3)
study = st.sidebar.slider("Study Load (1–5)", 1, 5, 3)
extra = st.sidebar.slider("Extracurricular Activities (1–5)", 1, 5, 3)

user_input = np.array([[sleep, acad, study, extra]])



# PREDICTION SECTION


if st.sidebar.button("Predict Stress"):

    # Random Forest Regression
    stress_score = rf_model.predict(user_input)[0]

    # XGBoost Classification (0–4 → +1)
    stress_class = int(xgb_model.predict(user_input)[0]) + 1

    # Combined Score
    combined_score = (stress_score + stress_class) / 2

    # Display Scores
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Predicted Stress Score")
        st.markdown(f"<h2 style='color:#e74c3c'>{stress_score:.2f} / 5</h2>", unsafe_allow_html=True)

    with col2:
        st.markdown("### Stress Category (XGBoost)")
        st.markdown(f"<h2 style='color:#2980b9'>{stress_class}</h2>", unsafe_allow_html=True)

    
    # RECOMMENDATION LOGIC
    
    if combined_score < 2:
        level = "Very Low Stress 🟢"
        advice = "Maintain your routine; you're doing great!"
    elif combined_score < 3:
        level = "Low Stress 🟡"
        advice = "Stress is manageable; keep healthy habits."
    elif combined_score < 4:
        level = "Moderate Stress 🟠"
        advice = "Improve sleep & reduce workload where possible."
    elif combined_score < 4.5:
        level = "High Stress 🔴"
        advice = "Reduce workload, take breaks, focus on balance."
    else:
        level = "Very High Stress ⚠️"
        advice = "Seek help immediately; prioritize your well-being."

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"### Stress Interpretation: {level}")
    st.markdown(f"**Recommendation:** {advice}")



# DASHBOARD SECTION


st.markdown("<br><hr><h2 style='text-align:center;'>📊 Stress Data Dashboard</h2><br>", unsafe_allow_html=True)

try:
    df = pd.read_csv("Combined_Student_Stress.csv")

    colA, colB = st.columns(2)

    # Feature Importance
    with colA:
        st.markdown("### 🔍 Feature Importance (Random Forest)")
        importances = rf_model.feature_importances_
        fig, ax = plt.subplots()
        ax.bar(df.columns[:-1], importances, color='teal')
        ax.set_ylabel("Importance Score")
        st.pyplot(fig)

    # Stress Distribution
    with colB:
        st.markdown("### 📈 Stress Level Distribution")
        fig2, ax2 = plt.subplots()
        df["StressLevel"].plot(kind="hist", bins=5, color="orange", edgecolor="black")
        ax2.set_xlabel("Stress Level")
        ax2.set_ylabel("Frequency")
        st.pyplot(fig2)

    # Heatmap
    st.markdown("### 🔥 Correlation Heatmap")
    fig3, ax3 = plt.subplots()
    corr = df.corr()
    im = ax3.imshow(corr, cmap="coolwarm")
    plt.colorbar(im, ax=ax3)
    ax3.set_xticks(range(len(corr.columns)))
    ax3.set_yticks(range(len(corr.columns)))
    ax3.set_xticklabels(corr.columns, rotation=45)
    ax3.set_yticklabels(corr.columns)
    st.pyplot(fig3)

except:
    st.warning("Upload Combined_Student_Stress.csv to enable dashboard features.")



# ADVANCED VISUALIZATIONS


st.markdown("<hr><h2 style='text-align:center;'>📊 Advanced Model & Data Insights</h2><br>", 
            unsafe_allow_html=True)


# MODEL COMPARISON
st.markdown("### 🏆 Model Comparison (Regression & Classification)")

models = [
    "Simple Linear Regression","Multiple Linear Regression","Polynomial Regression",
    "Decision Tree Regression","Random Forest Regression","Logistic Regression",
    "KNN Classifier","Naive Bayes","SVM Classifier","XGBoost Classifier"
]

r2_scores = [0.121,0.1356,0.1456,0.372,0.684,0,0,0,0,0.86]
rmse_inv = [1/1.257,1/1.2467,1/1.2394,1/1.096,1/0.777,0,0,0,0,0]
accuracy = [0,0,0,0,0,0.7266,0.43,0.71,0.85,0.86]

fig4, ax4 = plt.subplots(figsize=(12,6))
width = 0.25
x = np.arange(len(models))

ax4.bar(x-width, r2_scores, width, label="R² Score", color="#1abc9c")
ax4.bar(x, rmse_inv, width, label="RMSE (Inverted)", color="#e67e22")
ax4.bar(x+width, accuracy, width, label="Accuracy", color="#3498db")

ax4.set_xticks(x)
ax4.set_xticklabels(models, rotation=90)
ax4.set_ylabel("Performance Score")
ax4.set_title("Comparison of All ML Models")
ax4.legend()

st.pyplot(fig4)




# BOX PLOT – ACADEMIC PERFORMANCE VS STRESS
st.markdown("### 🎓 Academic Performance vs Stress Level")
fig6, ax6 = plt.subplots()
df.boxplot(column="StressLevel", by="AcademicPerf", ax=ax6)
plt.suptitle("")
ax6.set_title("Stress Distribution Across Academic Performance")
ax6.set_xlabel("Academic Performance")
ax6.set_ylabel("Stress Level")
st.pyplot(fig6)


