"""
Simple API test script to verify the backend is working
Run this after starting app.py to test the API
"""
import requests
import json
import time

API_URL = "http://localhost:5000"
TEST_SCENARIO = "Why do I keep buying things I don't need?"

def test_health():
    """Test if the API is alive"""
    print("Testing API health...")
    try:
        response = requests.get(f"{API_URL}/api/health")
        if response.status_code == 200:
            print("✅ Health check passed")
            return True
        else:
            print(f"❌ Health check failed: {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to server at http://localhost:5000")
        print("   Make sure the backend is running: python app.py")
        return False

def test_analyze():
    """Test the AI analysis endpoint"""
    print(f"\nTesting AI analysis with: '{TEST_SCENARIO}'")
    print("(This may take 5-10 seconds...)")
    
    try:
        start_time = time.time()
        
        response = requests.post(
            f"{API_URL}/api/analyze",
            json={"text": TEST_SCENARIO},
            timeout=30
        )
        
        elapsed = time.time() - start_time
        
        if response.status_code == 200:
            data = response.json()
            if 'analysis' in data:
                print(f"✅ Analysis successful ({elapsed:.1f}s)")
                print("\nResponse (first 500 chars):")
                print("-" * 50)
                analysis = data['analysis'][:500]
                print(analysis)
                if len(data['analysis']) > 500:
                    print("...[truncated]")
                print("-" * 50)
                return True
            else:
                print(f"❌ Invalid response format: {data}")
                return False
        else:
            print(f"❌ Request failed: {response.status_code}")
            print(f"Error: {response.text}")
            return False
            
    except requests.exceptions.Timeout:
        print("❌ Request timed out (took too long)")
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to server")
    except Exception as e:
        print(f"❌ Error: {str(e)}")
    
    return False

def main():
    print("=" * 50)
    print("Mental Model Hub - API Test")
    print("=" * 50)
    print()
    
    # Test health
    if not test_health():
        print("\n❌ API is not running. Start it with: python app.py")
        return
    
    # Test analyze
    if not test_analyze():
        print("\n❌ Analysis test failed")
        return
    
    print("\n" + "=" * 50)
    print("✅ All tests passed! The app is working.")
    print("=" * 50)
    print("\nYou can now:")
    print("1. Open index.html in your browser")
    print("2. Go to the 'AI Explain' tab")
    print("3. Try the AI analysis feature")

if __name__ == "__main__":
    main()
