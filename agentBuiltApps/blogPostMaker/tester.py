import requests
import json
import time

def test_blog_generator():
    """Test the blog post generator API"""
    
    # API endpoint
    url = "http://localhost:5000/generate_blog"
    
    # Test data
    test_data = {
        "topic": "The benefits of machine learning in healthcare",
        "length": "medium",
        "tone": "informative",
        "audience": "healthcare professionals"
    }
    
    try:
        print("Testing blog post generator...")
        print(f"Topic: {test_data['topic']}")
        print(f"Length: {test_data['length']}")
        print(f"Tone: {test_data['tone']}")
        print(f"Audience: {test_data['audience']}")
        print("-" * 50)
        
        # Send POST request
        response = requests.post(
            url, 
            json=test_data,
            headers={"Content-Type": "application/json"},
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            print("✅ Success! Blog post generated:")
            print("-" * 50)
            print(result['blog_post'])
        else:
            print(f"❌ Error {response.status_code}:")
            print(response.json())
            
    except requests.exceptions.ConnectionError:
        print("❌ Connection error. Make sure the Flask app is running on localhost:5000")
    except requests.exceptions.Timeout:
        print("❌ Request timed out")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    print("Make sure to:")
    print("1. Set GOOGLE_API_KEY environment variable")
    print("2. Run 'python main.py' in another terminal")
    print("3. Wait for Flask to start, then run this test")
    print()
    
    input("Press Enter when ready to test...")
    test_blog_generator()
    