
import os
from podcastPost import PodcastPost

import sys
import os
import uuid
from dotenv import load_dotenv
from rpds import List
from sentence_transformers import SentenceTransformer

load_dotenv()

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# import lib for guids
import uuid

from genAiPowerToolsInfra.chroma_data_repository import ChromaDataRepository

class PodcastDataReader:
    def __init__(self):
        pass

    def get_files_at_path(self, path: str) -> list[str]:
        """Get all JSON files in the specified path."""
        import os
        if not os.path.exists(path):
            raise FileNotFoundError(f"Path does not exist: {path}")
        
        return [f for f in os.listdir(path) if f.endswith(".json")]
    
    def load_podcast_from_file(self, file_path: str) -> PodcastPost:
        """
        Load a single podcast episode from JSON file.
        
        Args:
            file_path: Path to the JSON file
            
        Returns:
            PodcastEpisode instance
        """
        return PodcastPost.from_json_file(file_path)
    
    def get_podcasts_from_directory(self, directory_path: str) -> list[PodcastPost]:
        """
        Load all podcast episodes from JSON files in a directory.
        
        Args:
            directory_path: Path to directory containing JSON files
            
        Returns:
            List of PodcastEpisode instances
        """
        import os
        
        podcast_episodes = []
        json_files = self.get_files_at_path(directory_path)
        
        for filename in json_files:
            file_path = os.path.join(directory_path, filename)
            try:
                episode = self.load_podcast_from_file(file_path)
                podcast_episodes.append(episode)
                print(f"✅ Loaded: {episode.title[:60]}...")
            except Exception as e:
                print(f"❌ Failed to load {filename}: {e}")
        
        return podcast_episodes

class ChromaRepository:
    def __init__(self):
        pass


    

podcastDataReader = PodcastDataReader()
posts = podcastDataReader.get_podcasts_from_directory("../data/podcastData")

chromaRepo = ChromaDataRepository()
chromaRepo.create_collection("podcasts")

collection = chromaRepo.get_collection("podcasts")
for post in posts:    
    podcast_id = str(uuid.uuid5(uuid.NAMESPACE_DNS, post.enclosure_url))
    text_content = f"{post.title}|{post.description}"
    metadata = post.to_dict()  # Convert PodcastPost to dict for metadata
    chromaRepo.add_document(collection, podcast_id, text_content, metadata)
    print(f"Added podcast: {post.title} with ID: {podcast_id}")

