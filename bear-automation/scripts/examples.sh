#!/bin/bash

# Bear Automation - Usage Examples
# This script demonstrates various use cases for the Bear automation skill

set -e

# Source the helper functions
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/bear_helper.sh"

echo "=========================================="
echo "Bear Automation - Usage Examples"
echo "=========================================="
echo ""

# Example 1: Create a simple note
echo "Example 1: Creating a simple note"
echo "Command: bear_create --title 'Test Note' --text 'This is a test note' --tags 'test,demo'"
echo ""
read -p "Press Enter to execute (or Ctrl+C to skip)..."
bear_create --title "Test Note" --text "This is a test note created by Bear automation skill" --tags "test,demo"
echo "✓ Note created"
echo ""

# Example 2: Add text to existing note
echo "Example 2: Adding text to existing note"
echo "Command: bear_add_text --title 'Test Note' --text 'Additional content' --mode append"
echo ""
read -p "Press Enter to execute (or Ctrl+C to skip)..."
bear_add_text --title "Test Note" --text "Additional content added at $(date)" --mode append
echo "✓ Text added"
echo ""

# Example 3: Search notes
echo "Example 3: Searching notes"
echo "Command: bear_search --term 'test' --tag 'demo'"
echo ""
read -p "Press Enter to execute (or Ctrl+C to skip)..."
bear_search --term "test" --tag "demo"
echo "✓ Search executed"
echo ""

# Example 4: Create daily journal
echo "Example 4: Creating daily journal entry"
echo "Command: bear_daily_journal"
echo ""
read -p "Press Enter to execute (or Ctrl+C to skip)..."
bear_daily_journal
echo "✓ Daily journal created"
echo ""

# Example 5: Quick capture from clipboard
echo "Example 5: Quick capture from clipboard"
echo "First, let's copy some text to clipboard..."
echo "This is a test capture from clipboard" | pbcopy
echo "Command: bear_capture_clipboard 'inbox'"
echo ""
read -p "Press Enter to execute (or Ctrl+C to skip)..."
bear_capture_clipboard "inbox"
echo "✓ Clipboard content captured"
echo ""

# Example 6: Add log entry
echo "Example 6: Adding log entry"
echo "Command: bear_log_entry 'Completed automation testing'"
echo ""
read -p "Press Enter to execute (or Ctrl+C to skip)..."
bear_log_entry "Completed automation testing"
echo "✓ Log entry added"
echo ""

# Example 7: Open tag collection
echo "Example 7: Opening tag collection"
echo "Command: bear_open_tag 'test'"
echo ""
read -p "Press Enter to execute (or Ctrl+C to skip)..."
bear_open_tag "test"
echo "✓ Tag collection opened"
echo ""

# Example 8: Show today's notes
echo "Example 8: Showing today's notes"
echo "Command: bear_today"
echo ""
read -p "Press Enter to execute (or Ctrl+C to skip)..."
bear_today
echo "✓ Today's notes displayed"
echo ""

echo "=========================================="
echo "All examples completed!"
echo "=========================================="
echo ""
echo "Check your Bear app to see the results."
echo ""
echo "To clean up test notes:"
echo "1. Open Bear"
echo "2. Search for tag: #test"
echo "3. Delete the test notes"
echo ""
