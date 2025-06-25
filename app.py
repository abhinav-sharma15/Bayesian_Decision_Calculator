import streamlit as st

st.set_page_config(
    page_title="Bayesian Decision Calculator",
    page_icon="🎯",
    layout="centered",
)

st.title("🎯 Bayesian Decision Calculator")

st.markdown("""
Welcome to the **Bayesian Decision Calculator**!  
Use this tool to help make better decisions under uncertainty using Bayesian reasoning.

---

### 📊 Features:
- Compute posterior probabilities from your priors and evidence.
- Compare decisions based on expected utilities.
- Learn how Bayesian decision theory works.
- Explore real-world examples.

---

👉 Select a page from the sidebar to get started:
- **Calculator:** Run your own decision analysis.
- **Examples:** Try preset real-world examples.
- **Learn More:** Understand the theory.
- **About:** About this app.
""")

#st.image("assets/bayes_diagram.png", caption="Bayesian Decision Flow", use_column_width=True)
