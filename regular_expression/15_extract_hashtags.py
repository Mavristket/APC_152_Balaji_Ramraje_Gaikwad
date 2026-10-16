"""
Program 15:
Write a program to extract all hashtags from a social media post.
"""

import re

# Social media post
post = "Learning #Python and #DataScience is thrilling! Build #AI models with #NumPy, #Pandas & #MachineLearning #100DaysOfCode."
print("Social Media Post:\n", post)
print("-" * 60)

# Pattern: #\w+ matches # followed by letters, digits, or underscores
hashtags = re.findall(r"#\w+", post)

print(f"Extracted Hashtags (Count: {len(hashtags)}):")
for idx, tag in enumerate(hashtags, start=1):
    print(f"  {idx}. {tag}")

# Hashtags without the '#' symbol
clean_tags = [tag.lstrip("#") for tag in hashtags]
print("\nHashtag Tags Only (without #):", clean_tags)
