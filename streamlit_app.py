import streamlit as st

st.title("Comparative Analysis Report")

# Paste your Power BI embed link below
powerbi_url = "https://app.powerbi.com/view?r=eyJrIjoiZjE0YjA5YWQtMjNlNy00NzMwLThjN2YtODlhNGQ0YWEyYzE5IiwidCI6IjE2ZDgzZWU2LTI1NGEtNDY5ZC1hNmNjLTU0ZTJjYTIzMTNlNyIsImMiOjh9"

st.components.v1.html(
    f'<iframe title="PLATFORM COMPARISON" width="600" height="373.5" src="https://app.powerbi.com/view?r=eyJrIjoiZjE0YjA5YWQtMjNlNy00NzMwLThjN2YtODlhNGQ0YWEyYzE5IiwidCI6IjE2ZDgzZWU2LTI1NGEtNDY5ZC1hNmNjLTU0ZTJjYTIzMTNlNyIsImMiOjh9" frameborder="0" allowFullScreen="true"></iframe>',
    height=600
)