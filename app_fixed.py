"""
AI Debate Arena - Multi-Agent Debate System
Streamlit UI: Modern dark theme debate arena with high contrast and professional layout
"""

import streamlit as st
import os
from dotenv import load_dotenv
from coordinator import Coordinator

# Load environment variables
load_dotenv()

# Page configuration per spec
st.set_page_config(
    page_title="AI Debate Arena",
    page_icon="🤖",
    layout="wide"
)

# Custom CSS for dark debate arena theme with high contrast
st.markdown("""
<style>
    /* Dark gradient background */
    .stApp {
        background: linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 50%, #16213e 100%);
        color: #FFFFFF;
    }
    
    /* High contrast text */
    h1, h2, h3, h4, h5, h6 {
        color: #FFFFFF !important;
        text-shadow: 0 2px 4px rgba(0,0,0,0.5);
    }
    
    .stTextInput > div > div > input {
        background-color: #2d3748;
        color: #E5E7EB;
        border: 1px solid #4a5568;
    }
    
    /* Header */
    .main-header {
        font-size: 4rem;
        font-weight: bold;
        text-align: center;
        background: linear-gradient(135deg, #2563EB, #1d4ed8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 0.5rem;
    }
    
    .sub-header {
        font-size: 1.8rem;
        text-align: center;
        color: #E5E7EB;
        margin-bottom: 2rem;
    }
    
    /* Debate stage containers */
    .round-container {
        background: rgba(255,255,255,0.05);
        border-radius: 15px;
        padding: 2rem;
        margin-bottom: 2rem;
        border: 1px solid rgba(255,255,255,0.1);
        backdrop-filter: blur(10px);
    }
    
    /* Pro Agent (blue) */
    .pro-box {
        background: linear-gradient(135deg, #2563EB 0%, #1d4ed8 100%);
        color: #FFFFFF;
        padding: 1.5rem;
        border-radius: 12px;
        margin-bottom: 1rem;
        box-shadow: 0 8px 32px rgba(37,99,235,0.3);
        border-left: 5px solid #60a5fa;
    }
    
    /* Opponent Agent (red) */
    .opp-box {
        background: linear-gradient(135deg, #DC2626 0%, #b91c1c 100%);
        color: #FFFFFF;
        padding: 1.5rem;
        border-radius: 12px;
        margin-bottom: 1rem;
        box-shadow: 0 8px 32px rgba(220,38,38,0.3);
        border-left: 5px solid #f87171;
    }
    
    /* Judge/Gold */
    .judge-box {
        background: linear-gradient(135deg, #FACC15 0%, #eab308 100%);
        color: #000000;
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 10px 40px rgba(250,204,21,0.4);
        border: 3px solid #fde047;
        font-weight: bold;
    }
    
    .winner-pro {
        border: 4px solid #60a5fa;
        background: linear-gradient(135deg, #2563EB, #1d4ed8);
    }
    
    .winner-opp {
        border: 4px solid #f87171;
        background: linear-gradient(135deg, #DC2626, #b91c1c);
    }
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #2563EB 0%, #1d4ed8 100%);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 1rem 2rem;
        font-size: 1.1rem;
        font-weight: bold;
        box-shadow: 0 4px 15px rgba(37,99,235,0.4);
        width: 100%;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(37,99,235,0.5);
    }
    
    /* Progress */
    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, #2563EB, #FACC15);
    }
    
    /* Topic display */
    .topic-display {
        background: rgba(255,255,255,0.1);
        border: 2px solid #FACC15;
        border-radius: 15px;
        padding: 2rem;
        text-align: center;
        font-size: 1.5rem;
        font-weight: bold;
        color: #FACC15;
        margin-bottom: 2rem;
    }
    
    /* Sidebar dark */
    .css-1d391kg {
        background: #1a1a2e;
    }
    
    /* Responsive columns */
    @media (max-width: 768px) {
        .main-header { font-size: 2.5rem; }
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Header per spec
    st.markdown('<h1 class="main-header">🤖 AI Debate Arena</h1>', unsafe_allow_html=True)
    st.markdown('<h2 class="sub-header">Multi-Agent Debate System</h2>', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.header("ℹ️ Debate Arena")
        st.markdown("""
        **Modern Multi-Agent Debate System**
        
        🎯 **Pro Agent (👍)**: Argues FOR the topic  
        🎯 **Opponent Agent (⚔️)**: Argues AGAINST
        🎯 **Judge (⚖️)**: Decides winner
        
        3 Rounds: Opening → Rebuttals → Finals
        """)
        
        st.header("🔑 API Setup")
        if os.getenv("GROQ_API_KEY"):
            st.success("✅ Groq API Ready")
        else:
            st.error("❌ Set GROQ_API_KEY in .env")
    
    # Input section in container
    input_container = st.container()
    with input_container:
        st.markdown("### 📝 Enter Debate Topic")
        topic = st.text_input(
            "Debate Topic",
            placeholder="Artificial Intelligence will do more harm than good...",
            help="Clear, debatable topic works best"
        )
        
        # Start button
        col_btn1, col_btn2 = st.columns(2)
        with col_btn1:
            if st.button("🚀 Start Debate", type="primary"):
                if not topic.strip():
                    st.error("Please enter a topic!")
                elif not os.getenv("GROQ_API_KEY"):
                    st.error("Set GROQ_API_KEY!")
                else:
                    st.session_state['debate_topic'] = topic.strip()
                    st.rerun()
        
        # Sample topics per spec (2 columns)
        st.markdown("**💡 Quick Start Samples:**")
        samples = [
            "Artificial Intelligence will do more harm than good",
            "Remote work is more productive than office work",
            "Social media does more harm than good"
        ]
        sample_cols = st.columns(3)
        for i, sample in enumerate(samples):
            with sample_cols[i]:
                if st.button(sample[:35] + "...", key=f"sample{i}"):
                    st.session_state['debate_topic'] = sample
                    st.rerun()
    
    # Run debate if topic ready
    if st.session_state.get('debate_topic'):
        run_debate(st.session_state['debate_topic'])
        if st.button("🔄 New Debate"):
            del st.session_state['debate_topic']
            st.rerun()

def run_debate(topic: str):
    with st.spinner("⚡ Initializing Debate Arena..."):
        coordinator = Coordinator()
        progress_bar = st.progress(0)
        status = st.empty()
        
        try:
            status.text("📢 Round 1: Opening Arguments")
            progress_bar.progress(20)
            result = coordinator.start_debate(topic) or {}
            
            if "error" in result or not result:
                st.warning(result.get("error", "Failed to generate debate. Check API keys."))
                return
            
            # Topic display
            topic_name = result.get("topic", topic)
            st.markdown(f'<div class="topic-display">📌 Debate Topic: {topic_name}</div>', unsafe_allow_html=True)
            
            # Round 1
            progress_bar.progress(40)
            display_round(result.get("round_1", {}), "1 – Opening Arguments")
            
            # Round 2
            status.text("⚔️ Round 2: Rebuttals")
            progress_bar.progress(60)
            display_round(result.get("round_2", {}), "2 – Rebuttals")
            st.divider()
            
            # Round 3
            status.text("🎯 Round 3: Final Statements")
            progress_bar.progress(80)
            display_round(result.get("round_3", {}), "3 – Final Statements")
            
            # Judge
            progress_bar.progress(100)
            display_judge_decision(result.get("judge_decision", {}))
            status.text("✅ Debate Complete!")
            
        except Exception as e:
            st.warning("⚠ Unable to generate debate response. Please check the API configuration.")

def display_round(round_data: dict, round_title: str):
    st.markdown(f'<div class="round-container"><h2>Round {round_title}</h2></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        st.markdown("### 👍 **Pro Agent**")
        pro_argument = round_data.get("pro_argument", "")
        if isinstance(pro_argument, str) and len(pro_argument.strip()) > 10:
            st.markdown(f'<div class="pro-box">{pro_argument}</div>', unsafe_allow_html=True)
        else:
            st.warning("⚠ Pro argument not available. Please check API configuration.")
    
    with col2:
        st.markdown("### ⚔️ **Opponent Agent**")
        opponent_argument = round_data.get("opponent_argument", "")
        if isinstance(opponent_argument, str) and len(opponent_argument.strip()) > 10:
            st.markdown(f'<div class="opp-box">{opponent_argument}</div>', unsafe_allow_html=True)
        else:
            st.warning("⚠ Opponent argument not available. Please check API configuration.")

def display_judge_decision(decision: dict):
    st.markdown('<h1 style="color: #FACC15; text-align: center;">⚖️ Judge Decision</h1>', unsafe_allow_html=True)
    
    winner = decision.get("winner", "Tie")
    reasoning = decision.get("reasoning", "No analysis available.")
    if not isinstance(reasoning, str) or len(reasoning.strip()) < 10:
        st.warning("⚠ Judge analysis not available. Please check API configuration.")
        return
    
    # Winner highlight
    winner_class = "winner-pro" if "Pro" in winner else "winner-opp" if "Opponent" in winner else ""
    st.markdown(f'''
    <div class="judge-box {winner_class}">
        <h2>🏆 **{winner} Wins!**</h2>
    </div>
    <div class="judge-box" style="background: rgba(255,255,255,0.1); color: #E5E7EB;">
        <h3>📜 Analysis</h3>
        <p>{reasoning}</p>
    </div>
    ''', unsafe_allow_html=True)

if __name__ == "__main__":
    main()

