from Wappalyzer import Wappalyzer, WebPage
import requests

def detect_technology(url):
    try:
        if not url.startswith("http"):
            url = "https://" + url

        wappalyzer = Wappalyzer.latest()
        webpage = WebPage.new_from_url(url)

      response = requests.get(
           url,
           timeout=10,
           headers={
               "User-Agent": "Mozilla/5.0"
    }
)

server = response.headers.get("Server", "Unknown")
powered_by = response.headers.get("X-Powered-By", "Unknown")

cloudflare = (
    response.headers.get("CF-RAY") is not None
    or response.headers.get("Server", "").lower() == "cloudflare"
)

return {
    "status": "success",
    "server": server,
    "powered_by": powered_by,
    "cloudflare": cloudflare,
    "technologies": sorted(list(wappalyzer.analyze(webpage)))
}

    except Exception as e:
        return {
            "error": str(e)
        }