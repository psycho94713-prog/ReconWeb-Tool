from Wappalyzer import Wappalyzer, WebPage

def detect_technology(url):
    try:
        if not url.startswith("http"):
            url = "https://" + url

        wappalyzer = Wappalyzer.latest()
        webpage = WebPage.new_from_url(url)

        return {
            "technologies": list(wappalyzer.analyze(webpage))
        }

    except Exception as e:
        return {
            "error": str(e)
        }