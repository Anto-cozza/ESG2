import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
from datetime import datetime, timedelta

# Set page configuration
st.set_page_config(
    page_title="GreenInvestEdu – ESG Investment Learning for Everyone",
    page_icon="🌱",
    layout="wide"
)

# Add a title
st.title("🌱 GreenInvestEdu – ESG Investment Learning for Everyone")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to",
    ["Home Dashboard", "Learning Path", "ESG Financial Products", "ESG Profile Advisor", "Gamification & Rewards"]
)

# User Data
user_name = "Marco"
completed_modules = 3
total_modules = 6
esg_score = 72

# Create page content based on selection
if page == "Home Dashboard":
    st.header(f"Welcome back, {user_name}!")
    st.subheader("Your Learning Progress")
    
    # Progress bar
    progress = completed_modules / total_modules
    st.progress(progress)
    st.write(f"You've completed {completed_modules} out of {total_modules} modules")
    
    # ESG Score
    st.subheader("Your ESG Score")
    col1, col2 = st.columns([1, 3])
    with col1:
        # Display the score in a circle
        if esg_score >= 80:
            color = "green"
        elif esg_score >= 60:
            color = "orange"
        else:
            color = "red"
        
        st.markdown(f"""
        <div style="width:100px;height:100px;border-radius:50%;background-color:{color};
                    display:flex;align-items:center;justify-content:center;color:white;
                    font-size:30px;font-weight:bold;">
            {esg_score}
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.write("Your ESG score reflects your understanding of sustainable investing concepts.")
        st.write("Complete more modules to improve your score!")
    
    # News Feed
    st.subheader("ESG News Feed")
    
    news = [
        {
            "title": "EU Announces New Green Bond Standards",
            "summary": "The European Union has unveiled stricter standards for green bonds to combat greenwashing."
        },
        {
            "title": "Solar Energy Investments Hit Record High",
            "summary": "Global investments in solar energy projects reached $320 billion in Q1 2025."
        },
        {
            "title": "Major Asset Managers Pledge Net-Zero Portfolios by 2040",
            "summary": "A coalition of investment firms have committed to carbon-neutral investment portfolios."
        }
    ]
    
    for item in news:
        st.markdown(f"""
        <div style="padding:10px;border-left:4px solid #1E8449;margin-bottom:10px;">
            <h4>{item['title']}</h4>
            <p>{item['summary']}</p>
        </div>
        """, unsafe_allow_html=True)

elif page == "Learning Path":
    st.header("Personalized Learning Path")
    st.write("Build your ESG investment knowledge one module at a time.")
    
    # Overall progress
    st.subheader("Overall Progress")
    progress = completed_modules / total_modules
    st.progress(progress)
    st.write(f"{int(progress*100)}% Complete")
    
    # Module list
    modules = [
        {"id": 1, "title": "Introduction to ESG Investing", "completed": True, "progress": 100},
        {"id": 2, "title": "Understanding ESG Ratings", "completed": True, "progress": 100},
        {"id": 3, "title": "Green Bonds Explained", "completed": True, "progress": 100},
        {"id": 4, "title": "Sustainable ETFs and Mutual Funds", "completed": False, "progress": 45},
        {"id": 5, "title": "ESG Risk Assessment", "completed": False, "progress": 0},
        {"id": 6, "title": "Impact Investing Principles", "completed": False, "progress": 0}
    ]
    
    # Display modules
    for module in modules:
        status = "✅ Completed" if module["completed"] else f"🔄 {module['progress']}% Complete" if module["progress"] > 0 else "🔒 Not Started"
        
        expander = st.expander(f"Module {module['id']}: {module['title']} - {status}")
        with expander:
            st.progress(module["progress"]/100)
            
            if module["completed"]:
                st.success("You've completed this module!")
            elif module["progress"] > 0:
                st.info("Continue where you left off")
                if st.button("Continue Module", key=f"continue_{module['id']}"):
                    st.write("Module content would load here...")
            else:
                if st.button("Start Module", key=f"start_{module['id']}"):
                    st.write("Module content would load here...")

elif page == "ESG Financial Products":
    st.header("ESG Financial Products")
    st.write("Explore sustainable investment options aligned with your values.")
    
    # Create sample product data
    products = pd.DataFrame({
        'Name': [
            'GreenGrowth Global Equity Fund', 
            'BlueWater Clean Ocean Bond', 
            'SustainTech Innovation ETF',
            'Climate Action Corporate Bond',
            'Renewable Energy Leaders Index'
        ],
        'Type': [
            'Equity Fund', 
            'Green Bond', 
            'ETF',
            'Corporate Bond',
            'Index Fund'
        ],
        'ESG_Rating': [
            'AAA', 
            'AA', 
            'AAA',
            'A',
            'AA'
        ],
        'Risk_Level': [
            'Medium', 
            'Low', 
            'Medium-High',
            'Low',
            'Medium'
        ],
        'Expected_Return': [
            '7-9%', 
            '3-4%', 
            '8-11%',
            '3-5%',
            '6-8%'
        ]
    })
    
    # Filters
    st.subheader("Filter Products")
    col1, col2 = st.columns(2)
    
    with col1:
        product_type = st.multiselect(
            "Product Type:",
            options=products['Type'].unique(),
            default=products['Type'].unique()
        )
    
    with col2:
        esg_rating = st.multiselect(
            "ESG Rating:",
            options=products['ESG_Rating'].unique(),
            default=products['ESG_Rating'].unique()
        )
    
    # Apply filters
    filtered_products = products[
        (products['Type'].isin(product_type)) &
        (products['ESG_Rating'].isin(esg_rating))
    ]
    
    # Display products
    st.subheader(f"Showing {len(filtered_products)} products")
    st.dataframe(filtered_products)
    
    # Product details
    if len(filtered_products) > 0:
        st.subheader("Product Details")
        selected_product = st.selectbox("Select a product for more information:", filtered_products['Name'])
        
        product = filtered_products[filtered_products['Name'] == selected_product].iloc[0]
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.write(f"**Name:** {product['Name']}")
            st.write(f"**Type:** {product['Type']}")
            st.write(f"**ESG Rating:** {product['ESG_Rating']}")
            st.write(f"**Risk Level:** {product['Risk_Level']}")
            st.write(f"**Expected Return:** {product['Expected_Return']}")
            
            # Simulated performance chart
            st.subheader("12-Month Performance")
            np.random.seed(42)
            data = np.cumsum(np.random.normal(0.005, 0.03, 12))
            chart_data = pd.DataFrame(data, columns=["Returns"])
            st.line_chart(chart_data)
            
        with col2:
            st.subheader("ESG Breakdown")
            env_score = random.randint(60, 95)
            soc_score = random.randint(55, 90)
            gov_score = random.randint(65, 95)
            
            st.write("Environmental")
            st.progress(env_score/100)
            st.write("Social")
            st.progress(soc_score/100)
            st.write("Governance")
            st.progress(gov_score/100)

elif page == "ESG Profile Advisor":
    st.header("ESG Profile Advisor")
    st.write("Discover your sustainable investor profile through a personalized assessment.")
    
    if 'profile_complete' not in st.session_state:
        st.session_state.profile_complete = False
    
    if not st.session_state.profile_complete:
        st.subheader("ESG Investment Profile Questionnaire")
        st.write("Answer these 5 questions to receive your personalized ESG investor profile.")
        
        # Questions
        questions = [
            {
                "question": "How important is environmental impact in your investment decisions?",
                "options": ["Not important", "Somewhat important", "Very important", "It's my top priority"]
            },
            {
                "question": "Which area of ESG are you most interested in?",
                "options": ["Environmental issues", "Social responsibility", "Corporate governance", "All equally"]
            },
            {
                "question": "How much of your portfolio would you dedicate to ESG investments?",
                "options": ["Less than 10%", "10-25%", "25-50%", "More than 50%"]
            },
            {
                "question": "What's your primary motivation for sustainable investing?",
                "options": ["Financial returns", "Risk management", "Positive impact", "Aligning with personal values"]
            },
            {
                "question": "What investment time horizon do you typically consider?",
                "options": ["Short-term (< 1 year)", "Medium-term (1-5 years)", "Long-term (5+ years)"]
            }
        ]
        
        # Display questions
        with st.form("profile_questionnaire"):
            responses = []
            
            for i, q in enumerate(questions):
                st.write(f"**{i+1}. {q['question']}**")
                response = st.radio(f"Question {i+1}", options=q['options'], key=f"q{i}")
                responses.append(response)
                st.write("---")
            
            submitted = st.form_submit_button("Get My ESG Profile")
            
            if submitted:
                st.session_state.profile_complete = True
                st.session_state.responses = responses
    
    if st.session_state.profile_complete:
        st.subheader("Your ESG Investor Profile")
        
        # Determine profile based on responses
        profiles = [
            "Green Explorer",
            "Impact Seeker",
            "Sustainable Wealth Builder",
            "ESG Risk Manager",
            "Balanced ESG Integrator"
        ]
        
        # Using deterministic mapping based on mock responses
        if hasattr(st.session_state, 'responses'):
            # Use a simplified approach for the demo
            responses = st.session_state.responses
            if "Very important" in responses or "It's my top priority" in responses:
                profile = "Impact Seeker"
            elif "Risk management" in responses:
                profile = "ESG Risk Manager"
            elif "More than 50%" in responses:
                profile = "Sustainable Wealth Builder"
            elif "All equally" in responses:
                profile = "Balanced ESG Integrator"
            else:
                profile = "Green Explorer"
            
            st.markdown(f"""
            <div style="text-align:center; font-size:24px; font-weight:bold; color:#1E8449; margin:20px 0;">
                {profile}
            </div>
            """, unsafe_allow_html=True)
            
            # Profile descriptions
            descriptions = {
                "Green Explorer": "You're taking your first steps into sustainable investing with a balanced approach.",
                "Impact Seeker": "Your primary motivation is making a positive difference through your investments.",
                "Sustainable Wealth Builder": "You see ESG as a smart long-term strategy for growth and returns.",
                "ESG Risk Manager": "You recognize ESG factors as material risks and take a defensive approach.",
                "Balanced ESG Integrator": "You take a holistic view of ESG alongside traditional metrics."
            }
            
            st.write(descriptions[profile])
            
            # Recommendations
            st.subheader("Recommended Investment Approach")
            st.write("- Focus on products that align with your values")
            st.write("- Consider your time horizon when selecting ESG investments")
            st.write("- Review ESG ratings for transparency")
            st.write("- Regularly reassess your portfolio to meet your goals")
            
            # Reset button
            if st.button("Retake Assessment"):
                st.session_state.profile_complete = False

elif page == "Gamification & Rewards":
    st.header("Gamification & Rewards")
    st.write("Track your achievements and compete with other sustainable investors.")
    
    tab1, tab2, tab3 = st.tabs(["Achievement Badges", "Weekly Goals", "Leaderboard"])
    
    with tab1:
        st.subheader("Your Achievement Badges")
        
        badges = [
            {"name": "ESG Rookie", "earned": True, "icon": "🌱"},
            {"name": "Quiz Master", "earned": True, "icon": "🎯"},
            {"name": "Green Bond Explorer", "earned": True, "icon": "🔍"},
            {"name": "Sustainability Advocate", "earned": True, "icon": "📣"},
            {"name": "Carbon Neutral", "earned": False, "icon": "♻️"},
            {"name": "ESG Portfolio Builder", "earned": False, "icon": "📊"},
            {"name": "Impact Investor", "earned": False, "icon": "🌍"},
            {"name": "Sustainable Finance Pro", "earned": False, "icon": "🏆"}
        ]
        
        # Display badges in a grid
        cols = st.columns(4)
        for i, badge in enumerate(badges):
            with cols[i % 4]:
                if badge["earned"]:
                    st.markdown(f"""
                    <div style="text-align:center; padding:15px; background-color:#d4edda; border-radius:10px; margin-bottom:10px;">
                        <div style="font-size:36px;">{badge['icon']}</div>
                        <div style="font-weight:bold;">{badge['name']}</div>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div style="text-align:center; padding:15px; background-color:#f8f9fa; border-radius:10px; 
                         opacity:0.7; filter:grayscale(1); margin-bottom:10px;">
                        <div style="font-size:36px;">{badge['icon']}</div>
                        <div style="font-weight:bold;">{badge['name']}</div>
                        <div style="font-size:0.8rem; color:#6c757d;">Locked</div>
                    </div>
                    """, unsafe_allow_html=True)
    
    with tab2:
        st.subheader("Weekly Goals")
        
        goals = [
            {"title": "Complete 2 learning modules", "progress": 1, "target": 2, "icon": "📚"},
            {"title": "Take 3 module quizzes", "progress": 2, "target": 3, "icon": "✏️"},
            {"title": "Read 2 ESG news articles", "progress": 2, "target": 2, "icon": "📰"}
        ]
        
        for goal in goals:
            progress_pct = goal["progress"] / goal["target"]
            completed = goal["progress"] >= goal["target"]
            
            col1, col2 = st.columns([1, 4])
            with col1:
                st.markdown(f"<div style='font-size:36px;'>{goal['icon']}</div>", unsafe_allow_html=True)
            with col2:
                st.write(f"**{goal['title']}**")
                st.write(f"Progress: {goal['progress']}/{goal['target']}")
                st.progress(progress_pct)
                if completed:
                    st.success("Completed!")
    
    with tab3:
        st.subheader("ESG Investors Leaderboard")
        
        leaderboard = pd.DataFrame({
            'Rank': [1, 2, 3, 4, 5],
            'Name': ['Julia', user_name, 'Lucas', 'Sofia', 'Carlos'],
            'Score': [850, 720, 680, 645, 590],
            'Badges': [7, 4, 5, 4, 3]
        })
        
        st.dataframe(leaderboard, use_container_width=True)
        
        # Bar chart
        st.bar_chart(leaderboard.set_index('Name')['Score'])

# Add footer
st.markdown("""
<div style="text-align:center; padding:20px; font-size:0.8rem; color:#6c757d; margin-top:30px;">
    GreenInvestEdu – ESG Investment Learning for Everyone<br>
    © 2025 GreenInvestEdu. All rights reserved. This is a demonstration app.
</div>
""", unsafe_allow_html=True)
