import streamlit as st
from hallucinate import factual_check, logical_check, contextual_check,check_citations

st.title("🧠 AI Hallucination Detector")

st.markdown("""
Enter your **context** (question or prompt) and the **model response** below.
The app will analyze the response for:
- Factual hallucinations
- Logical inconsistencies
- Contextual relevance
- Citation validity
""")

context = st.text_area("Context (User Input / Prompt)", height=100)
response = st.text_area("Model Response / Answer", height=150)

if st.button("Check for Hallucinations"):
    if not context.strip() or not response.strip():
        st.error("Please enter both context and response.")
    else:
        st.subheader("Analysis Results:")
        st.write(factual_check(response))
        st.write(logical_check(response))
        st.write(contextual_check(context, response))
        citations = check_citations(response)
        for url, status in citations.items():
            st.write(f"citation:{url} → {status}")

