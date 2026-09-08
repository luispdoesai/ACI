"""
Web Scraper & Content Extractor Utility
Extracts clean markdown or text content from web pages for research and lead analysis.
"""

import sys
import json
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import re
from typing import Dict, Any


def extract_page_text(url: str, timeout: int = 10) -> Dict[str, Any]:
    """Fetch URL and extract title and cleaned text content."""
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
    }

    req = Request(url, headers=headers)
    try:
        with urlopen(req, timeout=timeout) as response:
            html = response.read().decode("utf-8", errors="ignore")
            
            # Simple regex parser for titles and clean body text
            title_match = re.search(r"<title>(.*?)</title>", html, re.IGNORECASE | re.DOTALL)
            title = title_match.group(1).strip() if title_match else "No Title"

            # Remove scripts, styles, and html tags
            cleaned_html = re.sub(r"<(script|style).*?>.*?</\1>", "", html, flags=re.DOTALL | re.IGNORECASE)
            text_lines = re.sub(r"<[^>]+>", " ", cleaned_html).split()
            clean_text = " ".join(text_lines)

            return {
                "success": True,
                "url": url,
                "title": title,
                "character_count": len(clean_text),
                "preview": clean_text[:500] + ("..." if len(clean_text) > 500 else "")
            }

    except HTTPError as e:
        return {"success": False, "url": url, "error": f"HTTP Error: {e.code}"}
    except URLError as e:
        return {"success": False, "url": url, "error": f"URL Error: {e.reason}"}
    except Exception as e:
        return {"success": False, "url": url, "error": str(e)}


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python web_scraper.py <url>")
        sys.exit(1)

    target_url = sys.argv[1]
    result = extract_page_text(target_url)
    print(json.dumps(result, indent=2))
