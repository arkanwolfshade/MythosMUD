#!/usr/bin/env python3
"""
Simple webhook receiver for testing MythosMUD alerts
"""

from datetime import datetime

from flask import Flask, jsonify, request

from server.logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)

app = Flask(__name__)


@app.route("/webhook", methods=["POST"])
def webhook():
    """Receive and log alert webhooks"""
    try:
        data = request.get_json()

        if not data:
            logger.warning("Received empty webhook data")
            return jsonify({"error": "No data received"}), 400

        # Log the alert
        logger.info("Received alert webhook", status=data.get('status', 'unknown'))
        logger.info("Webhook group labels", group_labels=data.get('groupLabels', {}))
        logger.info("Webhook common labels", common_labels=data.get('commonLabels', {}))

        # Log individual alerts
        alerts = data.get("alerts", [])
        for alert in alerts:
            alert_name = alert.get('labels', {}).get('alertname', 'unknown')
            alert_status = alert.get('status', 'unknown')
            alert_severity = alert.get('labels', {}).get('severity', 'unknown')
            alert_service = alert.get('labels', {}).get('service', 'unknown')
            alert_summary = alert.get('annotations', {}).get('summary', 'No summary')
            alert_description = alert.get('annotations', {}).get('description', 'No description')
            alert_starts_at = alert.get('startsAt', 'unknown')
            alert_ends_at = alert.get('endsAt')

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

        return jsonify({"status": "success", "message": "Webhook received"}), 200

    except Exception as e:
        logger.error("Error processing webhook", error=str(e), exc_info=True)
        return jsonify({"error": str(e)}), 500


@app.route("/health", methods=["GET"])
def health():
    """Health check endpoint"""
    return jsonify({"status": "healthy", "timestamp": datetime.utcnow().isoformat()}), 200


@app.route("/alerts", methods=["GET"])
def get_alerts():
    """Get recent alerts (for testing)"""
    # This would typically store alerts in a database
    # For now, just return a simple response
    return jsonify({"message": "Alert endpoint active", "timestamp": datetime.utcnow().isoformat()}), 200


if __name__ == "__main__":
    logger.info("Starting MythosMUD webhook receiver", host="0.0.0.0", port=5001)
    app.run(host="0.0.0.0", port=5001, debug=False)
