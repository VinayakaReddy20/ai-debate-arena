# 🤖 AI Debate Arena

A Multi-Agent Debate (MAD) system that demonstrates **Agentic AI** through a competitive debate framework where AI agents argue opposing sides of a topic and a judge evaluates to declare a winner.

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

