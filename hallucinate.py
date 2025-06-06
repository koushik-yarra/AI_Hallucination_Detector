import wikipedia #type: ignore
from difflib import SequenceMatcher
import re

def get_wikipedia_summary(query, sentences=3):
    try:
        return wikipedia.summary(query, sentences=sentences)
    except:
        return None

def similarity_score(text1, text2):
    return SequenceMatcher(None, text1.lower(), text2.lower()).ratio()

def factual_check(statement):
    topic = " ".join(statement.split()[:5])
    wiki_summary = get_wikipedia_summary(topic)
    if not wiki_summary:
        return "🔍 Factual Check: Unable to verify (No article)"
    score = similarity_score(statement, wiki_summary)
    return f"🔍 Factual Check Score: {round(score, 2)} → {'✅ Pass' if score > 0.6 else '❌ Possible Hallucination'}"

def logical_check(response):
    steps = re.split(r'\.\s+', response.strip())
    for step in steps:
        if not any(kw in step.lower() for kw in ['because', 'therefore', 'so', 'thus']):
            return "🧠 Logical Check: ❌ Incomplete or broken reasoning"
    return "🧠 Logical Check: ✅ Steps appear logically connected"

def contextual_check(context, response):
    context_keywords = set(context.lower().split())
    response_keywords = set(response.lower().split())
    if len(context_keywords) == 0:
        return "📘 Contextual Relevance: No context provided"
    overlap = len(context_keywords.intersection(response_keywords)) / len(context_keywords)
    return f"📘 Contextual Relevance: {round(overlap * 100)}% → {'✅ Aligned' if overlap > 0.3 else '❌ Misaligned'}"


import requests

def extract_urls(text):
    return re.findall(r'https?://[^\s\)\]]+', text)

def validate_url(url):
    try:
        response = requests.head(url, timeout=5)
        return response.status_code == 200
    except:
        return False

def check_citations(text):
    urls = extract_urls(text)
    results = {}
    for url in urls:
        valid = validate_url(url)
        results[url] = "✅ Valid" if valid else "❌ Broken or Hallucinated"
    return results

