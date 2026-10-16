"""
Program 26:
Extract DOI identifiers, publication years, email addresses, and URLs
from a collection of research paper references.
"""

import re

# Collection of research paper references
references_text = """
1. Vaswani, A., et al. (2017). Attention Is All You Need. Advances in Neural Information Processing Systems.
   DOI: 10.1016/j.neunet.2017.06.012. Available at: https://arxiv.org/abs/1706.03762.
   Contact author: ashish.vaswani@google.com.

2. LeCun, Y., Bengio, Y., & Hinton, G. (2015). Deep learning. Nature, 521(7553), 436-444.
   DOI: 10.1038/nature14539. Web link: https://www.nature.com/articles/nature14539.
   Inquiries: yann.lecun@nyu.edu or hinton@cs.toronto.edu.

3. He, K., Zhang, X., Ren, S., & Sun, J. (2016). Deep Residual Learning for Image Recognition.
   IEEE CVPR. DOI: 10.1109/CVPR.2016.90. URL: http://openaccess.thecvf.com/content_cvpr_2016.
   Correspondence: kaScript@microsoft.com.
"""

print("Research Paper References Collection:")
print(references_text.strip())
print("=" * 65)

# 1. DOIs: standard format starts with 10.XXXX/...
# Pattern: \b10\.\d{4,9}/[-._;()/:A-Za-z0-9]+\b
doi_pattern = r"\b10\.\d{4,9}/[-._;()/:A-Za-z0-9]+"
dois = re.findall(doi_pattern, references_text)
print("1. Extracted DOI Identifiers:")
for d in dois:
    print(f"   - {d}")
print("-" * 65)

# 2. Publication Years: e.g. (2017), (2015), (2016)
# Pattern: \b(?:19|20)\d{2}\b
year_pattern = r"\b(?:19|20)\d{2}\b"
years = sorted(list(set(re.findall(year_pattern, references_text))))
print("2. Extracted Publication Years (Unique):")
print(f"   {years}")
print("-" * 65)

# 3. Email Addresses
email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
emails = re.findall(email_pattern, references_text)
print("3. Extracted Email Addresses:")
for e in emails:
    print(f"   - {e}")
print("-" * 65)

# 4. URLs: starting with http:// or https://
url_pattern = r"https?://[^\s,;\"'>)]+"
urls = re.findall(url_pattern, references_text)
print("4. Extracted URLs:")
for u in urls:
    print(f"   - {u}")
