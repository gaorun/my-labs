#!/usr/bin/env python3
"""
Bear App x-callback-url Helper Script

This script provides utilities for interacting with Bear app via x-callback-url.
"""

import urllib.parse
import subprocess
import sys
import json
from typing import Dict, Optional, List


class BearAutomation:
    """Helper class for Bear app automation"""

    BASE_URL = "bear://x-callback-url"

    @staticmethod
    def _encode_params(params: Dict) -> str:
        """URL encode parameters"""
        return urllib.parse.urlencode(params)

    @staticmethod
    def _open_url(url: str) -> None:
        """Open URL using system default handler"""
        try:
            subprocess.run(["open", url], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error opening URL: {e}", file=sys.stderr)
            sys.exit(1)

    @classmethod
    def _build_url(cls, action: str, params: Dict) -> str:
        """Build complete Bear x-callback-url"""
        query = cls._encode_params(params)
        return f"{cls.BASE_URL}/{action}?{query}"

    @classmethod
    def create_note(cls,
                   title: Optional[str] = None,
                   text: str = "",
                   clipboard: bool = False,
                   tags: Optional[List[str]] = None,
                   file_base64: Optional[str] = None,
                   filename: Optional[str] = None,
                   pin: bool = False,
                   open_note: bool = False,
                   new_window: bool = False,
                   float_window: bool = False,
                   edit: bool = False,
                   timestamp: bool = False,
                   html_type: bool = False,
                   base_url: Optional[str] = None) -> str:
        """
        Create a new note in Bear

        Args:
            title: Note title
            text: Note content (Markdown supported)
            clipboard: Use clipboard content
            tags: List of tags
            file_base64: Base64 encoded file content
            filename: File name with extension (required with file_base64)
            pin: Pin the note
            open_note: Open note after creation
            new_window: Open in new window (Mac)
            float_window: Float window on top (Mac)
            edit: Place cursor in editor
            timestamp: Add timestamp
            html_type: Convert HTML to Markdown
            base_url: Base URL for resolving relative links (with html_type)

        Returns:
            The Bear URL
        """
        params = {}

        if text:
            params["text"] = text
        if title:
            params["title"] = title
        if clipboard:
            params["clipboard"] = "yes"
        if tags:
            params["tags"] = ",".join(tags)
        if file_base64:
            params["file"] = file_base64
        if filename:
            params["filename"] = filename
        if pin:
            params["pin"] = "yes"
        if open_note:
            params["open_note"] = "yes"
        if new_window:
            params["new_window"] = "yes"
        if float_window:
            params["float"] = "yes"
        if edit:
            params["edit"] = "yes"
        if timestamp:
            params["timestamp"] = "yes"
        if html_type:
            params["type"] = "html"
        if base_url:
            params["url"] = base_url

        url = cls._build_url("create", params)
        cls._open_url(url)
        return url

    @classmethod
    def add_text(cls,
                title: Optional[str] = None,
                note_id: Optional[str] = None,
                text: str = "",
                mode: str = "append",
                tags: Optional[List[str]] = None,
                open_note: bool = False,
                new_line: bool = True,
                timestamp: bool = False) -> str:
        """
        Add text to existing note (or create new one)

        Args:
            title: Note title to search for
            note_id: Note unique identifier
            text: Text to add
            mode: Where to add text (append, prepend, replace, replace_all)
            tags: Tags for the note
            open_note: Open note after adding
            new_line: Add new line before/after text
            timestamp: Add timestamp

        Returns:
            The Bear URL
        """
        params = {"text": text, "mode": mode}

        if title:
            params["title"] = title
        if note_id:
            params["id"] = note_id
        if tags:
            params["tags"] = ",".join(tags)
        if open_note:
            params["open_note"] = "yes"
        if not new_line:
            params["new_line"] = "no"
        if timestamp:
            params["timestamp"] = "yes"

        url = cls._build_url("add-text", params)
        cls._open_url(url)
        return url

    @classmethod
    def add_file(cls,
                file_path: str,
                title: Optional[str] = None,
                note_id: Optional[str] = None,
                filename: Optional[str] = None,
                mode: str = "append",
                open_note: bool = False) -> str:
        """
        Add file to note

        Args:
            file_path: Path to file
            title: Note title
            note_id: Note unique identifier
            filename: Custom filename
            mode: Where to add file (append, prepend, replace)
            open_note: Open note after adding

        Returns:
            The Bear URL
        """
        params = {"file": file_path, "mode": mode}

        if title:
            params["title"] = title
        if note_id:
            params["id"] = note_id
        if filename:
            params["filename"] = filename
        if open_note:
            params["open_note"] = "yes"

        url = cls._build_url("add-file", params)
        cls._open_url(url)
        return url

    @classmethod
    def open_note(cls,
                 title: Optional[str] = None,
                 note_id: Optional[str] = None,
                 header: Optional[str] = None,
                 edit: bool = False,
                 new_window: bool = False) -> str:
        """
        Open a specific note

        Args:
            title: Note title
            note_id: Note unique identifier
            header: Scroll to specific header
            edit: Place cursor in editor
            new_window: Open in new window (Mac)

        Returns:
            The Bear URL
        """
        params = {}

        if title:
            params["title"] = title
        if note_id:
            params["id"] = note_id
        if header:
            params["header"] = header
        if edit:
            params["edit"] = "yes"
        if new_window:
            params["new_window"] = "yes"

        url = cls._build_url("open-note", params)
        cls._open_url(url)
        return url

    @classmethod
    def search(cls, term: Optional[str] = None, tag: Optional[str] = None) -> str:
        """
        Search notes

        Args:
            term: Search term
            tag: Filter by tag

        Returns:
            The Bear URL
        """
        params = {}

        if term:
            params["term"] = term
        if tag:
            params["tag"] = tag

        url = cls._build_url("search", params)
        cls._open_url(url)
        return url

    @classmethod
    def open_tag(cls, tag_name: str) -> str:
        """
        Open a tag collection

        Args:
            tag_name: Tag name

        Returns:
            The Bear URL
        """
        params = {"name": tag_name}
        url = cls._build_url("open-tag", params)
        cls._open_url(url)
        return url

    @classmethod
    def rename_tag(cls, old_name: str, new_name: str) -> str:
        """
        Rename a tag

        Args:
            old_name: Current tag name
            new_name: New tag name

        Returns:
            The Bear URL
        """
        params = {"name": old_name, "new_name": new_name}
        url = cls._build_url("rename-tag", params)
        cls._open_url(url)
        return url

    @classmethod
    def delete_tag(cls, tag_name: str) -> str:
        """
        Delete a tag

        Args:
            tag_name: Tag name to delete

        Returns:
            The Bear URL
        """
        params = {"name": tag_name}
        url = cls._build_url("delete-tag", params)
        cls._open_url(url)
        return url

    @classmethod
    def trash_note(cls, note_id: str) -> str:
        """
        Move note to trash

        Args:
            note_id: Note unique identifier

        Returns:
            The Bear URL
        """
        params = {"id": note_id}
        url = cls._build_url("trash", params)
        cls._open_url(url)
        return url

    @classmethod
    def archive_note(cls, note_id: str) -> str:
        """
        Archive a note

        Args:
            note_id: Note unique identifier

        Returns:
            The Bear URL
        """
        params = {"id": note_id}
        url = cls._build_url("archive", params)
        cls._open_url(url)
        return url

    @classmethod
    def show_untagged(cls) -> str:
        """Show all untagged notes"""
        url = f"{cls.BASE_URL}/untagged"
        cls._open_url(url)
        return url

    @classmethod
    def show_today(cls) -> str:
        """Show notes modified today"""
        url = f"{cls.BASE_URL}/today"
        cls._open_url(url)
        return url

    @classmethod
    def show_todo(cls) -> str:
        """Show notes with uncompleted todos"""
        url = f"{cls.BASE_URL}/todo"
        cls._open_url(url)
        return url

    @classmethod
    def show_locked(cls) -> str:
        """Show locked notes"""
        url = f"{cls.BASE_URL}/locked"
        cls._open_url(url)
        return url

    @classmethod
    def grab_url(cls,
                url: str,
                tags: Optional[List[str]] = None,
                pin: bool = False,
                wait: bool = True) -> str:
        """
        Create a new note with content from a web page

        Args:
            url: URL to grab
            tags: List of tags (ignored if set in Bear's preferences)
            pin: Pin the note
            wait: Wait for completion before calling x-success

        Returns:
            The Bear URL
        """
        params = {"url": url}

        if tags:
            params["tags"] = ",".join(tags)
        if pin:
            params["pin"] = "yes"
        if not wait:
            params["wait"] = "no"

        url = cls._build_url("grab-url", params)
        cls._open_url(url)
        return url

    @classmethod
    def get_tags(cls, token: str) -> str:
        """
        Get all tags as JSON array

        Args:
            token: Application token (generate in Bear → Help → API Token)

        Returns:
            The Bear URL
        """
        params = {"token": token}
        url = cls._build_url("tags", params)
        cls._open_url(url)
        return url


def main():
    """CLI interface for Bear automation"""
    import argparse

    parser = argparse.ArgumentParser(description="Bear App Automation Helper")
    subparsers = parser.add_subparsers(dest="command", help="Command to execute")

    # Create note
    create_parser = subparsers.add_parser("create", help="Create a new note")
    create_parser.add_argument("--title", help="Note title")
    create_parser.add_argument("--text", required=True, help="Note content")
    create_parser.add_argument("--tags", help="Comma-separated tags")
    create_parser.add_argument("--pin", action="store_true", help="Pin the note")
    create_parser.add_argument("--open", action="store_true", help="Open note after creation")
    create_parser.add_argument("--edit", action="store_true", help="Place cursor in editor")

    # Add text
    add_parser = subparsers.add_parser("add-text", help="Add text to existing note")
    add_parser.add_argument("--title", help="Note title")
    add_parser.add_argument("--id", help="Note ID")
    add_parser.add_argument("--text", required=True, help="Text to add")
    add_parser.add_argument("--mode", default="append", choices=["append", "prepend", "replace"], help="Where to add text")
    add_parser.add_argument("--tags", help="Comma-separated tags")

    # Search
    search_parser = subparsers.add_parser("search", help="Search notes")
    search_parser.add_argument("--term", help="Search term")
    search_parser.add_argument("--tag", help="Filter by tag")

    # Open note
    open_parser = subparsers.add_parser("open", help="Open a note")
    open_parser.add_argument("--title", help="Note title")
    open_parser.add_argument("--id", help="Note ID")
    open_parser.add_argument("--header", help="Scroll to header")

    # Open tag
    tag_parser = subparsers.add_parser("open-tag", help="Open a tag collection")
    tag_parser.add_argument("tag", help="Tag name")

    args = parser.parse_args()

    if args.command == "create":
        tags = args.tags.split(",") if args.tags else None
        BearAutomation.create_note(
            title=args.title,
            text=args.text,
            tags=tags,
            pin=args.pin,
            open_note=args.open,
            edit=args.edit
        )
    elif args.command == "add-text":
        tags = args.tags.split(",") if args.tags else None
        BearAutomation.add_text(
            title=args.title,
            note_id=args.id,
            text=args.text,
            mode=args.mode,
            tags=tags
        )
    elif args.command == "search":
        BearAutomation.search(term=args.term, tag=args.tag)
    elif args.command == "open":
        BearAutomation.open_note(title=args.title, note_id=args.id, header=args.header)
    elif args.command == "open-tag":
        BearAutomation.open_tag(args.tag)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
