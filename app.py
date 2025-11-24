import streamlit as st
from pdf_utils import extract_text_from_pdf
from summarizer import (
    summarize_text,
    extract_title,
    extract_keywords,
    check_plagiarism,
    semantic_search,
    generate_ppt,
    extract_algorithms_equations,
    generate_research_notes_pdf,
)

# ---------- Custom CSS ----------

def load_custom_css():
    st.markdown(
        """
    <style>
    /* Global body */
    body, .stApp {
        background-color: #0d1117;
        color: #f0f6fc;
        font-family: "Segoe UI", system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
    }

    /* Header Gradient */
    .title-wrapper {
        padding: 24px 30px;
        border-radius: 18px;
        background: linear-gradient(135deg, #6f42c1, #1f6feb);
        text-align: center;
        color: white !important;
        margin-bottom: 28px;
        box-shadow: 0px 0px 20px rgba(100,100,255,0.35);
    }

    .title-wrapper h1 {
        margin-bottom: 6px;
    }

    /* Section titles */
    .section-title {
        font-size: 1.1rem;
        font-weight: 600;
        margin-bottom: 6px;
    }

    /* Card look via containers (no extra empty divs) */
    .stContainer {
        padding: 0.5rem 0.2rem;
    }

    /* Buttons */
    .stButton>button {
        background: linear-gradient(90deg, #6f42c1, #1f6feb);
        color: white;
        padding: 0.6rem 1.2rem;
        border-radius: 10px;
        font-size: 0.95rem;
        border: none;
        box-shadow: 0px 4px 10px rgba(111, 66, 193, 0.35);
    }

    .stButton>button:hover {
        transform: scale(1.03);
        background: linear-gradient(90deg, #8257d6, #3784ff);
    }

    /* Text input */
    .stTextInput>div>div>input {
        background-color: #161b22;
        color: white;
        border-radius: 8px;
        padding: 10px;
        border: 1px solid rgba(255,255,255,0.12);
    }

    /* Select boxes */
    .stSelectbox>div {
        background-color: #161b22;
        border-radius: 8px;
        border: 1px solid rgba(255,255,255,0.12);
    }

    </style>
    """,
        unsafe_allow_html=True,
    )


# ---------- Page config & header ----------

st.set_page_config(
    page_title="AI Research Paper Summarizer",
    layout="centered",
)

load_custom_css()

st.markdown(
    """
<div class="title-wrapper">
    <h1>📄 AI Research Paper Summarizer</h1>
    <p style="font-size:16px; opacity:0.87;">
        Gemini-powered assistant for fast, structured research understanding
    </p>
</div>
""",
    unsafe_allow_html=True,
)

# ---------- File upload ----------

uploaded_file = st.file_uploader("📎 Upload a research paper (PDF)", type="pdf")

if uploaded_file:
    # Save file temporarily
    with open("temp_uploaded.pdf", "wb") as f:
        f.write(uploaded_file.read())

    # Extract text
    extracted_text = extract_text_from_pdf("temp_uploaded.pdf")

    if not extracted_text or not extracted_text.strip():
        st.error("⚠️ No extractable text found in the PDF. Try another file.")
    else:
        # ---------- Preview ----------
        with st.container():
            st.markdown('<div class="section-title">📃 Extracted Preview (first 1000 characters):</div>', unsafe_allow_html=True)
            # Use markdown instead of st.text to avoid big grey box
            st.markdown(
                f"<p style='color:#bfbfbf; white-space:pre-wrap;'>{extracted_text[:1000]}</p>",
                unsafe_allow_html=True,
            )

        # ---------- Summary settings ----------
        with st.container():
            st.markdown('<div class="section-title">📝 Summary Settings</div>', unsafe_allow_html=True)

            summary_length = st.selectbox(
                "Choose summary length:",
                ["Short", "Medium", "Long"],
                index=1,
            )

            summary_style = st.selectbox(
                "Choose summary style:",
                ["Academic", "Simple English", "Bullet Points", "Technical", "Creative"],
                index=0,
            )

            if st.button("🧠 Generate Summary"):
                with st.spinner("Generating summary using Gemini..."):
                    summary = summarize_text(
                        extracted_text[:8000],
                        summary_length,
                        summary_style,
                    )

                if summary:
                    st.subheader("📝 AI-Generated Summary")
                    st.write(summary)

                    st.download_button(
                        label="📥 Download Summary as TXT",
                        data=summary,
                        file_name="summary.txt",
                        mime="text/plain",
                    )
                else:
                    st.error("❌ Failed to generate summary. Try again.")

        # ---------- Additional insights ----------
        with st.container():
            st.markdown('<div class="section-title">📌 Additional Insights</div>', unsafe_allow_html=True)

            col1, col2, col3 = st.columns(3)

            with col1:
                if st.button("🔎 Extract Title from Paper"):
                    with st.spinner("Extracting title..."):
                        title = extract_title(extracted_text[:8000])
                    st.success("Title Extracted:")
                    st.write(f"📘 {title}")

            with col2:
                if st.button("🧩 Extract Keywords"):
                    with st.spinner("Extracting keywords..."):
                        keywords = extract_keywords(extracted_text[:8000])
                    st.success("Keywords Identified:")
                    st.write(keywords)

            with col3:
                if st.button("🕵️ Check Plagiarism"):
                    with st.spinner("Checking plagiarism and originality..."):
                        report = check_plagiarism(extracted_text[:8000])
                    st.success("Plagiarism Analysis Complete:")
                    st.write(report)

        # ---------- Semantic search ----------
        with st.container():
            st.markdown('<div class="section-title">🔍 Semantic Search in Paper</div>', unsafe_allow_html=True)

            user_query = st.text_input(
                "Ask a question about the paper:",
                placeholder="e.g., What is the main contribution of this paper?",
            )

            if st.button("🔎 Search"):
                if not user_query.strip():
                    st.warning("Please enter a question.")
                else:
                    with st.spinner("Searching the paper..."):
                        answer = semantic_search(user_query, extracted_text[:8000])
                    st.success("Answer:")
                    st.write(answer)

        # ---------- Downloads & advanced tools ----------
        with st.container():
            st.markdown('<div class="section-title">📂 Exports & Advanced Tools</div>', unsafe_allow_html=True)

            col_a, col_b, col_c = st.columns(3)

            # PPT
            with col_a:
                if st.button("📊 Generate Presentation (PPT)"):
                    with st.spinner("Creating your PPT..."):
                        ppt_path = generate_ppt(extracted_text[:8000])

                    if isinstance(ppt_path, str) and ppt_path.endswith(".pptx"):
                        with open(ppt_path, "rb") as file:
                            st.download_button(
                                label="📥 Download PPT",
                                data=file,
                                file_name="Research_Presentation.pptx",
                                mime="application/vnd.openxmlformats-officedocument.presentationml.presentation",
                            )
                        st.success("PPT generated successfully!")
                    else:
                        st.error(ppt_path)

            # Research Notes PDF
            with col_b:
                if st.button("📄 Generate Research Notes PDF"):
                    with st.spinner("Creating Research Notes PDF..."):
                        title = extract_title(extracted_text[:8000])
                        keywords = extract_keywords(extracted_text[:8000])
                        summary_for_pdf = summarize_text(
                            extracted_text[:8000],
                            summary_length,
                            summary_style,
                        )
                        plagiarism_report = check_plagiarism(extracted_text[:8000])
                        algo_eq = extract_algorithms_equations(extracted_text[:8000])

                        pdf_path = generate_research_notes_pdf(
                            title,
                            keywords,
                            summary_for_pdf,
                            plagiarism_report,
                            algo_eq,
                        )

                    if isinstance(pdf_path, str) and pdf_path.endswith(".pdf"):
                        with open(pdf_path, "rb") as pdf:
                            st.download_button(
                                label="📥 Download Research Notes PDF",
                                data=pdf,
                                file_name="Research_Notes.pdf",
                                mime="application/pdf",
                            )
                        st.success("PDF generated successfully!")
                    else:
                        st.error(pdf_path)

            # Algorithms & equations
            with col_c:
                if st.button("🧮 Extract Algorithms & Equations"):
                    with st.spinner("Extracting algorithms and equations..."):
                        output = extract_algorithms_equations(extracted_text[:8000])
                    st.success("Extraction Complete:")
                    st.write(output)

else:
    st.info("👆 Upload a PDF above to get started.")

# ---------- Footer ----------
st.markdown("---")
st.caption("Built using Streamlit & Gemini API !")
