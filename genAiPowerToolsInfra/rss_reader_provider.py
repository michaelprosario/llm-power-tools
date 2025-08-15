import feedparser
import requests
from typing import List, Dict, Any, Optional
from datetime import datetime
from dataclasses import dataclass
import time
from urllib.parse import urlparse

@dataclass
class FeedEntry:
    """Represents a single entry from an RSS/Atom feed."""
    title: str
    link: str
    description: str
    published: Optional[datetime] = None
    author: Optional[str] = None
    categories: List[str] = None
    guid: Optional[str] = None
    content: Optional[str] = None
    summary: Optional[str] = None
    
    def __post_init__(self):
        if self.categories is None:
            self.categories = []

@dataclass
class FeedMetadata:
    """Represents metadata about the RSS/Atom feed."""
    title: str
    link: str
    description: str
    language: Optional[str] = None
    last_updated: Optional[datetime] = None
    generator: Optional[str] = None
    feed_type: Optional[str] = None  # 'rss' or 'atom'
    version: Optional[str] = None

class RSSReaderResult:
    """Result class for RSS reader operations."""
    
    def __init__(self, success: bool = True, message: str = "", errors: List[str] = None):
        self.success = success
        self.message = message
        self.errors = errors or []
        
        # Feed data
        self.feed_metadata: Optional[FeedMetadata] = None
        self.entries: List[FeedEntry] = []
        self.total_entries: int = 0
        
        # Request metadata
        self.feed_url: str = ""
        self.status_code: Optional[int] = None
        self.fetch_time: Optional[datetime] = None
        self.etag: Optional[str] = None
        self.last_modified: Optional[str] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert result to dictionary."""
        return {
            "success": self.success,
            "message": self.message,
            "errors": self.errors,
            "feed_url": self.feed_url,
            "status_code": self.status_code,
            "fetch_time": self.fetch_time.isoformat() if self.fetch_time else None,
            "total_entries": self.total_entries,
            "feed_metadata": {
                "title": self.feed_metadata.title if self.feed_metadata else None,
                "description": self.feed_metadata.description if self.feed_metadata else None,
                "feed_type": self.feed_metadata.feed_type if self.feed_metadata else None,
            } if self.feed_metadata else None,
            "entries": [
                {
                    "title": entry.title,
                    "link": entry.link,
                    "description": entry.description,
                    "published": entry.published.isoformat() if entry.published else None,
                    "author": entry.author,
                    "categories": entry.categories
                }
                for entry in self.entries
            ]
        }
    
    def __repr__(self):
        status = "SUCCESS" if self.success else "FAILED"
        return f"RSSReaderResult({status}, {self.total_entries} entries, {self.feed_url})"


class RSSReaderProvider:
    """Provider class for reading RSS and Atom feeds."""
    
    def __init__(self, timeout: int = 30, user_agent: str = None):
        """
        Initialize RSS reader provider.
        
        Args:
            timeout: Request timeout in seconds
            user_agent: Custom user agent string
        """
        self.timeout = timeout
        self.user_agent = user_agent or "RSS Reader Provider 1.0"
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': self.user_agent})
    
    def read_feed(self, feed_url: str, max_entries: int = None) -> RSSReaderResult:
        """
        Read RSS or Atom feed from URL.
        
        Args:
            feed_url: URL of the RSS/Atom feed
            max_entries: Maximum number of entries to return (None for all)
            
        Returns:
            RSSReaderResult containing feed data or error information
        """
        result = RSSReaderResult()
        result.feed_url = feed_url
        result.fetch_time = datetime.now()
        
        try:
            # Validate URL
            if not self._is_valid_url(feed_url):
                result.success = False
                result.message = "Invalid feed URL"
                result.errors.append(f"Invalid URL format: {feed_url}")
                return result
            
            # Fetch feed with timeout
            print(f"Fetching feed from: {feed_url}")
            response = self.session.get(feed_url, timeout=self.timeout)
            result.status_code = response.status_code
            
            # Check HTTP status
            if response.status_code != 200:
                result.success = False
                result.message = f"HTTP {response.status_code} error"
                result.errors.append(f"Failed to fetch feed: HTTP {response.status_code}")
                return result
            
            # Parse feed using feedparser
            feed_data = feedparser.parse(response.content)
            
            # Check for feed parsing errors
            if hasattr(feed_data, 'bozo') and feed_data.bozo:
                print(f"Warning: Feed parsing issues detected: {feed_data.bozo_exception}")
                result.errors.append(f"Feed parsing warning: {feed_data.bozo_exception}")
            
            # Extract feed metadata
            result.feed_metadata = self._extract_feed_metadata(feed_data)
            
            # Extract entries
            entries = feed_data.entries
            if max_entries:
                entries = entries[:max_entries]
            
            result.entries = [self._extract_entry(entry) for entry in entries]
            result.total_entries = len(result.entries)
            
            # Extract additional metadata
            result.etag = getattr(feed_data, 'etag', None)
            result.last_modified = getattr(feed_data, 'modified', None)
            
            result.message = f"Successfully parsed {result.total_entries} entries"
            print(f"Successfully parsed {result.total_entries} entries from feed")
            
        except requests.exceptions.Timeout:
            result.success = False
            result.message = "Request timeout"
            result.errors.append(f"Timeout after {self.timeout} seconds")
            
        except requests.exceptions.ConnectionError:
            result.success = False
            result.message = "Connection error"
            result.errors.append("Failed to connect to feed URL")
            
        except requests.exceptions.RequestException as e:
            result.success = False
            result.message = "Request failed"
            result.errors.append(f"Request error: {str(e)}")
            
        except Exception as e:
            result.success = False
            result.message = "Unexpected error"
            result.errors.append(f"Unexpected error: {str(e)}")
        
        return result
    
    def read_feed_content(self, feed_content: str) -> RSSReaderResult:
        """
        Read RSS or Atom feed from content string.
        
        Args:
            feed_content: Raw RSS/Atom feed content as string
            
        Returns:
            RSSReaderResult containing feed data or error information
        """
        result = RSSReaderResult()
        result.feed_url = "content-string"
        result.fetch_time = datetime.now()
        
        try:
            # Parse feed content
            feed_data = feedparser.parse(feed_content)
            
            # Check for parsing errors
            if hasattr(feed_data, 'bozo') and feed_data.bozo:
                result.errors.append(f"Feed parsing warning: {feed_data.bozo_exception}")
            
            # Extract feed metadata
            result.feed_metadata = self._extract_feed_metadata(feed_data)
            
            # Extract entries
            result.entries = [self._extract_entry(entry) for entry in feed_data.entries]
            result.total_entries = len(result.entries)
            
            result.message = f"Successfully parsed {result.total_entries} entries from content"
            
        except Exception as e:
            result.success = False
            result.message = "Failed to parse feed content"
            result.errors.append(f"Parsing error: {str(e)}")
        
        return result
    
    def _extract_feed_metadata(self, feed_data) -> FeedMetadata:
        """Extract metadata from parsed feed."""
        feed_info = feed_data.feed
        
        # Determine feed type
        feed_type = "unknown"
        if hasattr(feed_data, 'version'):
            if 'rss' in feed_data.version.lower():
                feed_type = "rss"
            elif 'atom' in feed_data.version.lower():
                feed_type = "atom"
        
        # Parse last updated time
        last_updated = None
        if hasattr(feed_info, 'updated_parsed') and feed_info.updated_parsed:
            last_updated = datetime(*feed_info.updated_parsed[:6])
        
        return FeedMetadata(
            title=getattr(feed_info, 'title', 'Unknown'),
            link=getattr(feed_info, 'link', ''),
            description=getattr(feed_info, 'description', ''),
            language=getattr(feed_info, 'language', None),
            last_updated=last_updated,
            generator=getattr(feed_info, 'generator', None),
            feed_type=feed_type,
            version=getattr(feed_data, 'version', None)
        )
    
    def _extract_entry(self, entry) -> FeedEntry:
        """Extract data from a single feed entry."""
        # Parse published date
        published = None
        if hasattr(entry, 'published_parsed') and entry.published_parsed:
            published = datetime(*entry.published_parsed[:6])
        
        # Extract categories/tags
        categories = []
        if hasattr(entry, 'tags'):
            categories = [tag.term for tag in entry.tags if hasattr(tag, 'term')]
        elif hasattr(entry, 'category'):
            categories = [entry.category]
        
        # Get content (prefer content over summary)
        content = None
        if hasattr(entry, 'content') and entry.content:
            content = entry.content[0].value if isinstance(entry.content, list) else entry.content
        
        return FeedEntry(
            title=getattr(entry, 'title', 'No Title'),
            link=getattr(entry, 'link', ''),
            description=getattr(entry, 'description', getattr(entry, 'summary', '')),
            published=published,
            author=getattr(entry, 'author', None),
            categories=categories,
            guid=getattr(entry, 'id', getattr(entry, 'guid', None)),
            content=content,
            summary=getattr(entry, 'summary', None)
        )
    
    def _is_valid_url(self, url: str) -> bool:
        """Validate URL format."""
        try:
            result = urlparse(url)
            return all([result.scheme, result.netloc])
        except Exception:
            return False
    
    def close(self):
        """Close the session."""
        if hasattr(self, 'session'):
            self.session.close()


