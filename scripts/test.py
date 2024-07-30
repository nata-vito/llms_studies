from transformers import pipeline

pipe = pipeline("text-classification", model="meta-llama/Prompt-Guard-86M")

messages = [
    {
        "role": "user", 
        "content": "Who are you?"
    },
]

pipe = pipeline("text-generation", model="meta-llama/Llama-Guard-3-8B")
pipe(messages)

messages = [
    {"role": "user", "content": "Who are you?"},
]
pipe = pipeline("text-generation", model="meta-llama/Meta-Llama-3.1-8B-Instruct")
pipe(messages)
