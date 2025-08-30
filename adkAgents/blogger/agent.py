
from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.tools import google_search
from google.genai import types
from google.adk.agents import Agent, LlmAgent,SequentialAgent


blogger_writer_agent = Agent(
    name="blogger_writer_agent",
    model="gemini-2.0-flash",
    description="Agent to write a 600 word blog post about a focused topic.",
    instruction="""
I can write a detailed 600 word blog post on any focused topic you provide. 
Just give me the topic and I'll create the content for you!  
I will try to use real world case studies or stories to increase engagement.

**Quality elements for blog post**
- Compelling Title: Grabs attention immediately.
- Lead Paragraph: Hooks the reader with relevance.
- Personal Experience: Builds connection through storytelling.
- Main Body: Scannable content with lists and bullets.
- Discussion Question: Invites reader interaction.
    """,
    tools=[google_search],
    output_key="blog_content"
)

blogger_review_agent = Agent(
    name="blogger_review_agent",
    model="gemini-2.0-flash",
    description="Agent to review blog content for quality and accuracy.",
    instruction="""
    I can review your blog content and provide feedback on quality and accuracy. 
    You are focused on novice or intermediate learners.
    Just provide me with the content and I'll outline corrections and suggestions as bullets.

    **Blog Content to Review:**
    {blog_content}
    """,
    tools=[google_search],
    output_key="review_comments"
)

blogger_revise_agent = Agent(
    name="blogger_revise_agent",
    model="gemini-2.0-flash",
    description="Agent to revise blog content based on review comments.",
    instruction="""
    I can help you revise your blog content based on the feedback provided. Just give me the original content and the review comments, and I'll make the necessary changes.  Return content as markdown.

    **Original Blog Content:**
    {blog_content}

    **Review Comments:**
    {review_comments}

    """,
    tools=[google_search],
    output_key="blog_content"
)

blogger_outline_agent = Agent(
    name="blogger_outline_agent",
    model="gemini-2.0-flash",
    description="Agent to outline a blog post series on a specific theme.",
    instruction="I can help you outline a series of blog posts on a specific theme. Just provide me with the theme and I'll create an outline for you!",
    tools=[google_search],
    output_key="blog_series_outline"
)

blogger_review_agent2 = Agent(
    name="blogger_review_agent",
    model="gemini-2.0-flash",
    description="Agent to review blog content for quality and accuracy.",
    instruction="""
    I can review your blog content and provide feedback on quality and accuracy. 
    You are focused on novice or intermediate learners.
    Just provide me with the content and I'll outline corrections and suggestions as bullets.

    **Blog Content to Review:**
    {blog_content}
    """,
    tools=[google_search],
    output_key="review_comments"
)

blogger_revise_agent2 = Agent(
    name="blogger_revise_agent2",
    model="gemini-2.0-flash",
    description="Agent to revise blog content based on review comments.",
    instruction="""
    I can help you revise your blog content based on the feedback provided. Just give me the original content and the review comments, and I'll make the necessary changes.  Return content as markdown.

    **Original Blog Content:**
    {blog_content}

    **Review Comments:**
    {review_comments}

    """,
    tools=[google_search],
    output_key="blog_content"
)

blog_pipeline_agent = SequentialAgent(
    name="BlogPipelineAgent",
    sub_agents=[
        blogger_writer_agent, 
        blogger_review_agent, 
        blogger_revise_agent, 
        blogger_review_agent2, 
        blogger_revise_agent2
    ],
    description="Executes a sequence of blog writing, reviewing, and revising."
)

root_agent = blog_pipeline_agent
