#!/usr/bin/env python3
import glob
import os

SITEMAP_PATH = "/home/rashid/Documents/blog/sitemap.xml"

# Root pages
pages = [
    "https://www.howtocrypt.com/",
    "https://www.howtocrypt.com/exchanges.html",
    "https://www.howtocrypt.com/about.html",
    "https://www.howtocrypt.com/contact.html",
    "https://www.howtocrypt.com/affiliate-disclosure.html",
    "https://www.howtocrypt.com/privacy-policy.html",
    "https://www.howtocrypt.com/reviews/",
]

# Reviews
review_files = sorted(glob.glob("/home/rashid/Documents/blog/reviews/*-review.html"))
for rf in review_files:
    fname = os.path.basename(rf)
    pages.append(f"https://www.howtocrypt.com/reviews/{fname}")

# Compare
pages.extend([
    "https://www.howtocrypt.com/compare/",
    "https://www.howtocrypt.com/compare/bybit-vs-bitget.html",
    "https://www.howtocrypt.com/compare/bybit-vs-binance.html",
])

# Guides
pages.extend([
    "https://www.howtocrypt.com/guides/",
    "https://www.howtocrypt.com/guides/how-to-sign-up-bybit.html",
    "https://www.howtocrypt.com/guides/how-to-complete-kyc.html",
])

# Questions
pages.extend([
    "https://www.howtocrypt.com/questions/",
    "https://www.howtocrypt.com/questions/trade-futures-without-kyc.html",
])

# Best
pages.extend([
    "https://www.howtocrypt.com/best/",
    "https://www.howtocrypt.com/best/best-exchange-beginners.html",
])

# Country
pages.extend([
    "https://www.howtocrypt.com/country/",
    "https://www.howtocrypt.com/country/best-exchange-india.html",
])

xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for p in pages:
    xml += f"  <url><loc>{p}</loc></url>\n"
xml += "</urlset>\n"

with open(SITEMAP_PATH, "w", encoding="utf-8") as f:
    f.write(xml)

print(f"Updated sitemap.xml with {len(pages)} URLs successfully!")
