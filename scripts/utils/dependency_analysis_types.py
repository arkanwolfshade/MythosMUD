"""Shared TypedDict models for dependency analyzer scripts."""

from __future__ import annotations

from typing import NotRequired, TypedDict


class DepInfo(TypedDict):
    """Single dependency row (npm may include wanted/type; pip does not)."""

    current: str
    latest: str
    ecosystem: str
    update_type: str
    risk_level: str
    wanted: NotRequired[str]
    type: NotRequired[str]


class UpdateStrategy(TypedDict):
    strategy: str
    priority: str
    update_counts: dict[str, int]
    risk_counts: dict[str, int]
    total_packages: int


class BreakingChange(TypedDict):
    package: str
    current: str
    latest: str
    ecosystem: str


class RiskAssessment(TypedDict):
    breaking_changes: list[BreakingChange]
    security_vulnerabilities: list[str]
    compatibility_issues: list[str]
    overall_risk: str


class PriorityItem(TypedDict):
    package: str
    priority_score: int
    update_type: str
    risk_level: str
    current: str
    latest: str
    ecosystem: str


class AnalysisSnapshot(TypedDict):
    timestamp: str
    project: str
    client_dependencies: dict[str, DepInfo]
    server_dependencies: dict[str, DepInfo]
    update_strategy: UpdateStrategy
    risk_assessment: RiskAssessment
    priority_order: list[PriorityItem]
