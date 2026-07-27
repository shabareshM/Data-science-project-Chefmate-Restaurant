import streamlit as st

def recipe_chatbot():

    st.title("👨‍🍳 AI Recipe Assistant")

    st.write("Ask any cooking question.")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:

        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    prompt = st.chat_input("Type your recipe question...")

    if prompt:

        st.session_state.messages.append(
            {
                "role":"user",
                "content":prompt
            }
        )

        with st.chat_message("user"):
            st.write(prompt)

        answer = f"""
### 🍽 Recipe

You asked:

**{prompt}**

This is a demo chatbot.

Later we will connect Gemini AI.

Example:

✅ Ingredients

✅ Preparation

✅ Cooking Steps

✅ Cooking Time

✅ Tips
"""

        with st.chat_message("assistant"):
            st.markdown(answer)

        st.session_state.messages.append(
            {
                "role":"assistant",
                "content":answer
            }
        )