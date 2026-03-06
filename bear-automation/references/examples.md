# Bear App x-callback-url Examples

This document provides practical examples and use cases for Bear automation.

## Table of Contents

1. [Basic Operations](#basic-operations)
2. [Workflow Automation](#workflow-automation)
3. [Integration Examples](#integration-examples)
4. [Advanced Patterns](#advanced-patterns)
5. [Troubleshooting](#troubleshooting)

## Basic Operations

### Creating Notes

#### Simple Note
```bash
open "bear://x-callback-url/create?text=Hello%20World"
```

#### Note with Title and Tags
```bash
open "bear://x-callback-url/create?title=Meeting%20Notes&text=Discussed%20Q1%20goals&tags=work,meetings"
```

#### Markdown Note
```bash
TEXT="# Project Plan\n\n## Goals\n- Goal 1\n- Goal 2"
open "bear://x-callback-url/create?text=$(urlencode "$TEXT")&tags=projects"
```

#### Pinned Note with Editor Open
```bash
open "bear://x-callback-url/create?title=Important&text=Content&pin=yes&edit=yes&open_note=yes"
```

### Adding Content to Existing Notes

#### Append to Note
```bash
open "bear://x-callback-url/add-text?title=Daily%20Log&text=New%20entry&mode=append"
```

#### Prepend to Note
```bash
open "bear://x-callback-url/add-text?title=Todo%20List&text=Urgent%20task&mode=prepend"
```

#### Replace Note Content
```bash
open "bear://x-callback-url/add-text?id=ABC123&text=New%20content&mode=replace"
```

#### Add with Timestamp
```bash
ENTRY="Task completed"
open "bear://x-callback-url/add-text?title=Log&text=$ENTRY&timestamp=yes"
```

### Searching and Opening

#### Search by Term
```bash
open "bear://x-callback-url/search?term=meeting"
```

#### Search by Tag
```bash
open "bear://x-callback-url/search?tag=work"
```

#### Search with Both
```bash
open "bear://x-callback-url/search?term=project&tag=active"
```

#### Open Specific Note
```bash
open "bear://x-callback-url/open-note?title=Project%20Plan"
```

#### Open Note at Header
```bash
open "bear://x-callback-url/open-note?title=Documentation&header=Installation"
```

### Tag Management

#### Open Tag Collection
```bash
open "bear://x-callback-url/open-tag?name=work"
```

#### Rename Tag
```bash
open "bear://x-callback-url/rename-tag?name=old-project&new_name=archived"
```

#### Delete Tag
```bash
open "bear://x-callback-url/delete-tag?name=obsolete"
```

## Workflow Automation

### Daily Journal

```bash
#!/bin/bash
# Create daily journal entry

DATE=$(date +"%Y-%m-%d")
DAY=$(date +"%A")
TITLE="Journal - $DATE"

TEXT="# Daily Journal - $DAY\n\n"
TEXT+="## Morning\n\n"
TEXT+="## Afternoon\n\n"
TEXT+="## Evening\n\n"
TEXT+="## Reflections\n\n"

open "bear://x-callback-url/create?title=$(urlencode "$TITLE")&text=$(urlencode "$TEXT")&tags=journal&edit=yes&open_note=yes"
```

### Meeting Notes Template

```bash
#!/bin/bash
# Create meeting notes from template

MEETING_TITLE="$1"
ATTENDEES="$2"

if [[ -z "$MEETING_TITLE" ]]; then
    echo "Usage: $0 'Meeting Title' 'Attendees'"
    exit 1
fi

TEXT="# $MEETING_TITLE\n\n"
TEXT+="**Date:** $(date +"%Y-%m-%d")\n"
TEXT+="**Time:** $(date +"%H:%M")\n"
TEXT+="**Attendees:** $ATTENDEES\n\n"
TEXT+="## Agenda\n\n"
TEXT+="## Discussion\n\n"
TEXT+="## Action Items\n\n"
TEXT+="## Next Steps\n\n"

open "bear://x-callback-url/create?title=$(urlencode "$MEETING_TITLE")&text=$(urlencode "$TEXT")&tags=meetings,work&edit=yes&open_note=yes"
```

### Quick Capture

```bash
#!/bin/bash
# Quick capture from clipboard to Bear

CONTENT=$(pbpaste)
TIMESTAMP=$(date +"%Y-%m-%d %H:%M")

if [[ -z "$CONTENT" ]]; then
    echo "Clipboard is empty"
    exit 1
fi

TEXT="[$TIMESTAMP]\n\n$CONTENT"

open "bear://x-callback-url/create?text=$(urlencode "$TEXT")&tags=inbox,quick-capture"

echo "Captured to Bear"
```

### Weekly Review

```bash
#!/bin/bash
# Create weekly review note

WEEK=$(date +"%Y-W%V")
START=$(date -v-Mon +"%Y-%m-%d")
END=$(date -v+Sun +"%Y-%m-%d")

TITLE="Weekly Review - $WEEK"

TEXT="# Weekly Review\n\n"
TEXT+="**Week:** $START to $END\n\n"
TEXT+="## Accomplishments\n\n"
TEXT+="## Challenges\n\n"
TEXT+="## Learnings\n\n"
TEXT+="## Next Week Goals\n\n"

open "bear://x-callback-url/create?title=$(urlencode "$TITLE")&text=$(urlencode "$TEXT")&tags=reviews,weekly&edit=yes&open_note=yes"
```

### Project Tracker

```bash
#!/bin/bash
# Add project update to tracker

PROJECT_NAME="$1"
UPDATE="$2"

if [[ -z "$PROJECT_NAME" ]] || [[ -z "$UPDATE" ]]; then
    echo "Usage: $0 'Project Name' 'Update text'"
    exit 1
fi

TIMESTAMP=$(date +"%Y-%m-%d %H:%M")
ENTRY="### $TIMESTAMP\n\n$UPDATE\n\n"

open "bear://x-callback-url/add-text?title=$(urlencode "Project: $PROJECT_NAME")&text=$(urlencode "$ENTRY")&mode=append&tags=projects"
```

### Reading List

```bash
#!/bin/bash
# Add article to reading list

URL="$1"
TITLE="$2"
NOTES="$3"

if [[ -z "$URL" ]]; then
    echo "Usage: $0 'URL' ['Title'] ['Notes']"
    exit 1
fi

TEXT="- [$TITLE]($URL)\n"
[[ -n "$NOTES" ]] && TEXT+="  - $NOTES\n"

open "bear://x-callback-url/add-text?title=Reading%20List&text=$(urlencode "$TEXT")&mode=append&tags=reading"
```

## Integration Examples

### With Alfred Workflow

```bash
# Alfred Script Filter
query="{query}"

cat << EOF
{
  "items": [
    {
      "title": "Quick Note",
      "subtitle": "Create note: $query",
      "arg": "bear://x-callback-url/create?text=$(urlencode "$query")&tags=quick"
    },
    {
      "title": "Search Bear",
      "subtitle": "Search for: $query",
      "arg": "bear://x-callback-url/search?term=$(urlencode "$query")"
    }
  ]
}
EOF
```

### With Keyboard Maestro

```applescript
-- Keyboard Maestro AppleScript
set theText to the clipboard
set encodedText to do shell script "python3 -c 'import urllib.parse; print(urllib.parse.quote(\"" & theText & "\"))'"
set bearURL to "bear://x-callback-url/create?text=" & encodedText & "&tags=inbox"
open location bearURL
```

### With Shortcuts (iOS/macOS)

1. Get text from input
2. URL Encode text
3. Set variable `encodedText`
4. Open URL: `bear://x-callback-url/create?text=[encodedText]&tags=shortcuts`

### With Drafts

```javascript
// Drafts action script
const title = draft.title || "Untitled";
const content = draft.content;

const params = {
    title: title,
    text: content,
    tags: "drafts,imported"
};

const query = Object.keys(params)
    .map(key => `${key}=${encodeURIComponent(params[key])}`)
    .join('&');

const url = `bear://x-callback-url/create?${query}`;
app.openURL(url);
```

### With Python Script

```python
#!/usr/bin/env python3
import sys
import urllib.parse
import subprocess

def create_bear_note(title, content, tags=None):
    params = {
        'title': title,
        'text': content
    }
    if tags:
        params['tags'] = ','.join(tags)

    query = urllib.parse.urlencode(params)
    url = f"bear://x-callback-url/create?{query}"
    subprocess.run(['open', url])

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: script.py 'title' 'content' [tag1,tag2]")
        sys.exit(1)

    title = sys.argv[1]
    content = sys.argv[2]
    tags = sys.argv[3].split(',') if len(sys.argv) > 3 else None

    create_bear_note(title, content, tags)
```

## Advanced Patterns

### Batch Note Creation

```bash
#!/bin/bash
# Create multiple notes from CSV

CSV_FILE="$1"

while IFS=',' read -r title content tags; do
    open "bear://x-callback-url/create?title=$(urlencode "$title")&text=$(urlencode "$content")&tags=$(urlencode "$tags")"
    sleep 1  # Avoid overwhelming Bear
done < "$CSV_FILE"
```

### Note Template System

```bash
#!/bin/bash
# Template-based note creation

TEMPLATE_DIR="$HOME/.bear-templates"

load_template() {
    local template_name="$1"
    local template_file="$TEMPLATE_DIR/${template_name}.md"

    if [[ ! -f "$template_file" ]]; then
        echo "Template not found: $template_name"
        return 1
    fi

    cat "$template_file"
}

create_from_template() {
    local template_name="$1"
    local title="$2"
    shift 2
    local tags="$@"

    local content=$(load_template "$template_name")

    # Replace placeholders
    content="${content//\{\{DATE\}\}/$(date +"%Y-%m-%d")}"
    content="${content//\{\{TIME\}\}/$(date +"%H:%M")}"
    content="${content//\{\{TITLE\}\}/$title}"

    open "bear://x-callback-url/create?title=$(urlencode "$title")&text=$(urlencode "$content")&tags=$(urlencode "$tags")"
}

# Usage
create_from_template "meeting" "Team Sync" "meetings,work"
```

### Callback Handling

```bash
#!/bin/bash
# Create note with success callback

# Start local server to handle callback
python3 -m http.server 8080 &
SERVER_PID=$!

# Create note with callback
SUCCESS_URL="http://localhost:8080/success"
ERROR_URL="http://localhost:8080/error"

open "bear://x-callback-url/create?text=Test&x-success=$(urlencode "$SUCCESS_URL")&x-error=$(urlencode "$ERROR_URL")"

# Wait for callback
sleep 5

# Cleanup
kill $SERVER_PID
```

### Automated Tagging

```bash
#!/bin/bash
# Auto-tag notes based on content

NOTE_ID="$1"
CONTENT="$2"

TAGS=""

# Analyze content and add tags
[[ "$CONTENT" =~ "TODO" ]] && TAGS+=",todo"
[[ "$CONTENT" =~ "URGENT" ]] && TAGS+=",urgent"
[[ "$CONTENT" =~ "meeting" ]] && TAGS+=",meetings"
[[ "$CONTENT" =~ "project" ]] && TAGS+=",projects"

if [[ -n "$TAGS" ]]; then
    TAGS="${TAGS:1}"  # Remove leading comma
    open "bear://x-callback-url/add-text?id=$NOTE_ID&text=&tags=$TAGS"
fi
```

## Troubleshooting

### URL Encoding Issues

```bash
# Test URL encoding
test_encoding() {
    local text="$1"
    local encoded=$(urlencode "$text")
    echo "Original: $text"
    echo "Encoded: $encoded"
    echo "URL: bear://x-callback-url/create?text=$encoded"
}

test_encoding "Hello World! #test"
```

### Debugging URLs

```bash
# Print URL without opening
debug_bear_url() {
    local action="$1"
    shift
    local params="$@"
    local url="bear://x-callback-url/${action}?${params}"
    echo "URL: $url"
    echo ""
    echo "Decoded:"
    python3 -c "import urllib.parse; print(urllib.parse.unquote('$url'))"
}

debug_bear_url "create" "title=Test&text=Hello%20World"
```

### Checking Bear Installation

```bash
# Verify Bear is installed
check_bear() {
    if ! open -Ra "Bear"; then
        echo "Bear app is not installed"
        return 1
    fi
    echo "Bear is installed"
}

check_bear
```

### Rate Limiting

```bash
# Batch operations with rate limiting
batch_create() {
    local notes=("$@")
    local delay=1

    for note in "${notes[@]}"; do
        open "bear://x-callback-url/create?text=$(urlencode "$note")"
        sleep $delay
    done
}

batch_create "Note 1" "Note 2" "Note 3"
```

## Best Practices

1. **Always URL-encode**: Use proper encoding functions
2. **Use note IDs**: More reliable than titles for targeting
3. **Add delays**: Between batch operations (1-2 seconds)
4. **Handle errors**: Implement x-error callbacks
5. **Test incrementally**: Start with simple URLs, add complexity
6. **Document workflows**: Keep templates and scripts organized
7. **Version control**: Track automation scripts in git
8. **Backup notes**: Regular exports before bulk operations

## Resources

- [Bear Official Documentation](https://bear.app/faq/x-callback-url-scheme-documentation/)
- [x-callback-url Specification](http://x-callback-url.com/)
- Bear Community Forums
- Automation subreddits and communities
