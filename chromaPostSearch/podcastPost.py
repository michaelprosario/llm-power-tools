import json
from dataclasses import dataclass
from typing import Optional
from datetime import datetime
import uuid

@dataclass
class PodcastPost:
    """Entity class representing a podcast episode."""
    
    id: str
    content_source_id: str
    title: str
    source_url: str
    description: str
    enclosure_url: str
    
    # Optional fields that might be added later
    published_date: Optional[datetime] = None
    duration: Optional[str] = None
    file_size: Optional[int] = None
    
    @classmethod
    def from_json(cls, json_data: str) -> 'PodcastPost':
        """
        Create a PodcastEpisode instance from JSON string.
        
        Args:
            json_data: JSON string containing podcast episode data
            
        Returns:
            PodcastEpisode instance
            
        Raises:
            ValueError: If required fields are missing or JSON is invalid
            json.JSONDecodeError: If JSON string is malformed
        """
        try:
            data = json.loads(json_data)
            return cls.from_dict(data)
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Invalid JSON format: {e}")
    
    @classmethod
    def from_dict(cls, data: dict) -> 'PodcastPost':
        """
        Create a PodcastEpisode instance from dictionary.
        
        Args:
            data: Dictionary containing podcast episode data
            
        Returns:
            PodcastEpisode instance
            
        Raises:
            ValueError: If required fields are missing
        """
        # Validate required fields
        required_fields = ['Id', 'ContentSourceId', 'Title', 'SourceUrl', 'Description', 'EnclosureUrl']
        missing_fields = [field for field in required_fields if field not in data]
        
        if missing_fields:
            raise ValueError(f"Missing required fields: {missing_fields}")
        
        return cls(
            id=data['Id'],
            content_source_id=data['ContentSourceId'],
            title=data['Title'],
            source_url=data['SourceUrl'],
            description=data['Description'],
            enclosure_url=data['EnclosureUrl']
        )
    
    @classmethod
    def from_json_file(cls, file_path: str) -> 'PodcastPost':
        """
        Create a PodcastEpisode instance from JSON file.
        
        Args:
            file_path: Path to JSON file containing podcast episode data
            
        Returns:
            PodcastEpisode instance
            
        Raises:
            FileNotFoundError: If file doesn't exist
            ValueError: If required fields are missing
            json.JSONDecodeError: If JSON is malformed
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                json_content = file.read()
                return cls.from_json(json_content)
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {file_path}")
        except Exception as e:
            raise ValueError(f"Error reading file {file_path}: {e}")
    
    def to_dict(self) -> dict:
        """
        Convert PodcastEpisode instance to dictionary.
        
        Returns:
            Dictionary representation of the podcast episode
        """
        return {
            'Id': self.id,
            'ContentSourceId': self.content_source_id,
            'Title': self.title,
            'SourceUrl': self.source_url,
            'Description': self.description,
            'EnclosureUrl': self.enclosure_url,
            'PublishedDate': self.published_date.isoformat() if self.published_date else None,
            'Duration': self.duration,
            'FileSize': self.file_size
        }
    
    def to_json(self) -> str:
        """
        Convert PodcastEpisode instance to JSON string.
        
        Returns:
            JSON string representation of the podcast episode
        """
        return json.dumps(self.to_dict(), indent=2, ensure_ascii=False)
    
    def get_clean_description(self) -> str:
        """
        Get description with HTML tags removed.
        
        Returns:
            Clean text description without HTML tags
        """
        import re
        # Remove HTML tags
        clean_text = re.sub(r'<[^>]+>', '', self.description)
        # Clean up extra whitespace
        clean_text = re.sub(r'\s+', ' ', clean_text).strip()
        return clean_text
    
    def get_short_id(self) -> str:
        """
        Get a shortened version of the ID for display purposes.
        
        Returns:
            First 8 characters of the ID
        """
        return self.id[:8] if len(self.id) >= 8 else self.id
    
    def __str__(self) -> str:
        """String representation of the podcast episode."""
        return f"PodcastEpisode(id='{self.get_short_id()}...', title='{self.title[:50]}...')"
    
    def __repr__(self) -> str:
        """Detailed string representation of the podcast episode."""
        return (f"PodcastEpisode(id='{self.id}', "
                f"content_source_id='{self.content_source_id}', "
                f"title='{self.title}')")


