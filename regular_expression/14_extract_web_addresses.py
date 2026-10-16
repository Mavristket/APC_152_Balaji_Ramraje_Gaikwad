"""
Program 14:
Write a program to identify web addresses beginning with http:// or https://.
"""

import re

# Text containing multiple web addresses
text = """
Explore educational resources at https://www.python.org and http://docs.scipy.org/numpy.
You can also view the code repository at https://github.com/torvalds/linux or HTTP insecure sites
like http://example.com:8080/path/to/page.html?ref=edu. Note that www.google.com without scheme is omitted.
"""

print("Input Text:\n", text.strip())
print("-" * 65)

# Pattern: https?:// matches http:// or https://, followed by non-whitespace characters
url_pattern = r"https?://[^\s,;\"'>)]+"
urls = re.findall(url_pattern, text)

print(f"Extracted Web Addresses (Count: {len(urls)}):")
for idx, url in enumerate(urls, start=1):
    print(f"  {idx}. {url}")
