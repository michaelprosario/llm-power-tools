Create a fast api to search for podcasts similar to a query
The api should use the existing ChromaRepository
The api should include an end point to add a new podcast to the Chroma repository

===
Given
- I use the get_similar_documents api
- I specify a valid query
- I specify a number of rows to return

When
- I invoke the get_similar_documents api

Then
- I receive a listing of similar podcasts
- The data row should include the following:
    id: str
    content_source_id: str
    title: str
    source_url: str
    description: str
    enclosure_url: str

===

Given
- I use the get_similar_documents api
- I specify an empty query
- I specify a number of rows to return

When
- I invoke the get_similar_documents api

Then
- I receive a clear error message

===

Given
- I use the get_similar_documents api
- I specify a valid 
- I specify a number of rows to return

When
- I invoke the get_similar_documents api

Then
- I receive a clear error message

===

Given 
- I use the add_podcast api
- I specify a valid podcast with the following elements:
    - Id
    - ContentSourceId
    - Title
    - SourceUrl
    - Description
    - EnclosureUrl

When
- I execute the add_podcast api

Then
- The api should report the status of ok if everything got added

===

Given 
- I use the add_podcast api
- I specify a valid podcast with the following elements:
    - Id
    - ContentSourceId
    - Title
    - SourceUrl
    - Description
    - EnclosureUrl

When
- I execute the add_podcast api
- And the system had some kind of failure

Then
- The api should report the status of error
- The system should return a message describing the error reason

===

Given 
- I use the add_podcast api
- I fail to fill out the required elements of a podcast

When
- I execute the add_podcast api

Then
- The api should report the status of validation error
- The system should return a message describing the error reason


