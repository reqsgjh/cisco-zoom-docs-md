# Notes on the Corpus

- Full Zoom documentation (218 MD files) was successfully downloaded from the official LLM-ready endpoints listed in https://developers.zoom.us/llms.txt.
- Cisco DevNet documentation was crawled using Scrapling ContentSpider (HTTP fetcher) targeting key hubs: Meraki API v1, NX-OS, IOS XE, Catalyst Center. ~80 pages captured.
- All files are in Markdown format suitable for chunking and embedding.
- The complete local collection is at the artifacts path; additional pushes can be done in batches if needed.
- For a full crawl of more Cisco product docs, increase max_pages and add more start_urls in the spider.

Ready for knowledge base embedding use.
