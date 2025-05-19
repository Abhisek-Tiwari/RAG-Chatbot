import streamlit as st
from rag_pipeline import create_rag_chain

# Initialize the RAG chain
@st.cache_resource
def get_chain():
    return create_rag_chain("faq.csv")

st.set_page_config(page_title="RAG Chatbot", layout="centered")

st.title("📚 RAG Chatbot (Open Source LLM)")
st.write("Ask questions based on the loaded knowledge base.")

# Load chain
chain = get_chain()

# Session state for messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Clear button
if st.button("🧹 Clear Chat"):
    st.session_state.messages = []

# Input field
user_input = st.text_input("You:", key="input")

# If user submits a query
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    response = chain.invoke({"query": user_input})
    answer = response['result']
    st.session_state.messages.append({"role": "bot", "content": answer})

# Scrollable chat container using st.container()
with st.container():
    st.markdown(
        """
        <div style='max-height: 400px; overflow-y: auto; padding-right:10px;'>
        """, unsafe_allow_html=True
    )

    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(f"💬 **You:** {msg['content']}")
        else:
            st.markdown(f"🤖 **Bot:** {msg['content']}")

    st.markdown("</div>", unsafe_allow_html=True)