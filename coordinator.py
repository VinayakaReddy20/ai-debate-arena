"""
AI Debate Arena - Multi-Agent Debate System
Coordinator Module: Manages the debate workflow and round-based interactions
"""

from agents import ProAgent, OpponentAgent, JudgeAgent


class Coordinator:
    """
    Coordinator Agent - Manages the debate workflow
    Controls debate rounds and orchestrates agent interactions
    """
    
    def __init__(self):
        self.pro_agent = ProAgent()
        self.opponent_agent = OpponentAgent()
        self.judge_agent = JudgeAgent()
        self.debate_history = {
            "topic": "",
            "rounds": [],
            "pro_arguments": [],
            "opponent_arguments": [],
            "judge_decision": None
        }
    
    def start_debate(self, topic: str) -> dict:
        """Start the debate and run all 3 rounds"""
        if not topic or not topic.strip():
            return {
                "error": "Topic cannot be empty. Please enter a debate topic."
            }
        
        self.debate_history = {
            "topic": topic.strip(),
            "rounds": [],
            "pro_arguments": [],
            "opponent_arguments": [],
            "judge_decision": None
        }
        
        # Round 1: Opening Arguments
        round_1 = self._run_round_1(topic)
        
        # Round 2: Rebuttals
        round_2 = self._run_round_2(topic, round_1)
        
        # Round 3: Final Statements
        round_3 = self._run_round_3(topic, round_2)
        
        # Judge Evaluation
        judge_decision = self._run_judge_evaluation(topic)
        
        return {
            "topic": topic,
            "round_1": round_1,
            "round_2": round_2,
            "round_3": round_3,
            "judge_decision": judge_decision,
            "success": True
        }
    
    def _run_round_1(self, topic: str) -> dict:
        """Round 1: Opening arguments from both sides"""
        pro_opening = self.pro_agent.give_opening_argument(topic)
        opponent_opening = self.opponent_agent.give_opening_argument(topic)
        
        round_data = {
            "round_name": "Round 1: Opening Arguments",
            "pro_argument": pro_opening,
            "opponent_argument": opponent_opening
        }
        
        self.debate_history["rounds"].append(round_data)
        self.debate_history["pro_arguments"].append(pro_opening)
        self.debate_history["opponent_arguments"].append(opponent_opening)
        
        return round_data
    
    def _run_round_2(self, topic: str, round_1: dict) -> dict:
        """Round 2: Rebuttals"""
        # Pro rebuts opponent's opening
        pro_rebuttal = self.pro_agent.rebut(
            topic, 
            round_1["opponent_argument"]
        )
        
        # Opponent rebuts Pro's opening
        opponent_rebuttal = self.opponent_agent.rebut(
            topic, 
            round_1["pro_argument"]
        )
        
        round_data = {
            "round_name": "Round 2: Rebuttals",
            "pro_argument": pro_rebuttal,
            "opponent_argument": opponent_rebuttal
        }
        
        self.debate_history["rounds"].append(round_data)
        self.debate_history["pro_arguments"].append(pro_rebuttal)
        self.debate_history["opponent_arguments"].append(opponent_rebuttal)
        
        return round_data
    
    def _run_round_3(self, topic: str, round_2: dict) -> dict:
        """Round 3: Final Statements"""
        # Combine all opponent arguments for Pro's final statement
        opponent_context = "\n\n".join(self.debate_history["opponent_arguments"])
        pro_final = self.pro_agent.give_final_statement(topic, opponent_context)
        
        # Combine all Pro arguments for Opponent's final statement
        pro_context = "\n\n".join(self.debate_history["pro_arguments"])
        opponent_final = self.opponent_agent.give_final_statement(topic, pro_context)
        
        round_data = {
            "round_name": "Round 3: Final Statements",
            "pro_argument": pro_final,
            "opponent_argument": opponent_final
        }
        
        self.debate_history["rounds"].append(round_data)
        self.debate_history["pro_arguments"].append(pro_final)
        self.debate_history["opponent_arguments"].append(opponent_final)
        
        return round_data
    
    def _run_judge_evaluation(self, topic: str) -> dict:
        """Judge evaluates the debate and declares winner"""
        # Combine all arguments for judge evaluation
        pro_arguments = "\n\n".join([
            f"Round {i+1}:\n{arg}" 
            for i, arg in enumerate(self.debate_history["pro_arguments"])
        ])
        
        opponent_arguments = "\n\n".join([
            f"Round {i+1}:\n{arg}" 
            for i, arg in enumerate(self.debate_history["opponent_arguments"])
        ])
        
        decision = self.judge_agent.evaluate_debate(
            topic, 
            pro_arguments, 
            opponent_arguments
        )
        
        self.debate_history["judge_decision"] = decision
        return decision
    
    def get_debate_summary(self) -> dict:
        """Get the complete debate summary"""
        return self.debate_history

