#!/usr/bin/env python3
import os
import glob
from datetime import datetime

BASE_DIR = "/home/rashid/Documents/blog"
SITEMAP_PATH = os.path.join(BASE_DIR, "sitemap.xml")
DOMAIN = "https://www.howtocrypt.com"

# Find all .html files
all_html = glob.glob(os.path.join(BASE_DIR, "**/*.html"), recursive=True)

urls = []
for file_path in sorted(all_html):
    rel_path = os.path.relpath(file_path, BASE_DIR)
    
    # Exclude 404 page from sitemap
    if rel_path == "404.html":
        continue
        
    # Convert index.html to directory URL where appropriate
    if rel_path == "index.html":
        url = f"{DOMAIN}/"
    elif rel_path.endswith("/index.html"):
        url = f"{DOMAIN}/{rel_path[:-10]}"
    else:
        url = f"{DOMAIN}/{rel_path}"
        
    # Get lastmod date
    mtime = os.path.getmtime(file_path)
    lastmod = datetime.fromtimestamp(mtime).strftime("%Y-%m-%d")
    
    # Priority & Changefreq determination
    if url == f"{DOMAIN}/":
        priority = "1.0"
        changefreq = "daily"
    elif "/reviews/" in url:
        priority = "0.9"
        changefreq = "weekly"
    elif "/compare/" in url or "/best/" in url:
        priority = "0.8"
        changefreq = "weekly"
    elif "/guides/" in url or "/questions/" in url:
        priority = "0.8"
        changefreq = "monthly"
    else:
        priority = "0.6"
        changefreq = "monthly"
        
    urls.append({
        "loc": url,
        "lastmod": lastmod,
        "changefreq": changefreq,
        "priority": priority
    })

xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

for u in urls:
    xml += '  <url>\n'
    xml += f'    <loc>{u["loc"]}</loc>\n'
    xml += f'    <lastmod>{u["lastmod"]}</lastmod>\n'
    xml += f'    <changefreq>{u["changefreq"]}</changefreq>\n'
    xml += f'    <priority>{u["priority"]}</priority>\n'
    xml += '  </url>\n'

xml += '</urlset>\n'

with open(SITEMAP_PATH, "w", encoding="utf-8") as f:
    f.write(xml)

print(f"Generated sitemap.xml with {len(urls)} URLs successfully!")
