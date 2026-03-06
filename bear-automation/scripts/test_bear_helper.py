#!/usr/bin/env python3
"""
Test script for Bear automation helper
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.bear_helper import BearAutomation


def test_url_encoding():
    """Test URL encoding"""
    print("Testing URL encoding...")

    # Test basic encoding
    params = {"text": "Hello World!", "tags": "test,demo"}
    encoded = BearAutomation._encode_params(params)
    print(f"  Encoded params: {encoded}")

    assert "Hello+World" in encoded or "Hello%20World" in encoded
    assert "test%2Cdemo" in encoded or "test,demo" in encoded
    print("  ✓ URL encoding works")


def test_build_url():
    """Test URL building"""
    print("\nTesting URL building...")

    url = BearAutomation._build_url("create", {"text": "Test", "tags": "demo"})
    print(f"  Built URL: {url}")

    assert url.startswith("bear://x-callback-url/create?")
    assert "text=" in url
    assert "tags=" in url
    print("  ✓ URL building works")


def test_create_note_url():
    """Test create note URL generation (without opening)"""
    print("\nTesting create note URL generation...")

    # Temporarily override _open_url to not actually open
    original_open = BearAutomation._open_url
    BearAutomation._open_url = lambda url: None

    try:
        url = BearAutomation.create_note(
            title="Test Note",
            text="This is a test",
            tags=["test", "demo"],
            pin=True
        )

        print(f"  Generated URL: {url}")

        assert "bear://x-callback-url/create?" in url
        assert "title=" in url
        assert "text=" in url
        assert "tags=" in url
        assert "pin=yes" in url
        print("  ✓ Create note URL generation works")

    finally:
        BearAutomation._open_url = original_open


def test_add_text_url():
    """Test add text URL generation"""
    print("\nTesting add text URL generation...")

    original_open = BearAutomation._open_url
    BearAutomation._open_url = lambda url: None

    try:
        url = BearAutomation.add_text(
            title="Daily Log",
            text="New entry",
            mode="append",
            timestamp=True
        )

        print(f"  Generated URL: {url}")

        assert "bear://x-callback-url/add-text?" in url
        assert "title=" in url
        assert "text=" in url
        assert "mode=append" in url
        assert "timestamp=yes" in url
        print("  ✓ Add text URL generation works")

    finally:
        BearAutomation._open_url = original_open


def test_search_url():
    """Test search URL generation"""
    print("\nTesting search URL generation...")

    original_open = BearAutomation._open_url
    BearAutomation._open_url = lambda url: None

    try:
        url = BearAutomation.search(term="meeting", tag="work")

        print(f"  Generated URL: {url}")

        assert "bear://x-callback-url/search?" in url
        assert "term=" in url
        assert "tag=" in url
        print("  ✓ Search URL generation works")

    finally:
        BearAutomation._open_url = original_open


def run_all_tests():
    """Run all tests"""
    print("=" * 60)
    print("Bear Automation Helper - Test Suite")
    print("=" * 60)

    try:
        test_url_encoding()
        test_build_url()
        test_create_note_url()
        test_add_text_url()
        test_search_url()

        print("\n" + "=" * 60)
        print("✓ All tests passed!")
        print("=" * 60)
        return 0

    except AssertionError as e:
        print(f"\n✗ Test failed: {e}")
        return 1
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(run_all_tests())
