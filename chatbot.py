import openai
import streamlit as st

# Initialize the OpenAI client with your API key
openai.api_key = "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"

st.title("Bav Bot")

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.echo():
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

prompt = st.chat_input("What's up?")
if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        for response in openai.Completion.create(
            engine=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        ).choices:
            full_response += response["text"]
            message_placeholder.markdown(full_response + " ")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})
