# llms_studies
Repository to archive my studies about LLMs 

```bash
conda create -n agentic_env python=3.10
conda activate agentic_env

git clone --recursive https://github.com/nata-vito/llms_studies.git
cd llms_studies
pip install -r requirements.txt

llama download --source huggingface --model-id llama3_1_8b_instruct  --hf-token $HF_TOKEN
```

Access to Meta AI and follow the steps to get the available link to Llama-Guard3, and follow the next steps:

```bash

# Llama-Guard3
git clone https://github.com/meta-llama/PurpleLlama.git

cd PurpleLlama/
cd Llama-Guard3/

# Insert the link to cli
./download.sh llama-guard-3 


# Prompt Guard
git clone https://github.com/meta-llama/llama-models.git
cd llama-models/models/llama3_1
sudo chmod +x download.sh 

# Insert the link to cli and select prompt-guard in the options menu
./download.sh



```