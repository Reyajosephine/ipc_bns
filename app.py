import streamlit as st
from compare import find_best_match_with_changes

st.set_page_config(page_title="IPC ↔ BNS Comparator (RAG)", layout="centered")
st.title("⚖ IPC ↔ BNS Comparator (RAG + LLM)")

ipc_section = st.text_input("Enter IPC Section Number (e.g., 420)")

if st.button("Compare"):
    if ipc_section:
        with st.spinner("🔍 Searching best match using RAG + LLM..."):
            result = find_best_match_with_changes(ipc_section)

        if "error" in result:
            st.error(result["error"])
        else:
            ipc = result["ipc_section"]
            bns = result["bns_section"]

            st.subheader("📘 IPC Section")
            st.markdown(f"**Section {ipc['section']}: {ipc['title']}**")
            st.write(ipc["description"])

            st.subheader("📙 BNS Section (Matched via RAG + LLM)")
            st.markdown(f"**Section {bns['section']}: {bns['title']}**")
            st.write(bns["description"])

            st.subheader("🧠 Matching Method")
            st.info(result["similarity"])

            st.subheader("🔍 Change Summary")
            for change in result["change_summary"]:
                st.write(f"- {change}")

            # Display the detailed LLM summary nicely formatted:
            if "llm_summary" in result and result["llm_summary"]:
                st.subheader("🤖 Detailed LLM Generated Summary")
                st.markdown(result["llm_summary"])
            else:
                st.warning("LLM summary not available or empty.")
    else:
        st.warning("Please enter a valid IPC section number.")
