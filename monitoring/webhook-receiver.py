#!/usr/bin/env python3
"""
Simple webhook receiver for testing MythosMUD alerts
"""

from datetime import UTC, datetime
from sqlite3 import DatabaseError

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from server.logging.enhanced_logging_config import get_logger
from sqlalchemy.exc import SQLAlchemyError

logger = get_logger(__name__)

app = FastAPI(title="MythosMUD Webhook Receiver")


@app.post("/webhook")
async def webhook(request: Request):
    """Receive and log alert webhooks"""
    try:
        data = await request.json()

        if not data:
            logger.warning("Received empty webhook data")
            return JSONResponse(status_code=400, content={"error": "No data received"})

        # Log the alert
        logger.info("Received alert webhook", status=data.get("status", "unknown"))
        logger.info("Webhook group labels", group_labels=data.get("groupLabels", {}))
        logger.info("Webhook common labels", common_labels=data.get("commonLabels", {}))

        # Log individual alerts
        alerts = data.get("alerts", [])
        for alert in alerts:
            alert_name = alert.get("labels", {}).get("alertname", "unknown")
            alert_status = alert.get("status", "unknown")
            alert_severity = alert.get("labels", {}).get("severity", "unknown")
            alert_service = alert.get("labels", {}).get("service", "unknown")
            alert_summary = alert.get("annotations", {}).get("summary", "No summary")
            alert_description = alert.get("annotations", {}).get("description", "No description")
            alert_starts_at = alert.get("startsAt", "unknown")
            alert_ends_at = alert.get("endsAt")

            logger.info(
                "Alert details",
                alert_name=alert_name,
                status=alert_status,
                severity=alert_severity,
                service=alert_service,
                summary=alert_summary,
                description=alert_description,
                starts_at=alert_starts_at,
                ends_at=alert_ends_at,
            )

        return {"status": "success", "message": "Webhook received"}

    except (DatabaseError, SQLAlchemyError) as e:
        logger.error("Error processing webhook", error=str(e), exc_info=True)
        # Return only a generic error message to avoid exposing internal details.
        return JSONResponse(
            status_code=500,
            content={"error": "An error occurred processing the webhook"},
        )


@app.get("/health")
async def health():
    """Health check endpoint"""
    return {"status": "healthy", "timestamp": datetime.now(UTC).isoformat()}


@app.get("/alerts")
async def get_alerts():
    """Get recent alerts (for testing)"""
    # This would typically store alerts in a database
    # For now, just return a simple response
    return {"message": "Alert endpoint active", "timestamp": datetime.now(UTC).isoformat()}


if __name__ == "__main__":
    import uvicorn

    logger.info("Starting MythosMUD webhook receiver", host="0.0.0.0", port=5001)
    uvicorn.run(app, host="0.0.0.0", port=5001)
