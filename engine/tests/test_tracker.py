"""
engine/tests/test_tracker.py
Unit tests for VisibilityTracker.
"""

import pytest
from engine.tracker import VisibilityTracker

def test_tracker_initialization():
    tracker = VisibilityTracker()
    assert len(tracker.questions) >= 100
    assert tracker.questions[0].qid == "Q001"

def test_tracker_run_quick():
    tracker = VisibilityTracker()
    results = tracker.run_tracking(limit=5)
    assert len(results) == 5
    assert results[0].qid == "Q001"
    assert results[0].google_rank in [">100", "1"]
    assert results[0].date is not None
