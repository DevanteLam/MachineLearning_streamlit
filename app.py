import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# 设置页面配置
st.set_page_config(
    page_title="AI Course Recommender",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 自定义CSS样式
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        width: 100%;
        background-color: #0066cc;
        color: white;
    }
    .metric-card {
        background-color: white;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# 主标题
st.title('🎓 Enterprise Course Recommender System')

# 创建三列布局
left_col, main_col, right_col = st.columns([1, 2, 1])

with main_col:
    st.header('Personalized Learning Path')
    
    # 技能评估部分
    with st.expander("🎯 Skill Assessment", expanded=True):
        st.subheader("Current Expertise")
        domains = {
            'Data Science': ['Python', 'R', 'SQL', 'Statistics'],
            'Machine Learning': ['Scikit-learn', 'TensorFlow', 'PyTorch'],
            'Web Development': ['JavaScript', 'React', 'Node.js'],
            'Cloud Computing': ['AWS', 'Azure', 'GCP'],
            'DevOps': ['Docker', 'Kubernetes', 'Jenkins']
        }
        
        selected_domain = st.selectbox('Select Your Primary Domain:', list(domains.keys()))
        selected_skills = st.multiselect('Your Current Skills:', domains[selected_domain])
        
        experience_level = st.select_slider(
            'Years of Experience:',
            options=['0-1', '1-3', '3-5', '5-10', '10+'],
            value='1-3'
        )

# 侧边栏设置
with st.sidebar:
    st.header('Learning Preferences')
    
    with st.expander("🎯 Learning Goals", expanded=True):
        career_goals = st.multiselect(
            'Career Objectives:',
            ['Data Scientist', 'ML Engineer', 'Full-Stack Developer', 'Cloud Architect', 'DevOps Engineer']
        )
        
        target_skills = st.multiselect(
            'Target Skills:',
            ['AI/ML', 'Cloud Computing', 'Web Development', 'Data Engineering', 'DevOps']
        )
    
    with st.expander("⚙️ Learning Settings", expanded=True):
        study_pace = st.select_slider(
            'Preferred Study Pace:',
            options=['Light', 'Moderate', 'Intensive'],
            value='Moderate'
        )
        
        weekly_commitment = st.slider(
            'Weekly Time Commitment (hours):',
            min_value=2,
            max_value=40,
            value=10
        )
        
        learning_style = st.multiselect(
            'Preferred Learning Style:',
            ['Video Lectures', 'Interactive Labs', 'Project-Based', 'Reading Materials']
        )

# 课程推荐结果
with main_col:
    st.header('Recommended Learning Paths')
    
    paths = {
        'Data Science Track': {
            'courses': ['Advanced Python Programming', 'Statistical Learning', 'Machine Learning Fundamentals'],
            'duration': '12 weeks',
            'rating': 4.8,
            'enrolled': 12500
        },
        'ML Engineering Track': {
            'courses': ['Deep Learning Specialization', 'MLOps Fundamentals', 'Production ML Systems'],
            'duration': '16 weeks',
            'rating': 4.9,
            'enrolled': 15000
        }
    }
    
    for path_name, path_info in paths.items():
        with st.expander(f"📚 {path_name}", expanded=True):
            col1, col2 = st.columns([3,1])
            with col1:
                st.markdown(f"**Duration:** {path_info['duration']}")
                st.markdown("**Courses:**")
                for course in path_info['courses']:
                    st.markdown(f"- {course}")
            with col2:
                st.metric("Rating", f"⭐ {path_info['rating']}")
                st.metric("Enrolled", f"👥 {path_info['enrolled']:,}")
                st.button('Enroll Now', key=path_name)

# 右侧统计数据
with right_col:
    st.header('Analytics')
    
    # 使用Plotly创建更漂亮的图表
    difficulty_data = pd.DataFrame({
        'Level': ['Beginner', 'Intermediate', 'Advanced'],
        'Count': [30, 45, 25]
    })
    
    fig = px.bar(difficulty_data, x='Level', y='Count',
                 title='Course Distribution by Level',
                 color='Count',
                 color_continuous_scale='blues')
    st.plotly_chart(fig, use_container_width=True)
    
    # 领域分布环形图
    domain_data = pd.DataFrame({
        'Domain': ['Data Science', 'ML', 'Web Dev', 'Cloud', 'DevOps'],
        'Courses': [35, 30, 20, 15, 10]
    })
    
    fig = px.pie(domain_data, values='Courses', names='Domain',
                 title='Course Distribution by Domain',
                 hole=0.4)
    st.plotly_chart(fig, use_container_width=True)

# 底部统计
with main_col:
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Learners", "100,000+", "↑ 15%")
    with col2:
        st.metric("Course Completion Rate", "87%", "↑ 5%")
    with col3:
        st.metric("Avg. Satisfaction", "4.8/5", "↑ 0.2")