from local_llm import LocalLLM
from prompt_engine import build_candidate_intro_prompt
import re

class Chatbot:
    def __init__(self):
        self.candidate_info = None
        self.llm = LocalLLM()

    def set_candidate_info(self, info: dict):
        self.candidate_info = info

    def has_candidate_info(self) -> bool:
        return self.candidate_info is not None

    def generate_questions(self) -> dict:
        if not self.candidate_info:
            return {}

        prompt = build_candidate_intro_prompt(self.candidate_info)
        llm_output = self.llm.ask(prompt, max_new_tokens=800)

        # Extract questions per tech (simple heuristic using tech names)
        tech_stack = [t.strip() for t in self.candidate_info['tech_stack'].split(",")]
        tech_q_dict = {tech: [] for tech in tech_stack}

        current_tech = None
        for line in llm_output.splitlines():
            line = line.strip()
            if not line:
                continue

            # Detect if this line is a tech section heading
            for tech in tech_stack:
                if re.search(fr'\b{tech}\b', line, re.IGNORECASE) and ':' in line:
                    current_tech = tech
                    break

            if re.match(r"^\d+\.", line) and current_tech:
                tech_q_dict[current_tech].append(line)

        return tech_q_dict
