import urllib.request
import os
from pathlib import Path

with open("urls.txt") as f:
    urls = [line.strip() for line in f if line.strip()]

print(f"Downloading {len(urls)} files...")
success = 0
for i, url in enumerate(urls, 1):
    try:
        # Create path from URL
        path = url.replace("https://developers.zoom.us/docs/", "").lstrip("/")
        if not path.endswith(".md"):
            path += ".md"
        full_path = Path(path)
        full_path.parent.mkdir(parents=True, exist_ok=True)
        
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            content = resp.read().decode("utf-8", errors="replace")
        
        full_path.write_text(content, encoding="utf-8")
        success += 1
        if i % 20 == 0:
            print(f"  {i}/{len(urls)} done")
    except Exception as e:
        print(f"Failed {url}: {e}")

print(f"Successfully downloaded {success}/{len(urls)} files")
