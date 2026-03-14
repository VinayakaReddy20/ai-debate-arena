"""
AI Debate Arena - Multi-Agent Debate System
Agents Module: Contains Pro, Opponent, and Judge agent implementations
"""

import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Groq model configuration
MODEL = "llama-3.1-8b-instant"


class BaseAgent:
    """Base class for all debate agents"""
    
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role
        self.messages = []
    
    def generate_response(self, system_prompt: str, user_prompt: str) -> str:
        """Generate response using Groq API"""
        try:
            response = client.chat.completions.create(
                model=MODEL,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.7,
                max_tokens=500
            )
            return response.choices[0].message.content
        except Exception:
            return "⚠ Unable to generate debate response. Please check the API configuration."


class ProAgent(BaseAgent):
    """Pro Agent - Argues in favor of the debate topic"""
    
    def __init__(self):
        super().__init__("Pro Agent", "affirmative")
        self.system_prompt = """You are Pro Agent, an expert debate participant who argues 
        IN FAVOR of the given topic. You are logical, persuasive, and provide strong 
        arguments to support the affirmative position. Your goal is to convince the 
        judge that the topic is correct/progressive/beneficial."""
    
    def give_opening_argument(self, topic: str) -> str:
        """Generate opening argument supporting the topic"""
        prompt = f"""Topic: {topic}

Provide a strong opening argument in favor of this topic. 
Focus on:
- Main supporting points
- Logical reasoning
- Real-world implications

Keep it concise but persuasive (100-150 words)."""
        return self.generate_response(self.system_prompt, prompt)
    
    def rebut(self, topic: str, opponent_argument: str) -> str:
        """Rebut opponent's arguments"""
        prompt = f"""Topic: {topic}

Opponent's argument:
{opponent_argument}

Rebut the opponent's arguments and defend your position.
Address their points and explain why they are flawed or incomplete.
Keep it concise (100-150 words)."""
        return self.generate_response(self.system_prompt, prompt)
    
    def give_final_statement(self, topic: str, opponent_arguments: str) -> str:
        """Give final closing statement"""
        prompt = f"""Topic: {topic}

Opponent's arguments throughout the debate:
{opponent_arguments}

Provide a strong final statement summarizing why you win this debate.
Focus on:
- Key strengths of your arguments
- Weaknesses in opponent's position
- Compelling conclusion

Keep it concise but impactful (100-150 words)."""
        return self.generate_response(self.system_prompt, prompt)


class OpponentAgent(BaseAgent):
    """Opponent Agent - Argues against the debate topic"""
    
    def __init__(self):
        super().__init__("Opponent Agent", "negative")
        self.system_prompt = """You are Opponent Agent, an expert debate participant who argues 
        AGAINST the given topic. You are critical, analytical, and provide strong 
        counter-arguments to challenge the affirmative position. Your goal is to 
        convince the judge that the topic is incorrect/harmful/flawed."""
    
    def give_opening_argument(self, topic: str) -> str:
        """Generate opening argument against the topic"""
        prompt = f"""Topic: {topic}

Provide a strong opening argument against this topic.
Focus on:
- Main opposing points
- Logical flaws in the proposition
- Potential negative implications

Keep it concise but persuasive (100-150 words)."""
        return self.generate_response(self.system_prompt, prompt)
    
    def rebut(self, topic: str, pro_argument: str) -> str:
        """Rebut Pro's arguments"""
        prompt = f"""Topic: {topic}

Pro Agent's argument:
{pro_argument}

Rebut the Pro Agent's arguments and defend your position.
Point out flaws, provide counter-evidence, and challenge their reasoning.
Keep it concise (100-150 words)."""
        return self.generate_response(self.system_prompt, prompt)
    
    def give_final_statement(self, topic: str, pro_arguments: str) -> str:
        """Give final closing statement"""
        prompt = f"""Topic: {topic}

Pro Agent's arguments throughout the debate:
{pro_arguments}

Provide a strong final statement summarizing why you win this debate.
Focus on:
- Key weaknesses in opponent's arguments
- Strengths of your counter-position
- Compelling conclusion

Keep it concise but impactful (100-150 words)."""
        return self.generate_response(self.system_prompt, prompt)


class JudgeAgent(BaseAgent):
    """Judge Agent - Evaluates arguments and decides winner"""
    
    def __init__(self):
        super().__init__("Judge Agent", "evaluator")
        self.system_prompt = """You are Judge Agent, an impartial and expert debate judge.
        You evaluate arguments from both sides fairly and objectively. 
        You consider logic, evidence, reasoning quality, and persuasion.
        Your decision should be well-reasoned and unbiased."""
    
    def evaluate_debate(self, topic: str, pro_arguments: str, opponent_arguments: str) -> dict:
        """Evaluate the debate and decide winner"""
        prompt = f"""Debate Topic: {topic}

PRO AGENT ARGUMENTS:
{pro_arguments}

OPPONENT AGENT ARGUMENTS:
{opponent_arguments}

Evaluate both sides fairly and decide the winner. Consider:
1. Logical strength of arguments
2. Quality of reasoning
3. Effectiveness of rebuttals
4. Persuasion and clarity
5. Overall debate performance

Provide your decision in this format:
WINNER: [Pro Agent / Opponent Agent]
REASONING: [Explain why this side won, referencing specific arguments]
SCORES: [Rate each side 1-10 with brief justification]"""
        
        result = self.generate_response(self.system_prompt, prompt)
        
        # Parse the result
        lines = result.split('\n')
        winner = "Pro Agent"
        reasoning = result
        
        for line in lines:
            if line.startswith("WINNER:"):
                winner = line.replace("WINNER:", "").strip()
            elif line.startswith("REASONING:"):
                reasoning = line.replace("REASONING:", "").strip()
        
        return {
            "winner": winner,
            "reasoning": reasoning,
            "topic": topic
        }

