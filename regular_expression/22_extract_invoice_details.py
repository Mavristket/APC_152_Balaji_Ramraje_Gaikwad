"""
Program 22:
Extract invoice numbers, dates, and monetary amounts from invoice text
using regular expressions.
"""

import re

# Given invoice text
invoice_text = """
TAX INVOICE
Invoice No: INV-2026-0042
Customer: Apex Enterprises
Date: 15/10/2026
Due Date: 30-10-2026

Items Ordered:
1. Server Hardware       Qty: 2    Rate: Rs. 45,000.00    Amount: Rs. 90,000.00
2. Networking Switch     Qty: 1    Rate: Rs. 15,500.50    Amount: Rs. 15,500.50

Subtotal: Rs. 1,05,500.50
GST (18%): Rs. 19,000.00
Final Total: Rs. 1,24,500.50
Paid via Wire Transfer on 16/10/2026: Rs. 1,24,500.50
Reference: INV-9981-OLD
"""

print("Invoice Raw Text:\n", invoice_text.strip())
print("=" * 65)

# 1. Extract Invoice Numbers: e.g. INV-2026-0042 or INV-9981-OLD
invoice_num_pattern = r"\bINV-[A-Za-z0-9-]+\b"
invoice_numbers = re.findall(invoice_num_pattern, invoice_text)
print("1. Extracted Invoice Numbers:")
for inv in invoice_numbers:
    print(f"   - {inv}")
print("-" * 65)

# 2. Extract Dates: e.g. DD/MM/YYYY or DD-MM-YYYY
date_pattern = r"\b\d{2}[/-]\d{2}[/-]\d{4}\b"
dates = re.findall(date_pattern, invoice_text)
print("2. Extracted Dates:")
for d in dates:
    print(f"   - {d}")
print("-" * 65)

# 3. Extract Monetary Amounts: e.g. Rs. 45,000.00 or Rs. 1,24,500.50
amount_pattern = r"(?:Rs\.?|₹|\$)\s*[\d,]+(?:\.\d{2})?"
amounts = re.findall(amount_pattern, invoice_text)
print(f"3. Extracted Monetary Amounts (Count: {len(amounts)}):")
for amt in amounts:
    print(f"   - {amt}")
