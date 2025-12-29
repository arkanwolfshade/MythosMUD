"""
Behavior engine for NPCs.

This module provides the deterministic behavior engine that evaluates rules
based on context and executes actions in a priority-based manner.

As noted in the Pnakotic Manuscripts, proper behavioral programming is essential
for maintaining the delicate balance between order and chaos in our eldritch
entity management systems.
"""

from collections.abc import Callable
from typing import Any

from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class BehaviorEngine:
    """
    Deterministic behavior engine for NPCs.

    This engine evaluates rules based on context and executes actions
    in a deterministic, priority-based manner.
    """

    def __init__(self):
        """Initialize the behavior engine."""
        self.rules: list[dict[str, Any]] = []
        self.action_handlers: dict[str, Callable] = {}
        self.state: dict[str, Any] = {}

        logger.debug("Behavior engine initialized", engine_id=id(self))

    def add_rule(self, rule: dict[str, Any]) -> bool:
        """
        Add a behavior rule to the engine.

        Args:
            rule: Rule dictionary with name, condition, action, and priority

        Returns:
            bool: True if rule was added successfully
        """
        try:
            required_fields = ["name", "condition", "action", "priority"]
            if not all(field in rule for field in required_fields):
                logger.error("Rule missing required fields", rule=rule)
                return False

            # Remove existing rule with same name
            self.rules = [r for r in self.rules if r["name"] != rule["name"]]

            # Add new rule
            self.rules.append(rule)
            logger.debug(
                "Added behavior rule",
                rule_name=rule["name"],
                priority=rule.get("priority", 0),
                total_rules=len(self.rules),
            )
            return True

        except (TypeError, KeyError, AttributeError, ValueError) as e:
            # Defensive: Catch specific exceptions when adding behavior rules
            # This handles malformed input (TypeError, KeyError, AttributeError, ValueError)
            # and ensures the method always returns a bool
            logger.error("Error adding behavior rule", error=str(e), error_type=type(e).__name__)
            return False

    def remove_rule(self, rule_name: str) -> bool:
        """
        Remove a behavior rule from the engine.

        Args:
            rule_name: Name of the rule to remove

        Returns:
            bool: True if rule was removed successfully
        """
        try:
            original_count = len(self.rules)
            self.rules = [r for r in self.rules if r["name"] != rule_name]

            if len(self.rules) < original_count:
                logger.debug("Removed behavior rule", rule_name=rule_name)
                return True
            else:
                logger.warning("Rule not found for removal", rule_name=rule_name)
                return False

        except (TypeError, KeyError, AttributeError) as e:
            logger.error("Error removing behavior rule", error=str(e), error_type=type(e).__name__)
            return False

    def get_rules(self) -> list[dict[str, Any]]:
        """Get all behavior rules."""
        return self.rules.copy()

    def _evaluate_equality(self, condition: str, context: dict[str, Any]) -> bool | None:
        """
        Evaluate equality condition (==).

        Returns:
            bool if condition matches, None if not an equality condition
        """
        if "==" not in condition:
            return None

        parts = condition.split("==")
        if len(parts) != 2:
            return None

        var_name = parts[0].strip()
        expected_value = parts[1].strip().strip("\"'")
        context_value = context.get(var_name, "")

        # Handle boolean values properly
        if expected_value.lower() in ["true", "false"]:
            return bool(context_value) == (expected_value.lower() == "true")
        return str(context_value) == expected_value

    def _evaluate_inequality(self, condition: str, context: dict[str, Any]) -> bool | None:
        """
        Evaluate inequality condition (!=).

        Returns:
            bool if condition matches, None if not an inequality condition
        """
        if "!=" not in condition:
            return None

        parts = condition.split("!=")
        if len(parts) != 2:
            return None

        var_name = parts[0].strip()
        expected_value = parts[1].strip().strip("\"'")
        return str(context.get(var_name, "")) != expected_value

    def _evaluate_numeric_comparison(self, condition: str, context: dict[str, Any], operator: str) -> bool | None:
        """
        Evaluate numeric comparison conditions (>=, <=, >, <).

        Args:
            condition: Condition string to evaluate
            context: Context dictionary with variables
            operator: Comparison operator (">=", "<=", ">", "<")

        Returns:
            bool if condition matches, None if not a numeric comparison
        """
        if operator not in condition:
            return None

        parts = condition.split(operator)
        if len(parts) != 2:
            return None

        var_name = parts[0].strip()
        threshold_str = parts[1].strip()
        # Check if threshold is a variable name or a literal value
        threshold = float(context.get(threshold_str, threshold_str))
        var_value = float(context.get(var_name, 0))

        if operator == ">=":
            return var_value >= threshold
        elif operator == "<=":
            return var_value <= threshold
        elif operator == ">":
            return var_value > threshold
        elif operator == "<":
            return var_value < threshold

        return None

    def _try_evaluators(self, condition: str, context: dict[str, Any]) -> bool | None:
        """
        Try multiple evaluator methods in sequence.

        Args:
            condition: Condition string to evaluate
            context: Context dictionary with variables

        Returns:
            bool if condition matches, None if no evaluator matched
        """
        # Try equality comparison first
        result = self._evaluate_equality(condition, context)
        if result is not None:
            return result

        # Try inequality comparison
        result = self._evaluate_inequality(condition, context)
        if result is not None:
            return result

        # Try numeric comparisons (check >= and <= BEFORE > and < to avoid incorrect parsing)
        numeric_operators = [">=", "<=", ">", "<"]
        for operator in numeric_operators:
            result = self._evaluate_numeric_comparison(condition, context, operator)
            if result is not None:
                return result

        return None

    def _evaluate_boolean_condition(self, condition: str, context: dict[str, Any]) -> bool:
        """
        Evaluate boolean conditions and variable lookups.

        Args:
            condition: Condition string to evaluate
            context: Context dictionary with variables

        Returns:
            bool: Result of boolean evaluation
        """
        if condition == "true":
            return True
        if condition == "false":
            return False

        # Treat as boolean variable
        return bool(context.get(condition, False))

    def evaluate_condition(self, condition: str, context: dict[str, Any]) -> bool:
        """
        Evaluate a condition string against context.

        Args:
            condition: Condition string to evaluate
            context: Context dictionary with variables

        Returns:
            bool: True if condition is met
        """
        try:
            logger.debug("Evaluating behavior condition", condition=condition, context_keys=list(context.keys()))

            # Try comparison evaluators first
            result = self._try_evaluators(condition, context)
            if result is not None:
                return result

            # Fall back to boolean condition evaluation
            return self._evaluate_boolean_condition(condition, context)

        except (TypeError, KeyError, ValueError, AttributeError) as e:
            logger.error(
                "Error evaluating condition",
                condition=condition,
                context_keys=list(context.keys()),
                error=str(e),
                error_type=type(e).__name__,
            )
            return False

    def get_applicable_rules(self, context: dict[str, Any]) -> list[dict[str, Any]]:
        """
        Get rules that are applicable given the current context.

        Args:
            context: Current context dictionary

        Returns:
            List of applicable rules sorted by priority (highest first)
        """
        applicable_rules = []

        for rule in self.rules:
            condition_result = self.evaluate_condition(rule["condition"], context)

            if condition_result:
                applicable_rules.append(rule)

        # Sort by priority (highest first)
        applicable_rules.sort(key=lambda r: r["priority"], reverse=True)
        return applicable_rules

    def register_action_handler(self, action_name: str, handler: Callable) -> bool:
        """
        Register an action handler for a specific action.

        Args:
            action_name: Name of the action
            handler: Function to handle the action

        Returns:
            bool: True if handler was registered successfully
        """
        try:
            self.action_handlers[action_name] = handler
            # Temporarily disable logging to avoid potential recursion issues
            # logger.debug("Registered action handler", action_name=action_name)
            return True
        except (TypeError, AttributeError) as e:
            logger.error(
                "Error registering action handler", action_name=action_name, error=str(e), error_type=type(e).__name__
            )
            return False

    def execute_action(self, action_name: str, context: dict[str, Any]) -> bool:
        """
        Execute a specific action.

        Args:
            action_name: Name of the action to execute
            context: Context for the action

        Returns:
            bool: True if action was executed successfully
        """
        try:
            if action_name not in self.action_handlers:
                logger.warning("No handler registered for action", action_name=action_name)
                return False

            handler = self.action_handlers[action_name]
            result = handler(context)
            logger.debug("Executed action", action_name=action_name, result=result)
            return result

        except (KeyError, TypeError, AttributeError) as e:
            logger.error("Error executing action", action_name=action_name, error=str(e), error_type=type(e).__name__)
            return False

    def execute_applicable_rules(self, context: dict[str, Any]) -> bool:
        """
        Execute all applicable rules based on context.

        Args:
            context: Current context dictionary

        Returns:
            bool: True if at least one rule was executed successfully
        """
        try:
            applicable_rules = self.get_applicable_rules(context)

            if not applicable_rules:
                logger.debug(
                    "No applicable rules found for context",
                    context_keys=list(context.keys()),
                    total_rules=len(self.rules),
                )
                return True  # No rules to execute is considered success

            # Execute highest priority rule only (deterministic behavior)
            highest_priority_rule = applicable_rules[0]
            logger.debug(
                "Executing highest priority rule",
                rule_name=highest_priority_rule["name"],
                priority=highest_priority_rule["priority"],
                action=highest_priority_rule["action"],
            )

            result = self.execute_action(highest_priority_rule["action"], context)
            logger.debug("Rule execution completed", rule_name=highest_priority_rule["name"], success=result)
            return result

        except (TypeError, KeyError, AttributeError) as e:
            logger.error(
                "Error executing applicable rules",
                context_keys=list(context.keys()),
                total_rules=len(self.rules),
                error=str(e),
                error_type=type(e).__name__,
            )
            return False
