### todo
- setup weaviate
- ingest data into weaviate
- write script to query weaviate based on prompt


### tool ideas for marketers
- get posts from rss feed
- Creating Timelines and Schedules: Building a detailed timeline for the entire event—from the initial planning stages to the day of the event—is crucial. This involves outlining every task, deadline, and responsibility, and it must be constantly updated and communicated to all parties.
- audience research
- marketing plan
- Competitor Analysis
- write content
- edit content
- proof-read content
- make images
- Taking a single blog post and turning it into social media posts, an email newsletter, and a video script requires a lot of formatting, editing, and tailoring for each specific platform
- Email Marketing: Crafting and sending email newsletters involves more than just writing. You need to segment your audience, design the email layout, A/B test subject lines, and schedule the send time for optimal engagement, all of which take careful planning and execution
- SEO Optimization


## ingestion of podcast data

Write program to import /workspaces/llm-power-tools/weaviatePostSearch/podcastData to weaviate
- as we start testing, only import the first 10 json file
- connect to cloud instance specified by .env
- each file in /workspaces/llm-power-tools/weaviatePostSearch/podcastData represents a single podcast
- The following fields are important to store in weaviate:
  - "Id"
  - "ContentSourceId"
  - "Title"
  - "SourceUrl"
  - "Description"
  - "EnclosureUrl"
- Store data in a collection called "Podcasts"
- use the model multi-qa-MiniLM-L6-cos-v1 to create embedding.  Embedding should be created from title and first 1000 characters of description
- do not leverage docker containers or ollama for embedding



