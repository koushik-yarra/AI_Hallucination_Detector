# AI Hallucination Detector

This project provides a simple **hallucination detection tool** for AI-generated text, checking for:

- Factual errors (using Wikipedia)
- Logical coherence (chain of thought)
- Contextual relevance to the input prompt
- Check citation by providing urls

## Setup

1. Create a virtual environment and install dependencies:

```bash
pip install -r requirements.txt


## Future improvements
1. using transformers for checking truthfulness
2. use RAG which pulls relevant context from external sources before generating the answer
3. consistent answer - Ask the same question for in different way