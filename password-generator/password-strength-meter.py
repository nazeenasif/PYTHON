import re
import streamlit as st

st.set_page_config(page_title="Password Strenght Meter By Nazeen Asif", page_icon="🔑", layout="centered")

st.sidebar.title("🔍 Navigation")
page = st.sidebar.radio("GO to", ["Password Checker", "View Saved Password"])

st.sidebar.write("🚀 Developed by **Nazeen Asif**")

if "passwords" not in st.session_state:
    st.session_state["passwords"] = {} 

st.markdown("""
    <style>
        .main {
            text-align: center;
        }
        input[type="text"] {
            width: 60% !important;
            margin: auto;
            display: block;
            text-align: center;
        }
        .custom-text {
            font-size: 24px;
            font-weight: bold;
            color: #333;
            margin-bottom: 20px;
        }
        .stButton>button {
            width: 50%;j
            max-width: 300px;
            background-color: green; 
            color: white; 
            font-size: 32px; 
            font-weight: bold;
            border-radius: 10px;
            padding: 10px;
            transition: background-color 0.3s ease;
        }
        .stButton>button:hover { 
            background-color: darkgreen;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)


def check_password_strength(password) :
    score = 0
    feedback = []
    
    #characters
    if len(password) >= 8 :
        score += 1 
    else :
        feedback.append("❌ Your password should be **at least 8 characters long**.") 
    
    #uppercase and lowercase letters
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]",password) :
        score += 1
    else :
        feedback.append("❌ Your password should contain **both uppercase (A-Z) and lowercase (a-z) letter**.")

    #numbers
    if re.search(r"[0-9]", password) :
        score += 1
    else :
        feedback.append("❌ Your password should contain **at least one number (0-9)**.")

    #special characters
    if re.search(r"!@#$%^&", password) :
        score += 1
    else :
        feedback.append("❌ Your password should contain **at least one special character (!@#$%^&)**.")

    if score == 4:
        st.success("✅ **Strong Password** Your password is secure.")
    elif score >= 3:
        st.info("⚠️ **Moderate Password** Your password is good, but consider adding a few more characters.")
    else :
        st.warning("❌ **Weak Password** Your password is weak, consider adding more characters.")

    if feedback :
        with st.expander("🔍 **Improve Your Password**"):
            for item in feedback:
                st.write(item)

if page == "Password Checker":
    st.title("🔐 Password Strength Meter ")
    st.write("Enter your password to check its security level 🔍")                
    
    username = st.text_input("Enter Account Name (e.g., Gmail, Facebook, etc.):", help="Enter a unique account name")
    password = st.text_input("Enter Password:", type="password", help="Ensure your password is strong 🔒" )      

    if st.button ("Check Strength"):
        if password:
           check_password_strength(password)
        else :
           st.error("⚠️ Please enter a password first!")

    if st.button("Save Password"):
         if username and password:
            st.session_state["passwords"][username] = password  # Save password explicitly
            st.success(f"✅ Password saved for **{username}** successfully!")
         else:
            st.error("⚠️ Please enter both account name and password before saving!")

elif page == "View Saved Password" :
        st.title("📑 View Your Saved Password")

        if st.session_state["passwords"]:
            for account, saved_password in st.session_state["passwords"].items():
               with st.expander(f"🔑 {account}"):
                st.text_input("Saved Password:", value=saved_password, type="password", disabled=True)
        else:
           st.warning("⚠️ No passwords found! Please save some first.")



