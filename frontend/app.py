import requests
import streamlit as st

API_URL = "http://127.0.0.1:8000/api/ask"


st.set_page_config(
    page_title="LocalSQL-AI",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 LocalSQL-AI")
st.caption("Ask your MySQL database using natural language")

question = st.text_area(
    "Ask a question about your database",
    placeholder="Show my top 5 most expensive transactions"
)

if st.button("Ask AI", type="primary"):

    if not question.strip():

        st.warning("Please enter a question.")

    else:

        with st.spinner("AI is analyzing your database..."):

            try:

                response = requests.post(
                    API_URL,
                    json={"question": question},
                    timeout=300
                )

                response.raise_for_status()

                data = response.json()


                st.subheader("Generated SQL")

                st.code(
                    data["sql"],
                    language="sql"
                )

                st.subheader("Query Results")

                results = data["results"]

                if results["rows"]:

                    st.dataframe(
                        results["rows"],
                        use_container_width=True
                    )

                else:

                    st.info("No results found.")

                st.metric(
                    "Rows returned",
                    results["row_count"]
                )

            except requests.exceptions.RequestException as e:

                st.error(f"API connection error: {e}")