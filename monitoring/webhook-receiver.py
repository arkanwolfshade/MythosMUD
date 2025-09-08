#!/usr/bin/env python3
"""
Simple webhook receiver for testing MythosMUD alerts
"""

import logging
from datetime import datetime

from flask import Flask, jsonify, request

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

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
        logger.info("Received alert webhook:")
        logger.info(f"  Status: {data.get('status', 'unknown')}")
        logger.info(f"  Group Labels: {data.get('groupLabels', {})}")
        logger.info(f"  Common Labels: {data.get('commonLabels', {})}")

        # Log individual alerts
        alerts = data.get("alerts", [])
        for alert in alerts:
            logger.info(f"  Alert: {alert.get('labels', {}).get('alertname', 'unknown')}")
            logger.info(f"    Status: {alert.get('status', 'unknown')}")
            logger.info(f"    Severity: {alert.get('labels', {}).get('severity', 'unknown')}")
            logger.info(f"    Service: {alert.get('labels', {}).get('service', 'unknown')}")
            logger.info(f"    Summary: {alert.get('annotations', {}).get('summary', 'No summary')}")
            logger.info(f"    Description: {alert.get('annotations', {}).get('description', 'No description')}")
            logger.info(f"    Starts At: {alert.get('startsAt', 'unknown')}")
            if alert.get("endsAt"):
                logger.info(f"    Ends At: {alert.get('endsAt')}")
            logger.info("  ---")

        return jsonify({"status": "success", "message": "Webhook received"}), 200

    except Exception as e:
        logger.error(f"Error processing webhook: {e}")
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
    logger.info("Starting MythosMUD webhook receiver on port 5001")
    app.run(host="0.0.0.0", port=5001, debug=False)
