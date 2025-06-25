import streamlit as st

st.title("📚 Learn More: Bayesian Decision Theory")

st.markdown(r"""
## 🔢 Bayes' Theorem
\[
P(H|E) = \frac{P(E|H) \cdot P(H)}{P(E|H) \cdot P(H) + P(E| \neg H) \cdot P(\neg H)}
\]

- **P(H)** = Prior probability
- **P(E|H)** = Likelihood of evidence under H
- **P(H|E)** = Posterior probability

---

## ⚖️ Decision Theory
Expected utility formula:

\[
EU = P(H|E) \cdot U(Decision, H) + P(\neg H|E) \cdot U(Decision, \neg H)
\]

The best decision is the one with the highest expected utility.

---

## 🔁 Sequential Updating
With multiple pieces of evidence, update the prior step by step:

1. Compute posterior with Evidence 1
2. Use that as the new prior for Evidence 2
3. Repeat

---

## 📚 References
- *Think Bayes* by Allen B. Downey (Free online)
- *Bayesian Reasoning and Machine Learning* by David Barber
- Wikipedia: [Bayesian Inference](https://en.wikipedia.org/wiki/Bayesian_inference)

---
""")
