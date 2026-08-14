import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate


# Load environment variables
load_dotenv()


# Connect LangChain to Groq
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7,
)


# Marketing instructions
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """You are an AI Social Media Marketing Assistant.

Your job is to create high-quality social media content.

When the user provides:
- Business/niche
- Platform
- Topic
- Target audience
- Tone

Create:

1. A strong hook
2. A social media post
3. A clear call-to-action
4. Relevant hashtags

Keep the content engaging, practical, and suitable for the requested platform."""
    ),
    (
        "human",
        """
Business/Niche: {business}
Platform: {platform}
Topic: {topic}
Target Audience: {audience}
Tone: {tone}
"""
    )
])


# Connect prompt → LLM
chain = prompt | llm


def generate_content(
    business,
    platform,
    topic,
    audience,
    tone
):
    response = chain.invoke({
        "business": business,
        "platform": platform,
        "topic": topic,
        "audience": audience,
        "tone": tone
    })

    return response.content