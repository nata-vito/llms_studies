# llms_studies
Repository to archive my studies about LLMs 

```bash
conda create -n agentic_env python=3.10
conda activate agentic_env

git clone --recursive https://github.com/nata-vito/llms_studies.git
cd llms_studies
pip install -r requirements.txt

huggingface-cli download meta-llama/Meta-Llama-3.1-8B-Instruct --include "original/*" --local-dir meta-llama/Meta-Llama-3.1-8B-Instruct
```

