"""
Program 21:
Write a program to remove HTML tags, extra whitespace, and unwanted punctuation
from a text document.
"""

import re

# Raw HTML document text with extra spaces, newlines, and punctuation
html_doc = """
<div class="content">
    <h1>Welcome to Python Programming!</h1>
    <p>Python is a powerful, versatile language &amp; easy-to-learn... <a href="#">Learn More</a></p>
    <ul>
        <li>Fast execution;</li>
        <li>Rich ecosystem (NumPy, Pandas, etc.)!</li>
    </ul>
</div>
"""

print("Original Raw HTML Document:")
print(html_doc)
print("=" * 65)

# Step 1: Remove HTML tags (anything enclosed in <...>)
no_html = re.sub(r"<[^>]+>", " ", html_doc)
print("Step 1 - After Removing HTML Tags:")
print(no_html.strip())
print("-" * 65)

# Step 2: Remove HTML entities like &amp; &lt; etc.
no_entities = re.sub(r"&[a-zA-Z]+;", " ", no_html)

# Step 3: Remove unwanted punctuation (keep alphanumeric characters and whitespace)
no_punct = re.sub(r"[^\w\s]", "", no_entities)
print("Step 2 & 3 - After Removing Unwanted Punctuation:")
print(no_punct.strip())
print("-" * 65)

# Step 4: Remove extra whitespace (replace multiple spaces/tabs/newlines with a single space)
cleaned_text = re.sub(r"\s+", " ", no_punct).strip()
print("Final Cleaned Text (Tags, Punctuation, and Extra Spaces Removed):")
print(cleaned_text)
