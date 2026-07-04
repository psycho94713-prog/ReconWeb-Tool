import httpx
from datetime import datetime


async def get_wayback(domain: str):
    """
    Fetch latest Wayback Machine snapshot for a domain.
    """

    target_url = f"https://{domain}"

    url = (
      "https://archive.org/wayback/available"
       f"?url={target_url}"
    )

    try:
        async with httpx.AsyncClient(timeout=15) as client:
            response = await client.get(url)

        response.raise_for_status()
        data = response.json()

        snapshot = (
            data.get("archived_snapshots", {})
            .get("closest")
        )

        if not snapshot:
            return {
                "available": False,
                "message": "No archived snapshot found."
            }

        timestamp = snapshot.get("timestamp")

        readable_date = None
        if timestamp:
            try:
                readable_date = datetime.strptime(
                    timestamp,
                    "%Y%m%d%H%M%S"
                ).strftime("%Y-%m-%d %H:%M:%S UTC")
            except Exception:
                readable_date = timestamp

        return {
            "available": True,
            "archive_url": snapshot.get("url"),
            "timestamp": timestamp,
            "date": readable_date,
            "http_status": snapshot.get("status")
        }

    except httpx.RequestError as e:
        return {
            "available": False,
            "error": f"Network Error: {str(e)}"
        }

    except Exception as e:
        return {
            "available": False,
            "error": str(e)
        }