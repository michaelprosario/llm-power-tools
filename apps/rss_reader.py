# adjust path to include the parent directory
import sys
import os
from dotenv import load_dotenv
from rpds import List
from sentence_transformers import SentenceTransformer

load_dotenv()

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from genAiPowerToolsInfra.rss_reader_provider import RSSReaderProvider

# Example usage and testing
def test_rss_reader():
    """Test function for the RSS reader."""
    reader = RSSReaderProvider(timeout=10)
    
    # Test feeds
    test_feeds = [
        "https://changelog.com/feed"        
    ]
    
    for feed_url in test_feeds:
        print(f"\n=== Testing feed: {feed_url} ===")
        
        result = reader.read_feed(feed_url, max_entries=1000)
        
        if result.success:
            print(f"✅ Success: {result.message}")
            print(f"Feed: {result.feed_metadata.title}")
            print(f"Type: {result.feed_metadata.feed_type}")
            print(f"Entries: {result.total_entries}")
            
            for i, entry in enumerate(result.entries, 1):
                print(f"\nEntry {i}:")
                print(f"  Title: {entry.title[:60]}...")
                print(f"  Link: {entry.link}")
                print(f"  Published: {entry.published}")
        else:
            print(f"❌ Failed: {result.message}")
            for error in result.errors:
                print(f"  Error: {error}")
    
    reader.close()


if __name__ == "__main__":
    test_rss_reader()