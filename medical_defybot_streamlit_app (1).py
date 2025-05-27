
import streamlit as st
import requests

st.set_page_config(page_title="Medical DefyBot", page_icon=":robot_face:")
st.title("Medical DefyBot")
st.write("Ask any medical question below:")

# User input
user_input = st.text_input("Your Question", "")

# Display response
if user_input:
    with st.spinner("Thinking..."):
        try:
            # Replace with actual API or chatbot endpoint
            endpoint = "https://udify.app/chat/tVtH6TwhsRrJZu0B"
            response = requests.post(endpoint, json={"query": user_input})

            # Assuming the response is in JSON and has a 'response' field
            if response.status_code == 200:
                data = response.json()
                st.success(data.get("response", "No response found."))
            else:
                st.error(f"API error: {response.status_code}")
        except Exception as e:
            st.error(f"Error: {e}")
