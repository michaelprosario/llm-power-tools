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



Thanks for sharing the error, Michael. Based on the details and recent community reports, here’s what’s happening:

---

### ❌ Error Breakdown

You're seeing:
```
dial tcp: lookup ollama on 10.19.0.10:53: no such host
```

This means Weaviate is trying to vectorize data using **Ollama**, but it can't resolve the hostname `ollama`. That’s because:

- You're using **Weaviate Cloud**, which doesn’t include or support a local Ollama container.
- Your config still references Ollama as the embedder.

---

### ✅ How to Fix It

You need to **remove Ollama references** and switch to a supported embedder like `text2vec-transformers`. Here's what to do:

#### 1. **Update Weaviate Configuration**
Make sure your Weaviate instance is configured with:

```yaml
ENABLE_MODULES: 'text2vec-transformers'
TRANSFORMERS_INFERENCE_API: 'https://<your-transformer-endpoint>'
```

If you're using Weaviate Cloud, you’ll need to host the transformer model separately (e.g., on a VM or container) and expose it via a public endpoint.

#### 2. **Remove Ollama from Your Code**
If your Python client or import script references `http://ollama:11434/api/embed`, update it to use the correct transformer endpoint.

#### 3. **Verify the Embedder**
Test the endpoint manually:

```bash
curl -X POST https://<your-transformer-endpoint>/embed \
  -H "Content-Type: application/json" \
  -d '{"model": "distilbert-base-uncased", "input": "Why is the sky blue?"}'
```

---

Would you like help setting up a lightweight transformer endpoint on a VM or container that works with Weaviate Cloud? I can walk you through that next.

