from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

model_id = "google/gemma-2b-it"

# Force CPU loading
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    device_map=None,  # no auto dispatch
    torch_dtype="auto"
)

gemma_pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    device=-1  # CPU only
)

def generate_summary(ipc_desc, bns_desc):
    prompt = f"""
You are a legal expert AI. Compare the following IPC and BNS law sections:
1. Describe the similarities between them.
2. Describe the differences in terms of punishment or scope.
3. Summarize the real-world impact in simple terms.

IPC Section: {ipc_desc}

BNS Section: {bns_desc}
"""
    output = gemma_pipe(
        prompt,
        max_new_tokens=600,
        do_sample=True,
        temperature=0.7,
        top_p=0.9,
        repetition_penalty=1.1
    )
    generated_text = output[0]["generated_text"][len(prompt):].strip()
    return generated_text
