from flask import Flask, request, jsonify
import google.generativeai as genai
import os
import logging


GEMINI_MODEL = "gemini-2.0-flash"   

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Configure Gemini API key
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")  # Or set it directly: "YOUR_API_KEY"
if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY environment variable not set.")

genai.configure(api_key=GOOGLE_API_KEY)

# Select the Gemini model
model = genai.GenerativeModel(GEMINI_MODEL)


@app.route('/generate_blog', methods=['POST'])
def generate_blog():
    """
    Generates a blog post based on the provided topic using the Gemini API.
    Accepts parameters for topic, length, tone, and target audience.
    """
    try:
        data = request.get_json()
        topic = data.get('topic')
        length = data.get('length', 'medium')  # short, medium, long
        tone = data.get('tone', 'neutral')  # informative, humorous, persuasive
        audience = data.get('audience', 'general')

        if not topic:
            return jsonify({'error': 'Topic is required'}), 400

        # Input validation for topic (example - prevent script injection)
        if not isinstance(topic, str) or len(topic) > 200:
            return jsonify({'error': 'Invalid topic'}), 400
        
        prompt = f"Write a {length} blog post about: {topic}. The tone should be {tone} and it is targeted towards a {audience} audience."
        logging.info(f"Prompt: {prompt}")

        try:
            response = model.generate_content(prompt)
            blog_post = response.text
            logging.info("Blog post generated successfully.")
            return jsonify({'blog_post': blog_post}), 200
        except genai.APIError as e:
            logging.error(f"Gemini API Error: {e}")
            return jsonify({'error': f"Gemini API Error: {str(e)}"}), 500


    except Exception as e:
        logging.exception("An unexpected error occurred:")
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=False)
