import streamlit as st
import random
import datetime

st.set_page_config(page_title="Growth Mindset Challenge", page_icon="🎯")

st.sidebar.title("📌 Navigate")
page = st.sidebar.radio("Go to", ["🏡 Home", "📝 Daily Challenges", "🎯 Goal Setting"])

def main():
    st.title("🚀 Growth Mindset Challenge")

    if page == "🏡 Home":
        st.header("Welcome to Growth Mindset Challenge! 🎯")
        st.write("Let's develop a mindset that embraces learning and improvement.")

        quotes = [
            "⭐ The journey of a thousand miles begins with a single step.",
            "⭐ Believe you can and you're halfway there.",
            "⭐ Success is not final, failure is not fatal: It is the courage to continue that counts.",
            "⭐ Mistakes show you're trying!",
            "⭐ Challenges help us grow!",
            "⭐ Your potential is limitless!",
            "⭐ Don't stop questioning. Curiosity has its own reason for existing."
        ]

        st.subheader("💡 Today's Motivation: ")
        st.write(random.choice(quotes))

        st.subheader("Why Adopt a Growth Mindset?")
        st.write("""
        - **✅ Embrace Challenges:** See obstacles as opportunities.  
        - **✅ Learn from Mistakes:** Errors help you grow.  
        - **✅ Persist Through Hardship:** Keep going, no matter what.  
        - **✅ Celebrate Effort:** Value hard work over results.  
        - **✅ Stay Open-Minded:** Adapt and keep learning.  
        """)

    elif page == "📝 Daily Challenges":
        st.header("🔥 Daily Challenge")

        if "completed_challenges" not in st.session_state:
            st.session_state["completed_challenges"] = []
        if "current_challenge" not in st.session_state:
            st.session_state["current_challenge"] = ""

        challenges = {
            "Mindset": [
                "Reflect on a past accomplishment and what it taught you.",
                "Reflect on a past mistake and what it taught you.",
                "Reframe a negative thought into a positive one.",
                "Write down three reasons why you're excited about the day ahead.",
                "Write down three things you're grateful for today."
            ],
            "Personal Growth and Exploration": [ 
                "Choose a new hobby or interest.",
                "Write down three things you're looking forward to doing today.",
                "Share a personal achievement with a friend or family member."
            ],
            "Social Connections": [
                "Reach out to an old friend and check in on them.",
                "Compliment someone genuinely today.",
                "Share a personal achievement with a friend or family member.",
                "Help someone with a small task or favor.",
                "Write a thank-you note or message to someone who has helped you."
            ]
        }

        category = st.selectbox("Choose a challenge category:", list(challenges.keys()))

        if st.button("🎲 Get New Challenge"):
            st.session_state["current_challenge"] = random.choice(challenges[category])

        if st.session_state["current_challenge"]:
            st.subheader("🎯 Today's Challenge")
            st.write(st.session_state["current_challenge"])

            if st.button("✅ Mark as Completed"):
                if st.session_state["current_challenge"] not in st.session_state["completed_challenges"]:
                    st.session_state["completed_challenges"].append({
                        "challenge": st.session_state["current_challenge"],
                        "date": datetime.date.today().strftime("%B %d, %Y")
                    })
                    st.success("Great job! You've completed this challenge. 🎉")
                st.session_state["current_challenge"] = ""

        if st.session_state["completed_challenges"]:
            st.subheader("🏆 Completed Challenges")
            for item in st.session_state["completed_challenges"]:
                st.write(f"- **{item['challenge']}** (📅 {item['date']})")

    elif page == "🎯 Goal Setting":
        st.header("🎯 Set Your Growth Goals")

        if "goal" not in st.session_state:
            st.session_state["goal"] = ""
        if "deadline" not in st.session_state:
            st.session_state["deadline"] = datetime.date.today()

        st.write("""
        - **✅ Break Down Your Goals:** Identify specific, achievable, relevant, and time-bound (SMART) goals.  
        - **✅ Prioritize Your Goals:** Focus on the most important goals first.  
        - **✅ Track Your Progress:** Keep a journal or spreadsheet to track your progress.  
        - **✅ Set Realistic Expectations:** Don't be discouraged by setbacks; keep moving forward!  
        """)

        goal = st.text_input("📝 Write your goal:", value=st.session_state["goal"])
        deadline = st.date_input("📅 Set a deadline:", value=st.session_state["deadline"], min_value=datetime.date.today())

        if st.button("Save Goal"):
            if goal:
                st.session_state["goal"] = goal
                st.session_state["deadline"] = deadline
                st.success(f"✅ Goal: {goal}\n📅 Deadline: {deadline.strftime('%B %d, %Y')}")
            else:
                st.warning("Please enter a goal before saving.")

        if st.button("🎉 Mark as Completed"):
            st.session_state["goal"] = ""
            st.session_state["deadline"] = datetime.date.today()
            st.success("Congrats! 🎉 You've achieved your goal!")

if __name__ == "__main__":
    main()
