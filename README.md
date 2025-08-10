## todo
- create weaviate stack that does not use ollama
- create ingestion program
- create program to grab posts from blog


## What is the context window size for Gemma?

🧠 The **Google Gemma 3B** model has a **128K token context window**, which is impressively large for a model of its size. That means it can process vast amounts of input—like multiple long documents, hundreds of images, or deeply layered prompts—all in a single go.

This expanded window is part of what makes Gemma 3 models so versatile for tasks like:
- 📄 Summarizing lengthy articles
- 🧩 Handling complex reasoning chains
- 🖼️ Analyzing multimodal inputs (text + images)

If you're experimenting with Gemma 3B on a gaming PC or local setup, that 128K context window opens up some serious possibilities for rich, persistent interactions. Want help exploring how to optimize it for your workflow?

## How do I properly setup my virtual environment?

```
# Navigate to your project directory
cd /home/mrosario/dev/semanticKernalLocal

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate
which python
```