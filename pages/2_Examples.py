import streamlit as st
from PIL import Image

st.title("📈 Examples of Bayesian Decision Making")

st.markdown("""
### 🦠 Medical Test Decision
- **Problem:** Should a doctor treat a patient based on a test?
- **Prior:** Disease prevalence = 10%
- **Likelihoods:**  
    - P(Positive Test | Disease) = 0.95  
    - P(Positive Test | No Disease) = 0.05
- **Utilities:**  
    - Treat when disease: +100  
    - Treat when no disease: -20  
    - Don't treat: 0

**Run this in the calculator to try it.**

---

### 📉 Business Investment
- **Problem:** Should a company launch a new product?
- **Prior:** Market success chance = 60%
- **Likelihoods:**  
    - Positive market research result given success = 0.8  
    - Positive result given failure = 0.3
- **Utilities:**  
    - Launch with success: +500  
    - Launch with failure: -200  
    - Don't launch: 0

---

### 🎯 A/B Test Marketing
- **Problem:** Is variant B better than A?
- **Prior:** 50% chance
- **Likelihoods:**  
    - Observed uplift under B if B better = 0.9  
    - Observed uplift under B if not = 0.1
- **Utilities:**  
    - Use B if better: +200  
    - Use B if not: -50  
    - Stick with A: 0

---

👉 Use the **Calculator tab** to input these numbers and see how it works!
""")
