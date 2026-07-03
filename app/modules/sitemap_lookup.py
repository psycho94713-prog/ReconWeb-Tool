import httpx
import xml.etree.ElementTree as ET


async def get_sitemap(domain: str):
    """
    Fetch and analyze sitemap.xml
    """

    url = f"https://{domain}/sitemap.xml"

    try:
        async with httpx.AsyncClient(timeout=15, follow_redirects=True) as client:
            response = await client.get(url)

        if response.status_code != 200:
            return {
                "available": False,
                "status_code": response.status_code,
                "message": "Sitemap not found"
            }

        root = ET.fromstring(response.text)

        namespace = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}

        urls = root.findall("sm:url", namespace)

        pages = []

        for item in urls[:20]:
            loc = item.find("sm:loc", namespace)
            lastmod = item.find("sm:lastmod", namespace)

            pages.append({
                "url": loc.text if loc is not None else "",
                "last_modified": lastmod.text if lastmod is not None else "Unknown"
            })

        return {
            "available": True,
            "status_code": response.status_code,
            "total_urls": len(urls),
            "sample_urls": pages
        }

    except Exception as e:
        return {
            "available": False,
            "error": str(e)
        }