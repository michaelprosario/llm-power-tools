import sys
import os
from dotenv import load_dotenv
from rpds import List
from sentence_transformers import SentenceTransformer

load_dotenv()

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# import lib for guids
import uuid

# get list of developer friendly RSS feeds
from genAiPowerToolsInfra.rss_reader_provider import RSSReaderProvider
from genAiPowerToolsInfra.chroma_data_repository import ChromaDataRepository


import requests
import random
import xml.etree.ElementTree as ET

def getBlogs3():
    """
    Fetches the OPML file from the provided URL, parses it, and returns 20 random blogs (title and xmlUrl).
    """
    url = "https://raw.githubusercontent.com/simevidas/web-dev-feeds/refs/heads/master/feeds.opml"
    response = requests.get(url)
    response.raise_for_status()
    root = ET.fromstring(response.content)
    # Find all outline elements with xmlUrl attribute
    outlines = root.findall('.//outline[@xmlUrl]')
    blogs = []
    for outline in outlines:
        title = outline.attrib.get('title') or outline.attrib.get('text')
        xml_url = outline.attrib.get('xmlUrl')
        if title and xml_url:
            blogs.append({"name": title, "rss_feed": xml_url})
    # Pick 20 random blogs
    return random.sample(blogs, min(20, len(blogs)))


def getBlogs2():
    blogs = [
    {
        "name": "Innovate Orlando",
        "rss_feed": "https://innovateorlando.com/feed"
    },
    {
    "name": "Google Cloud Blog",
    "rss_feed": "https://cloud.google.com/blog/products/gcp/rss.xml"
    },
    {
    "name": "Google Developers Blog",
    "rss_feed": "https://developers.googleblog.com/feeds/posts/default"
    },
    {
    "name": "Google AI Blog",
    "rss_feed": "https://ai.googleblog.com/feeds/posts/default"
    },
    {
    "name": "Google Workspace Updates Blog",
    "rss_feed": "https://workspaceupdates.googleblog.com/feeds/posts/default"
    },
    {
    "name": "Android Developers Blog",
    "rss_feed": "https://android-developers.googleblog.com/feeds/posts/default"
    },
    {
    "name": "web.dev",
    "rss_feed": "https://web.dev/feed.xml"
    },
    {
    "name": "Chrome Developers Blog",
    "rss_feed": "https://developer.chrome.com/blog/feed.xml"
    },
    {
    "name": "Firebase Blog",
    "rss_feed": "https://firebase.googleblog.com/feeds/posts/default"
    },
    {
    "name": "Google Security Blog",
    "rss_feed": "https://security.googleblog.com/feeds/posts/default"
    },
    {
    "name": "Google Search Central Blog",
    "rss_feed": "https://developers.google.com/search/blog/rss.xml"
    },
    {
    "name": "DEV Community (general)",
    "rss_feed": "https://dev.to/feed"
    },
    {
    "name": "Hacker Noon (general)",
    "rss_feed": "https://hackernoon.com/feed"
    },
    {
    "name": "InfoQ - Cloud",
    "rss_feed": "https://www.infoq.com/feed/cloud/"
    },
    {
    "name": "DZone - Cloud",
    "rss_feed": "https://dzone.com/articles/rss.xml?section=cloud"
    },
    {
    "name": "The New Stack",
    "rss_feed": "https://thenewstack.io/feed/"
    },
    {
    "name": "Serverless.com Blog",
    "rss_feed": "https://www.serverless.com/blog/rss.xml"
    },
    {
    "name": "Towards Data Science (publication feed)",
    "rss_feed": "https://towardsdatascience.com/feed"
    },
    {
    "name": "Cloud Native Computing Foundation (CNCF) Blog",
    "rss_feed": "https://www.cncf.io/feed/"
    },
    {
    "name": "Google Cloud Community Blogs",
    "rss_feed": "No single RSS feed available for this section"
    },
    {
    "name": "Google Open Source Blog",
    "rss_feed": "https://opensource.googleblog.com/feeds/posts/default"
    },
    {
    "name": "Open Source Initiative Blog",
    "rss_feed": "https://opensource.org/feed/"
    },
    {
    "name": "The GitHub Blog (Open Source section)",
    "rss_feed": "https://github.blog/category/open-source/feed/"
    },
    {
    "name": "ZDNET (Open Source section)",
    "rss_feed": "https://www.zdnet.com/topic/open-source/rss.xml"
    },
    {
    "name": "Open Source For You",
    "rss_feed": "https://opensourceforu.com/feed/"
    },
    {
    "name": "Red Hat Blog (Open Source section)",
    "rss_feed": "https://www.redhat.com/en/blog/feed/rss"
    },
    {
    "name": "Planet GNOME",
    "rss_feed": "https://planet.gnome.org/rss20.xml"
    },
    {
    "name": "Free Software Foundation (FSF) News",
    "rss_feed": "https://www.fsf.org/news/rss.xml"
    },
    {
    "name": "DEV Community (Open Source tag)",
    "rss_feed": "https://dev.to/feed/tag/opensource"
    },
    {
    "name": "TechRepublic (Open Source section)",
    "rss_feed": "https://www.techrepublic.com/rssfeeds/topic/open-source/"
    },
    {
        "name": "Microsoft Dotnet Blog",
        "rss_feed": "https://devblogs.microsoft.com/dotnet/feed"
    }

    ]
    return blogs

# using rss reader provider, get the content for these feeds
reader = RSSReaderProvider()

# setup chromadb
repo = ChromaDataRepository()
collection = repo.create_collection("rss_feeds")

for feed in getBlogs3():    
    content = reader.read_feed(feed['rss_feed'], max_entries=1000)
    print(f"Content for {feed}: {content}")

    # iterate over the content and extract relevant information
    for item in content.entries:
        title = item.title
        link = item.link
        published = item.published

        # create a hash from the link provided
        document_id = str(uuid.uuid5(uuid.NAMESPACE_URL, link))
        
        repo.add_document(
            collection,
            document_id=document_id,
            text_content=f"{title}|{item.summary}",
            meta_data={
                "title": item.title,
                "link": item.link,
                "description": item.description,
                "summary": item.summary,
                "feed": feed['rss_feed'],
                "feed_name": feed['name']
            }
        )




