
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

class LocalLLM:
    def __init__(self, model_id="microsoft/phi-2"):
        print("Loading Phi-2 model...")
        self.tokenizer = AutoTokenizer.from_pretrained(model_id)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_id,
            torch_dtype="float32",
            device_map={"": "cpu"},
            low_cpu_mem_usage=True
        )
        self.pipeline = pipeline("text-generation", model=self.model, tokenizer=self.tokenizer)

    def ask(self, prompt: str, max_new_tokens=300) -> str:
        print("Generating response...")
        output = self.pipeline(prompt, max_new_tokens=max_new_tokens, do_sample=True, temperature=0.7)
        return output[0]['generated_text'].replace(prompt, "").strip()
