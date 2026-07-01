from app.services.http_client import get


def detect_cms(domain: str):
    try:
        response = get(f"https://{domain}")

        html = response.text.lower()

        if "wp-content" in html or "wordpress" in html:
            cms = "WordPress"

        elif "joomla" in html:
            cms = "Joomla"

        elif "drupal" in html:
            cms = "Drupal"

        elif "shopify" in html:
            cms = "Shopify"

        elif "magento" in html:
            cms = "Magento"

        elif "wix.com" in html:
            cms = "Wix"

        else:
            cms = "Unknown"

        return {
            "status": "success",
            "cms": cms
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }