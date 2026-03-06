---
name: bear-automation
description: Automate Bear note-taking app using x-callback-url scheme. Use this skill when the user wants to create, edit, search, open, or manage Bear notes, tags, or archives. Trigger when user mentions Bear app, Bear notes, x-callback-url for Bear, or wants to automate note-taking workflows. Also use when user needs to generate Bear URL schemes or integrate Bear with other automation tools.
---

# Bear Automation Skill

This skill helps you automate the Bear note-taking app using its x-callback-url scheme. Bear implements the x-callback-url protocol, allowing you to programmatically create, edit, search, and manage notes.

## When to Use This Skill

Use this skill when the user wants to:
- Create new notes or append content to existing notes in Bear
- Search for notes by title, content, or tags
- Open specific notes or tag collections
- Manage tags, archive, or trash notes
- Generate executable URL schemes or shell commands for Bear automation
- Integrate Bear with other apps or automation workflows (Shortcuts, Drafts, scripts)

## Base URL Format

All Bear x-callback-url actions follow this format:

```
bear://x-callback-url/[action]?[parameters]&x-success=[callback]&x-error=[callback]
```

## Core Actions

### 1. Create New Note

**Action**: `create`

Creates a new note with specified content, title, and tags.

**Parameters**:
- `title` (optional): Note title
- `text` (optional): Note content (Markdown supported)
- `clipboard` (optional): Use clipboard content (`yes` or `no`)
- `tags` (optional): Comma-separated tags (e.g., `work,project`)
- `file` (optional): Base64 encoded file content
- `filename` (optional): File name with extension (required with `file`)
- `pin` (optional): Pin note (`yes` or `no`)
- `open_note` (optional): Open note after creation (`yes` or `no`)
- `new_window` (optional): Open in new window on Mac (`yes` or `no`)
- `float` (optional): Float window on top on Mac (`yes` or `no`)
- `show_window` (optional): Show Bear window (`yes` or `no`, default `yes`)
- `edit` (optional): Place cursor in editor (`yes` or `no`)
- `timestamp` (optional): Add timestamp (`yes` or `no`)
- `type` (optional): If `html`, convert HTML to Markdown
- `url` (optional): Base URL for resolving relative image links (with `type=html`)

**Example**:
```
bear://x-callback-url/create?title=Meeting%20Notes&text=Discussed%20project%20timeline&tags=work,meetings&pin=yes
```

**Shell command**:
```bash
open "bear://x-callback-url/create?title=Meeting%20Notes&text=Discussed%20project%20timeline&tags=work,meetings"
```

### 2. Add Text to Existing Note

**Action**: `add-text`

Appends or prepends text to an existing note (creates new note if not found).

**Parameters**:
- `title` (optional): Note title to search for
- `id` (optional): Note unique identifier
- `selected` (optional): Use currently selected note (`yes`, requires token)
- `text` (optional): Text to add
- `clipboard` (optional): Use clipboard content (`yes` or `no`)
- `header` (optional): Add text under specific header in note
- `tags` (optional): Tags for the note
- `mode` (optional): Where to add text
  - `append` (default): Add to end
  - `prepend`: Add to beginning
  - `replace`: Replace entire content (keeps title)
  - `replace_all`: Replace all occurrences of a string
- `open_note` (optional): Open note after adding (`yes` or `no`)
- `new_window` (optional): Open in new window on Mac (`yes` or `no`)
- `new_line` (optional): Add new line before/after text (`yes` or `no`, default `yes`)
- `exclude_trashed` (optional): Exclude trashed notes (`yes` or `no`, default `yes`)
- `show_window` (optional): Show Bear window (`yes` or `no`)
- `edit` (optional): Place cursor in editor (`yes` or `no`)
- `timestamp` (optional): Add timestamp (`yes` or `no`)

**Example**:
```
bear://x-callback-url/add-text?title=Daily%20Log&text=Completed%20task%20X&mode=append
```

### 3. Add File to Note

**Action**: `add-file`

Adds a file to a note (creates new note if not found).

**Parameters**:
- `title` (optional): Note title
- `id` (optional): Note unique identifier
- `selected` (optional): Use currently selected note (`yes`, requires token)
- `file` (required): Base64 encoded file content
- `filename` (required): File name with extension
- `header` (optional): Add file under specific header in note
- `mode` (optional): `append`, `prepend`, `replace`, `replace_all`
- `open_note` (optional): Open note after adding
- `new_window` (optional): Open in new window on Mac (`yes` or `no`)
- `show_window` (optional): Show Bear window (`yes` or `no`)
- `edit` (optional): Place cursor in editor (`yes` or `no`)

**Example**:
```
bear://x-callback-url/add-file?title=Resources&file=/path/to/document.pdf
```

### 4. Open Note

**Action**: `open-note`

Opens a specific note by title, ID, or search query.

**Parameters**:
- `title` (optional): Note title
- `id` (optional): Note unique identifier
- `header` (optional): Scroll to specific header
- `exclude_trashed` (optional): Exclude trashed notes
- `new_window` (optional): Open in new window (Mac)
- `float` (optional): Float window (Mac)
- `show_window` (optional): Show Bear window
- `open_note` (optional): Open note in edit mode
- `selected` (optional): Select specific text
- `edit` (optional): Place cursor in editor

**Example**:
```
bear://x-callback-url/open-note?title=Project%20Plan&header=Timeline
```

### 5. Search Notes

**Action**: `search`

Searches notes and displays results.

**Parameters**:
- `term` (optional): Search term
- `tag` (optional): Filter by tag
- `show_window` (optional): Show Bear window

**Example**:
```
bear://x-callback-url/search?term=meeting&tag=work
```

### 6. Open Tag

**Action**: `open-tag`

Opens a tag collection.

**Parameters**:
- `name` (required): Tag name
- `show_window` (optional): Show Bear window

**Example**:
```
bear://x-callback-url/open-tag?name=work
```

### 7. Rename Tag

**Action**: `rename-tag`

Renames a tag across all notes.

**Parameters**:
- `name` (required): Current tag name
- `new_name` (required): New tag name
- `show_window` (optional): Show Bear window

**Example**:
```
bear://x-callback-url/rename-tag?name=old-project&new_name=archived-project
```

### 8. Delete Tag

**Action**: `delete-tag`

Deletes a tag from all notes.

**Parameters**:
- `name` (required): Tag name to delete
- `show_window` (optional): Show Bear window

**Example**:
```
bear://x-callback-url/delete-tag?name=obsolete
```

### 9. Trash Note

**Action**: `trash`

Moves a note to trash.

**Parameters**:
- `id` (required): Note unique identifier
- `show_window` (optional): Show Bear window

**Example**:
```
bear://x-callback-url/trash?id=ABC123-DEF456
```

### 10. Archive Note

**Action**: `archive`

Archives a note.

**Parameters**:
- `id` (required): Note unique identifier
- `show_window` (optional): Show Bear window

**Example**:
```
bear://x-callback-url/archive?id=ABC123-DEF456
```

### 11. Untagged Notes

**Action**: `untagged`

Shows all untagged notes.

**Parameters**:
- `show_window` (optional): Show Bear window

**Example**:
```
bear://x-callback-url/untagged
```

### 12. Today Notes

**Action**: `today`

Shows notes modified today.

**Parameters**:
- `show_window` (optional): Show Bear window

**Example**:
```
bear://x-callback-url/today
```

### 13. Todo Notes

**Action**: `todo`

Shows notes with uncompleted todos.

**Parameters**:
- `show_window` (optional): Show Bear window

**Example**:
```
bear://x-callback-url/todo
```

### 14. Locked Notes

**Action**: `locked`

Shows locked notes.

**Parameters**:
- `show_window` (optional): Show Bear window

**Example**:
```
bear://x-callback-url/locked
```

### 15. Grab URL

**Action**: `grab-url`

Creates a new note with the content of a web page.

**Parameters**:
- `url` (required): URL to grab
- `tags` (optional): Comma-separated tags (ignored if tags are set in Bear's web content preferences)
- `pin` (optional): Pin note (`yes` or `no`)
- `wait` (optional): If `no`, x-success is called immediately without identifier and title

**Example**:
```
bear://x-callback-url/grab-url?url=https://example.com&tags=web,articles
```

**Shell command**:
```bash
open "bear://x-callback-url/grab-url?url=https://example.com&tags=web,articles&pin=yes"
```

### 16. Get Tags

**Action**: `tags`

Returns all tags in Bear as a JSON array.

**Parameters**:
- `token` (required): Application token (see Token Generation section)

**Returns**:
- JSON array of tag objects with name and count

**Example**:
```
bear://x-callback-url/tags?token=YOUR_TOKEN
```

**Shell command**:
```bash
open "bear://x-callback-url/tags?token=YOUR_TOKEN"
```

## Token Generation

Some Bear API calls require an application token for enhanced functionality. Tokens enable:
- Getting the currently selected note
- Retrieving all tags
- Getting detailed search results
- Accessing additional note metadata

**Important**: Tokens are platform-specific. A token generated on iOS will not work on macOS and vice versa.

### How to Generate a Token

1. Open Bear app
2. Go to **Help** → **API Token** (or **Bear** → **Help** → **API Token** on Mac)
3. Click **Generate Token**
4. Copy the token and use it in your API calls

### Using Tokens

Add the `token` parameter to API calls that support it:

```bash
# Get all tags
open "bear://x-callback-url/tags?token=YOUR_TOKEN"

# Use currently selected note
open "bear://x-callback-url/add-text?selected=yes&text=New%20content&token=YOUR_TOKEN"

# Get detailed search results
open "bear://x-callback-url/search?term=project&token=YOUR_TOKEN"
```

**Security Note**: Keep your token private. Anyone with your token can access your Bear notes through the API.

## Callback Parameters

Bear supports x-callback-url callbacks for success and error handling:

- `x-success`: URL to call on success
- `x-error`: URL to call on error
- `x-cancel`: URL to call if user cancels

**Example with callbacks**:
```
bear://x-callback-url/create?title=Test&text=Content&x-success=myapp://success&x-error=myapp://error
```

## Return Values

Some actions return data via the success callback:

### create / add-text / add-file
- `title`: Note title
- `identifier`: Note unique ID
- `tags`: Comma-separated tags

### search
- `notes`: JSON array of matching notes
- `tags`: JSON array of matching tags

### open-note
- `note`: Note content
- `identifier`: Note unique ID
- `title`: Note title

## URL Encoding

Always URL-encode parameters, especially:
- Spaces: `%20`
- Newlines: `%0A`
- Special characters: `#` → `%23`, `&` → `%26`, `=` → `%3D`

## Helper Functions

When generating Bear automation, provide these utilities:

### Shell Script Template

```bash
#!/bin/bash

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

# Example: Create note
TITLE=$(urlencode "My Note Title")
TEXT=$(urlencode "Note content here")
TAGS=$(urlencode "tag1,tag2")

open "bear://x-callback-url/create?title=${TITLE}&text=${TEXT}&tags=${TAGS}"
```

### Python Script Template

```python
#!/usr/bin/env python3
import urllib.parse
import subprocess

def open_bear_url(action, params):
    """Open Bear with x-callback-url"""
    base_url = f"bear://x-callback-url/{action}"
    query = urllib.parse.urlencode(params)
    url = f"{base_url}?{query}"
    subprocess.run(["open", url])

# Example: Create note
open_bear_url("create", {
    "title": "My Note",
    "text": "Content here",
    "tags": "work,project"
})
```

### JavaScript/Node.js Template

```javascript
const { exec } = require('child_process');

function openBearURL(action, params) {
    const baseURL = `bear://x-callback-url/${action}`;
    const query = new URLSearchParams(params).toString();
    const url = `${baseURL}?${query}`;
    exec(`open "${url}"`);
}

// Example: Create note
openBearURL('create', {
    title: 'My Note',
    text: 'Content here',
    tags: 'work,project'
});
```

## Common Workflows

### Daily Journal Entry

```bash
DATE=$(date +"%Y-%m-%d")
TITLE="Journal - $DATE"
TEXT="# Daily Journal\n\n## What I did today:\n\n"

open "bear://x-callback-url/create?title=$(urlencode "$TITLE")&text=$(urlencode "$TEXT")&tags=journal&edit=yes"
```

### Append to Running Log

```bash
ENTRY="[$(date +"%H:%M")] Task completed"
open "bear://x-callback-url/add-text?title=Daily%20Log&text=$(urlencode "$ENTRY")&mode=append"
```

### Quick Capture with Tag

```bash
# Capture clipboard content to Bear
CONTENT=$(pbpaste)
open "bear://x-callback-url/create?text=$(urlencode "$CONTENT")&tags=inbox"
```

### Search and Open

```bash
# Search for notes with specific term
open "bear://x-callback-url/search?term=meeting&tag=work"
```

## Best Practices

1. **Always URL-encode parameters**: Use proper encoding functions to avoid malformed URLs
2. **Use note IDs when possible**: IDs are more reliable than titles for targeting specific notes
3. **Handle callbacks gracefully**: Implement x-success and x-error handlers for robust automation
4. **Test with show_window=yes**: During development, keep Bear window visible to debug
5. **Batch operations carefully**: Bear processes one URL at a time; add delays between bulk operations
6. **Use tags consistently**: Establish a tagging convention for easier automation
7. **Leverage mode parameter**: Use `append`, `prepend`, or `replace` strategically for different workflows

## Troubleshooting

- **URL not working**: Check URL encoding, especially for special characters
- **Note not found**: Verify title matches exactly (case-sensitive) or use note ID
- **Bear doesn't open**: Ensure Bear app is installed and URL scheme is registered
- **Callback not firing**: Verify callback URL format and that receiving app is installed
- **Content not appearing**: Check for newline encoding (`%0A`) and `new_line` parameter

## Platform Considerations

### macOS
- Use `open` command to trigger URLs
- Supports `new_window` and `float` parameters
- Can integrate with Automator, AppleScript, and shell scripts

### iOS
- Use `UIApplication.shared.open()` in Swift
- Integrate with Shortcuts app for visual automation
- Can trigger from other apps via share extensions

## Integration Examples

### With Shortcuts (iOS/macOS)

Create a Shortcut that:
1. Gets text input
2. Formats as Markdown
3. Opens Bear URL with formatted text

### With Drafts

Use Drafts action to send current draft to Bear:
```javascript
const title = draft.title;
const content = draft.content;
const url = `bear://x-callback-url/create?title=${encodeURIComponent(title)}&text=${encodeURIComponent(content)}`;
app.openURL(url);
```

### With Alfred Workflow

Create Alfred workflow to quick-capture to Bear:
```bash
query="{query}"
open "bear://x-callback-url/create?text=$(urlencode "$query")&tags=quick-capture"
```

## Output Format

When helping users with Bear automation:

1. **Explain the action**: Describe what the URL will do
2. **Provide the URL**: Show the complete bear:// URL
3. **Show executable command**: Provide shell/script command to run it
4. **Include error handling**: Add x-error callbacks when appropriate
5. **Suggest workflow improvements**: Recommend tags, templates, or automation patterns

Always test the generated URLs and provide working examples that users can immediately execute.
