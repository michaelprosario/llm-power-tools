import requests
import json
import sys
from typing import Dict, Any

# API base URL
BASE_URL = "http://localhost:8000"

def test_health_check():
    """Test the health check endpoint"""
    print("Testing health check...")
    try:
        response = requests.get(f"{BASE_URL}/health")
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
        return response.status_code == 200
    except requests.exceptions.ConnectionError:
        print("❌ Connection error - make sure the API is running")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_add_podcast():
    """Test adding a podcast"""
    print("\nTesting add podcast...")
    
    test_podcast = {
        "id": "test-podcast-001",
        "content_source_id": "test-source-001",
        "title": "Introduction to Machine Learning",
        "source_url": "https://example.com/ml-podcast",
        "description": "A comprehensive introduction to machine learning concepts, algorithms, and applications in modern technology.",
        "enclosure_url": "https://example.com/ml-podcast.mp3"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/podcasts", json=test_podcast)
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
        return response.status_code == 200
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_add_invalid_podcast():
    """Test adding an invalid podcast (missing required fields)"""
    print("\nTesting add invalid podcast...")
    
    invalid_podcast = {
        "id": "test-podcast-002",
        # Missing required fields
        "title": "Incomplete Podcast"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/podcasts", json=invalid_podcast)
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
        return response.status_code == 422  # Validation error
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_search_valid_query():
    """Test searching with a valid query"""
    print("\nTesting search with valid query...")
    
    search_request = {
        "query": "machine learning",
        "max_results": 5
    }
    
    try:
        response = requests.post(f"{BASE_URL}/search", json=search_request)
        print(f"Status: {response.status_code}")
        result = response.json()
        print(f"Response: {json.dumps(result, indent=2)}")
        return response.status_code == 200
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_search_empty_query():
    """Test searching with an empty query"""
    print("\nTesting search with empty query...")
    
    search_request = {
        "query": "",
        "max_results": 5
    }
    
    try:
        response = requests.post(f"{BASE_URL}/search", json=search_request)
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
        return response.status_code == 422  # Validation error
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_root_endpoint():
    """Test the root endpoint"""
    print("\nTesting root endpoint...")
    
    try:
        response = requests.get(f"{BASE_URL}/")
        print(f"Status: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        return response.status_code == 200
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    """Run all tests"""
    print("🚀 Starting API tests...")
    print("Make sure the API is running with: python podcast_api.py")
    print("-" * 50)
    
    tests = [
        ("Health Check", test_health_check),
        ("Root Endpoint", test_root_endpoint),
        ("Add Valid Podcast", test_add_podcast),
        ("Add Invalid Podcast", test_add_invalid_podcast),
        ("Search Valid Query", test_search_valid_query),
        ("Search Empty Query", test_search_empty_query),
    ]
    
    results = []
    
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
            status = "✅ PASSED" if result else "❌ FAILED"
            print(f"{status}")
        except Exception as e:
            results.append((test_name, False))
            print(f"❌ FAILED - Exception: {e}")
        
        print("-" * 50)
    
    # Summary
    print("\n📊 TEST SUMMARY:")
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASSED" if result else "❌ FAILED"
        print(f"{test_name}: {status}")
    
    print(f"\nTotal: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed!")
        return 0
    else:
        print("💥 Some tests failed!")
        return 1

if __name__ == "__main__":
    sys.exit(main())
