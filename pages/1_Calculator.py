import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("🧠 Bayesian Decision Calculator")

# --- Inputs ---
st.header("1️⃣ Define Hypotheses")
hypothesis1 = st.text_input("Name of Hypothesis 1 (H1)", "Condition Present")
hypothesis2 = st.text_input("Name of Hypothesis 2 (H2)", "Condition Absent")

prior_H1 = st.slider(f"Prior probability of {hypothesis1} (H1)", 0.0, 1.0, 0.5)
prior_H2 = 1 - prior_H1

st.divider()

st.header("2️⃣ Enter Evidence (Likelihoods)")
likelihood_H1 = st.slider(f"P(Evidence | {hypothesis1})", 0.0, 1.0, 0.9)
likelihood_H2 = st.slider(f"P(Evidence | {hypothesis2})", 0.0, 1.0, 0.1)

# Posterior calculation
evidence = likelihood_H1 * prior_H1 + likelihood_H2 * prior_H2
posterior_H1 = (likelihood_H1 * prior_H1) / evidence
posterior_H2 = 1 - posterior_H1

st.subheader("🔍 Posterior Probabilities")
st.write(f"P({hypothesis1} | Evidence) = {posterior_H1:.3f}")
st.write(f"P({hypothesis2} | Evidence) = {posterior_H2:.3f}")

st.divider()

# --- Utilities ---
st.header("3️⃣ Set Decision Options and Utilities")
decision1 = st.text_input("Decision Option 1", "Act")
decision2 = st.text_input("Decision Option 2", "Don't Act")

st.subheader(f"Utility for decision '{decision1}':")
u_d1_h1 = st.number_input(f"When {hypothesis1} is true", value=1000)
u_d1_h2 = st.number_input(f"When {hypothesis2} is true", value=-500)

st.subheader(f"Utility for decision '{decision2}':")
u_d2_h1 = st.number_input(f"When {hypothesis1} is true", value=0)
u_d2_h2 = st.number_input(f"When {hypothesis2} is true", value=0)

# Expected utilities
EU_d1 = posterior_H1 * u_d1_h1 + posterior_H2 * u_d1_h2
EU_d2 = posterior_H1 * u_d2_h1 + posterior_H2 * u_d2_h2

st.divider()

st.header("4️⃣ Results")
st.subheader("Expected Utilities")
st.write(f"EU({decision1}) = {EU_d1:.2f}")
st.write(f"EU({decision2}) = {EU_d2:.2f}")

# Recommendation
if EU_d1 > EU_d2:
    st.success(f"✅ Recommended Decision: **{decision1}**")
elif EU_d1 < EU_d2:
    st.success(f"✅ Recommended Decision: **{decision2}**")
else:
    st.info("Both decisions have equal expected utility.")

# --- Visuals ---
st.subheader("📊 Expected Utilities Chart")
fig, ax = plt.subplots()
ax.bar([decision1, decision2], [EU_d1, EU_d2], color=['green', 'gray'])
ax.set_ylabel('Expected Utility')
st.pyplot(fig)

st.subheader("🔬 Posterior Probability Pie Chart")
fig2, ax2 = plt.subplots()
ax2.pie([posterior_H1, posterior_H2],
        labels=[hypothesis1, hypothesis2],
        autopct='%1.1f%%',
        colors=['blue', 'orange'])
st.pyplot(fig2)
