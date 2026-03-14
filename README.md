# 🤖 AI Debate Arena

A Multi-Agent Debate (MAD) system that demonstrates **Agentic AI** through a competitive debate framework where AI agents argue opposing sides of a topic and a judge evaluates to declare a winner.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![Groq](https://img.shields.io/badge/Groq-llama3--8b--8192-green.svg)

## 📚 Overview

**AI Debate Arena** implements a Multi-Agent Debate (MAD) architecture where multiple AI agents collaborate and compete to produce better reasoning and final judgment. This project demonstrates:

- **Multi-Agent Interaction**: Four specialized agents work together
- **Round-Based Debate**: Structured 3-round debate format
- **Contextual Arguments**: Agents reference previous arguments
- **Impartial Evaluation**: Judge agent provides fair assessment
- **Powered by Groq**: Ultra-fast inference with Llama 3 model

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     AI DEBATE ARENA                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌──────────────┐     ┌──────────────────────────────────┐     │
│  │    USER      │────▶│       COORDINATOR AGENT          │     │
│  │  (Input)     │     │  - Manages workflow              │     │
│  └──────────────┘     │  - Controls rounds               │     │
│                       └──────────────┬───────────────────┘     │
│                                      │                          │
│            ┌─────────────────────────┼───────────────────┐     │
│            │                         │                   │     │
│            ▼                         ▼                   ▼     │
│  ┌──────────────────┐    ┌──────────────────┐   ┌────────────┐ │
│  │   PRO AGENT      │    │  OPPONENT AGENT  │   │   JUDGE    │ │
│  │  (Affirmative)   │    │   (Negative)     │   │   AGENT    │ │
│  │                  │    │                  │   │            │ │
│  │ - Opening        │    │ - Opening        │   │ - Evaluate │ │
│  │ - Rebuttal       │    │ - Rebuttal       │   │ - Decide   │ │
│  │ - Final          │    │ - Final          │   │ - Explain  │ │
│  └──────────────────┘    └──────────────────┘   └────────────┘ │
│                                                                  │
│                         GROQ API                                 │
│                    (llama3-8b-8192)                              │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## 🎯 Debate Flow

```
ROUND 1: Opening Arguments
├── Pro Agent: Presents supporting arguments
└── Opponent Agent: Presents opposing arguments

ROUND 2: Rebuttals
├── Pro Agent: Counters opponent's arguments
└── Opponent Agent: Counters Pro's arguments

ROUND 3: Final Statements
├── Pro Agent: Summarizes why they win
└── Opponent Agent: Summarizes why they win

JUDGE EVALUATION
└── Winner declared with reasoning
```

## 🚀 Installation

### 1. Clone or Download the Project

```bash
# Navigate to project directory
cd ai-debate-arena
```

### 2. Create Virtual Environment (Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API Key

Create a `.env` file in the project root:

```bash
# Copy the example file
copy .env.example .env
```

Edit `.env` and add your Groq API key:

```env
GROQ_API_KEY=your_actual_api_key_here
```

**Get your API key from:** https://console.groq.com/keys

## ▶️ Running the Project

```bash
streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`

## 💡 Usage

1. **Enter a Topic**: Type your debate topic in the input box
2. **Start Debate**: Click the "Start Debate" button
3. **Watch the Debate**: Follow along as agents present their arguments
4. **See the Winner**: Judge evaluates and declares the winner

### Sample Topics to Try

- "Artificial Intelligence will do more harm than good"
- "Remote work should become the permanent norm"
- "Social media has a net negative effect on society"
- "Universal Basic Income is necessary for the future"
- "Space exploration is a waste of resources"

## 📖 Example Output

### Input Topic
```
"Artificial Intelligence will do more harm than good"
```

### Round 1: Opening Arguments
- **Pro Agent**: Presents arguments in favor of the topic (AI causing harm)
- **Opponent Agent**: Presents counter-arguments (AI benefits)

### Round 2: Rebuttals
- **Pro Agent**: Challenges opponent's points about AI benefits
- **Opponent Agent**: Defends AI's positive impact

### Round 3: Final Statements
- **Pro Agent**: Summarizes key harms of AI
- **Opponent Agent**: Emphasizes AI's transformative benefits

### Judge's Decision
```
WINNER: Pro Agent / Opponent Agent

REASONING: [Detailed explanation of why one side won]
```

## 📁 Project Structure

```
ai-debate-arena/
├── app.py              # Streamlit UI application
├── agents.py           # Pro, Opponent, and Judge agent classes
├── coordinator.py      # Debate workflow management
├── requirements.txt    # Python dependencies
├── .env.example        # Environment variables template
└── README.md           # This file
```

## 🔧 Configuration Options

You can customize the project by modifying environment variables:

| Variable | Description | Default |
|----------|-------------|---------|
| `GROQ_API_KEY` | Your Groq API key | Required |
| `MODEL` | Model to use | llama3-8b-8192 |

## ⚠️ Troubleshooting

### "API Key not found" Error
- Make sure `.env` file exists in the project directory
- Verify the API key is correct
- Check that `python-dotenv` is installed

### "Error running debate" 
- Check your internet connection
- Verify API key has sufficient credits
- Try again - sometimes APIs have temporary issues

### Streamlit port already in use
```bash
streamlit run app.py --port 8502
```

## 🎓 Learning Outcomes

This project demonstrates:

1. **Agentic AI**: Autonomous agents working together
2. **Multi-Agent Systems**: Specialized agents with distinct roles
3. **Competitive AI**: Agents challenging each other's arguments
4. **Reasoning & Evaluation**: Critical thinking through AI
5. **Human-AI Interaction**: Natural language debate interface
6. **Groq API Integration**: Fast LLM inference with Llama 3

## 📄 License

This project is for educational purposes.

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [Groq](https://groq.com/) (Llama 3 8B)
- Inspired by Multi-Agent Debate (MAD) research

---

*Made with ❤️ for AI enthusiasts*

