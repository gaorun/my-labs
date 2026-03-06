#!/bin/bash

# Bear App x-callback-url Helper Script
# Provides convenient functions for Bear automation

set -e

# Color output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# URL encode function
urlencode() {
    local string="${1}"
    local strlen=${#string}
    local encoded=""
    local pos c o

    for (( pos=0 ; pos<strlen ; pos++ )); do
        c=${string:$pos:1}
        case "$c" in
            [-_.~a-zA-Z0-9] ) o="${c}" ;;
            * ) printf -v o '%%%02x' "'$c"
        esac
        encoded+="${o}"
    done
    echo "${encoded}"
}

# Build Bear URL
build_bear_url() {
    local action="$1"
    shift
    local params="$@"
    echo "bear://x-callback-url/${action}?${params}"
}

# Open Bear URL
open_bear_url() {
    local url="$1"
    echo -e "${GREEN}Opening Bear:${NC} $url"
    open "$url"
}

# Create note
bear_create() {
    local title=""
    local text=""
    local tags=""
    local pin="no"
    local open_note="no"
    local edit="no"

    while [[ $# -gt 0 ]]; do
        case $1 in
            --title)
                title="$2"
                shift 2
                ;;
            --text)
                text="$2"
                shift 2
                ;;
            --tags)
                tags="$2"
                shift 2
                ;;
            --pin)
                pin="yes"
                shift
                ;;
            --open)
                open_note="yes"
                shift
                ;;
            --edit)
                edit="yes"
                shift
                ;;
            *)
                echo -e "${RED}Unknown option: $1${NC}"
                return 1
                ;;
        esac
    done

    if [[ -z "$text" ]]; then
        echo -e "${RED}Error: --text is required${NC}"
        return 1
    fi

    local params=""
    [[ -n "$title" ]] && params+="title=$(urlencode "$title")&"
    params+="text=$(urlencode "$text")&"
    [[ -n "$tags" ]] && params+="tags=$(urlencode "$tags")&"
    params+="pin=${pin}&"
    params+="open_note=${open_note}&"
    params+="edit=${edit}"

    local url=$(build_bear_url "create" "$params")
    open_bear_url "$url"
}

# Add text to note
bear_add_text() {
    local title=""
    local note_id=""
    local text=""
    local mode="append"
    local tags=""

    while [[ $# -gt 0 ]]; do
        case $1 in
            --title)
                title="$2"
                shift 2
                ;;
            --id)
                note_id="$2"
                shift 2
                ;;
            --text)
                text="$2"
                shift 2
                ;;
            --mode)
                mode="$2"
                shift 2
                ;;
            --tags)
                tags="$2"
                shift 2
                ;;
            *)
                echo -e "${RED}Unknown option: $1${NC}"
                return 1
                ;;
        esac
    done

    if [[ -z "$text" ]]; then
        echo -e "${RED}Error: --text is required${NC}"
        return 1
    fi

    local params=""
    [[ -n "$title" ]] && params+="title=$(urlencode "$title")&"
    [[ -n "$note_id" ]] && params+="id=$(urlencode "$note_id")&"
    params+="text=$(urlencode "$text")&"
    params+="mode=${mode}&"
    [[ -n "$tags" ]] && params+="tags=$(urlencode "$tags")&"
    params="${params%&}"

    local url=$(build_bear_url "add-text" "$params")
    open_bear_url "$url"
}

# Search notes
bear_search() {
    local term=""
    local tag=""

    while [[ $# -gt 0 ]]; do
        case $1 in
            --term)
                term="$2"
                shift 2
                ;;
            --tag)
                tag="$2"
                shift 2
                ;;
            *)
                echo -e "${RED}Unknown option: $1${NC}"
                return 1
                ;;
        esac
    done

    local params=""
    [[ -n "$term" ]] && params+="term=$(urlencode "$term")&"
    [[ -n "$tag" ]] && params+="tag=$(urlencode "$tag")&"
    params="${params%&}"

    local url=$(build_bear_url "search" "$params")
    open_bear_url "$url"
}

# Open note
bear_open() {
    local title=""
    local note_id=""
    local header=""

    while [[ $# -gt 0 ]]; do
        case $1 in
            --title)
                title="$2"
                shift 2
                ;;
            --id)
                note_id="$2"
                shift 2
                ;;
            --header)
                header="$2"
                shift 2
                ;;
            *)
                echo -e "${RED}Unknown option: $1${NC}"
                return 1
                ;;
        esac
    done

    local params=""
    [[ -n "$title" ]] && params+="title=$(urlencode "$title")&"
    [[ -n "$note_id" ]] && params+="id=$(urlencode "$note_id")&"
    [[ -n "$header" ]] && params+="header=$(urlencode "$header")&"
    params="${params%&}"

    local url=$(build_bear_url "open-note" "$params")
    open_bear_url "$url"
}

# Open tag
bear_open_tag() {
    local tag_name="$1"

    if [[ -z "$tag_name" ]]; then
        echo -e "${RED}Error: tag name is required${NC}"
        return 1
    fi

    local params="name=$(urlencode "$tag_name")"
    local url=$(build_bear_url "open-tag" "$params")
    open_bear_url "$url"
}

# Rename tag
bear_rename_tag() {
    local old_name="$1"
    local new_name="$2"

    if [[ -z "$old_name" ]] || [[ -z "$new_name" ]]; then
        echo -e "${RED}Error: both old and new tag names are required${NC}"
        return 1
    fi

    local params="name=$(urlencode "$old_name")&new_name=$(urlencode "$new_name")"
    local url=$(build_bear_url "rename-tag" "$params")
    open_bear_url "$url"
}

# Delete tag
bear_delete_tag() {
    local tag_name="$1"

    if [[ -z "$tag_name" ]]; then
        echo -e "${RED}Error: tag name is required${NC}"
        return 1
    fi

    local params="name=$(urlencode "$tag_name")"
    local url=$(build_bear_url "delete-tag" "$params")
    open_bear_url "$url"
}

# Show special collections
bear_untagged() {
    open_bear_url "bear://x-callback-url/untagged"
}

bear_today() {
    open_bear_url "bear://x-callback-url/today"
}

bear_todo() {
    open_bear_url "bear://x-callback-url/todo"
}

bear_locked() {
    open_bear_url "bear://x-callback-url/locked"
}

# Grab URL
bear_grab_url() {
    local url="$1"
    local tags="$2"
    local pin="${3:-no}"

    if [[ -z "$url" ]]; then
        echo -e "${RED}Error: URL is required${NC}"
        return 1
    fi

    local params="url=$(urlencode "$url")"
    [[ -n "$tags" ]] && params+="&tags=$(urlencode "$tags")"
    [[ "$pin" == "yes" ]] && params+="&pin=yes"

    local bear_url=$(build_bear_url "grab-url" "$params")
    open_bear_url "$bear_url"
}

# Get tags
bear_get_tags() {
    local token="$1"

    if [[ -z "$token" ]]; then
        echo -e "${RED}Error: token is required${NC}"
        echo -e "${YELLOW}Generate token in Bear → Help → API Token${NC}"
        return 1
    fi

    local params="token=$(urlencode "$token")"
    local url=$(build_bear_url "tags" "$params")
    open_bear_url "$url"
}

# Quick capture from clipboard
bear_capture_clipboard() {
    local tags="${1:-inbox}"
    local content=$(pbpaste)

    if [[ -z "$content" ]]; then
        echo -e "${YELLOW}Warning: Clipboard is empty${NC}"
        return 1
    fi

    bear_create --text "$content" --tags "$tags"
}

# Daily journal entry
bear_daily_journal() {
    local date=$(date +"%Y-%m-%d")
    local title="Journal - $date"
    local text="# Daily Journal\n\n## What I did today:\n\n"

    bear_create --title "$title" --text "$text" --tags "journal" --edit --open
}

# Append to daily log
bear_log_entry() {
    local entry="$1"

    if [[ -z "$entry" ]]; then
        echo -e "${RED}Error: log entry is required${NC}"
        return 1
    fi

    local timestamp=$(date +"%H:%M")
    local text="[$timestamp] $entry"

    bear_add_text --title "Daily Log" --text "$text" --mode "append"
}

# Show help
show_help() {
    cat << EOF
${GREEN}Bear App Automation Helper${NC}

Usage: source bear_helper.sh

Available functions:

  ${YELLOW}Note Creation:${NC}
    bear_create --title "Title" --text "Content" [--tags "tag1,tag2"] [--pin] [--open] [--edit]
    bear_add_text --title "Title" --text "Content" [--mode append|prepend|replace] [--tags "tags"]
    bear_capture_clipboard [tags]

  ${YELLOW}Note Access:${NC}
    bear_open --title "Title" [--header "Header"]
    bear_open --id "NOTE-ID"
    bear_search --term "search term" [--tag "tag"]

  ${YELLOW}Tag Management:${NC}
    bear_open_tag "tag-name"
    bear_rename_tag "old-name" "new-name"
    bear_delete_tag "tag-name"

  ${YELLOW}Special Collections:${NC}
    bear_untagged
    bear_today
    bear_todo
    bear_locked

  ${YELLOW}Web Content:${NC}
    bear_grab_url "https://example.com" ["tags"] ["yes"|"no" for pin]
    bear_get_tags "YOUR_TOKEN"

  ${YELLOW}Workflows:${NC}
    bear_daily_journal
    bear_log_entry "Entry text"
    bear_capture_clipboard [tags]

  ${YELLOW}Utilities:${NC}
    urlencode "text"
    build_bear_url "action" "params"

Examples:

  # Create a new note
  bear_create --title "Meeting Notes" --text "Discussed project timeline" --tags "work,meetings"

  # Append to existing note
  bear_add_text --title "Daily Log" --text "Completed task X" --mode append

  # Search notes
  bear_search --term "meeting" --tag "work"

  # Quick capture from clipboard
  bear_capture_clipboard "inbox"

  # Daily journal
  bear_daily_journal

EOF
}

# If script is executed (not sourced), show help
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    show_help
fi
