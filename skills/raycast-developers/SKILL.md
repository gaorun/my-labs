---
name: raycast-developers
description: >
  Develop Raycast extensions using the official Raycast API. 
  Trigger whenever the user wants to create, modify, or publish a Raycast extension; 
  when they mention Raycast, Raycast extensions, Raycast API, or building commands/tools for Raycast;
  or when the user wants to integrate a service/API into Raycast as a plugin.
  If the user wants to make a Raycast extension, do NOT jump into writing code right away.
  Instead, use this skill's brainstorming process first.
---

# Raycast Extension Developer

You are helping a user develop a Raycast extension. Raycast extensions are built with TypeScript, React, and Node.js using `@raycast/api`.

## Your Process: Brainstorm First, Build Second

Raycast extensions can take many forms — commands, tools, menu bar apps, AI tools, etc. Before writing any code, you must understand exactly what the user needs.

### Step 1: Brainstorming Session

Ask targeted questions to clarify the extension. Do NOT ask all of these at once — ask them conversationally, one or two at a time, and let the user respond before proceeding. Adapt your questions based on their answers.

**Core questions to explore (ask selectively based on context):**

- **What problem should this extension solve?** What does the user want to accomplish? What's the trigger or use case?
- **Command type**: Does this need a [Command](/references/information-terminology.md) (appears in Raycast root search), a [Tool](/references/information-terminology.md) (used by AI via `@mention`), or both?
- **UI mode**: If it's a command — should it be a `view` (with a UI component like List/Detail/Form/Grid), `no-view` (background script), or `menu-bar`?
- **Data source**: Where does the data come from? An external API? Local files? Clipboard? User input via arguments or form?
- **Authentication**: Does the extension need to authenticate against a third-party service? OAuth? API key? Personal access token?
- **User interaction**: Should the user search/filter items, fill out a form, see detailed info, trigger actions, or all of the above?
- **Preferences**: Are there configurable options the user should set (API keys, defaults, etc.)?
- **Target platform**: macOS, Windows, or both?

### Step 2: Plan the Implementation

Once the requirements are clear, outline:

1. **Extension structure** — what commands/tools, their entry points, manifest fields
2. **Key API surfaces** needed — list, form, detail, clipboard, AI, cache, etc.
3. **Data flow** — how data is fetched, cached, displayed, and acted upon
4. **Preferences/arguments** — what configuration the extension needs

### Step 3: Implement

Build the extension following Raycast conventions:

- Set up with `npm init @raycast/extension` or manual setup
- Structure code in `src/` with one file per command/tool
- Use `@raycast/api` for all Raycast interactions
- Use `@raycast/utils` for common patterns (useFetch, useCachedPromise, useForm, etc.)
- Add proper error handling with `showToast` — network failures, empty states, permission issues
- Add loading states via `isLoading` prop on List/Detail/Grid/Form
- Use `Action` components in an `ActionPanel` for user actions (copy, paste, open, etc.)
- For API calls, prefer `useFetch` or `useCachedPromise` from `@raycast/utils`
- For forms, use `useForm` with `FormValidation` for validation
- For AI-powered features, use `AI.ask` from `@raycast/api`

## Reference Architecture

The typical extension structure:

```
my-extension/
├── package.json          # Manifest (name, title, commands, preferences, etc.)
├── src/
│   ├── index.tsx         # Default command entry point
│   ├── my-command.tsx    # Additional command
│   └── tools/            # AI Tools directory
│       └── my-tool.ts    # AI tool entry point
├── assets/
│   └── icon.png          # 512x512px icon (optionally icon@dark.png)
├── ai.yaml               # AI extension instructions (optional)
└── tsconfig.json
```

## Key API Reference Files

Reference files are in `references/` directory. Load them as needed during implementation:

### Core API
- `api-reference-environment.md` — Runtime environment, canAccess, LaunchType
- `api-reference-feedback.md` — Toast, HUD, showHUD, showToast
- `api-reference-clipboard.md` — Clipboard.copy, Clipboard.paste, Clipboard.read
- `api-reference-cache.md` — Cache with LRU eviction, 10MB default capacity
- `api-reference-command.md` — launchCommand, updateCommandMetadata
- `api-reference-keyboard.md` — Keyboard shortcuts, Hotkey, Key.Modifier
- `api-reference-preferences.md` — Access extension/command preferences
- `api-reference-oauth.md` — OAuth flow for third-party services
- `api-reference-menu-bar-commands.md` — Menu bar extras
- `api-reference-browser-extensions.md` — Browser extension integration
- `api-reference-window-management.md` — Window management API
- `api-reference-ai.md` — AI.ask for AI-powered features

### User Interface
- `user-interface-list.md` — List component with search, filtering, sections
- `user-interface-detail.md` — Detail/Markdown view for item details
- `user-interface-form.md` — Forms with validation, dropdowns, text fields, etc.
- `user-interface-grid.md` — Grid layout for visual content
- `user-interface-actions.md` — ActionPanel, Action.SubmitForm, Action.CopyToClipboard, etc.
- `user-interface-navigation.md` — push, pop navigation
- `user-interface-colors.md` — Color, ColorLike
- `user-interface-icons-and-images.md` — Icon, Image, FileIcon, etc.

### Utilities (`@raycast/utils`)
- `react-hooks-usefetch.md` — Fetch data with caching, pagination, and revalidation
- `react-hooks-usecachedpromise.md` — Promise with disk cache
- `react-hooks-useform.md` — Form validation and handling
- `react-hooks-useai.md` — React hook for AI.ask
- `react-hooks-useexec.md` — Execute shell commands
- `react-hooks-usesql.md` — Query SQLite databases
- `react-hooks-uselocalstorage.md` — LocalStorage hook
- `react-hooks-usefrecencysorting.md` — Sort items by frecency
- `react-hooks-usestreamjson.md` — Stream and parse JSON

### Functions
- `functions-runapplescript.md` — Execute AppleScript
- `functions-showfailuretoast.md` — Standardized error toast
- `functions-withcache.md` — Wrap async functions with cache
- `functions-createdeeplink.md` — Create deeplinks to commands

### Information
- `information-manifest.md` — Full manifest/package.json reference
- `information-lifecycle.md` — Command lifecycle (launch, unload, LaunchProps)
- `information-lifecycle-arguments.md` — Command arguments
- `information-lifecycle-background-refresh.md` — Background refresh for no-view/menu-bar commands
- `information-lifecycle-deeplinks.md` — Deeplink lifecycle
- `information-terminology.md` — Key terms (Command, Tool, Extension, Action, etc.)
- `information-security.md` — Security best practices
- `information-versioning.md` — Version compatibility
- `information-developer-tools-cli.md` — CLI commands (dev, build, publish, lint)
- `information-developer-tools-templates.md` — Extension templates
- `information-best-practices.md` — Error handling, loading states, form validation

### Basics / Getting Started
- `basics-getting-started.md` — System requirements, sign in
- `basics-create-your-first-extension.md` — Create, build, develop
- `basics-prepare-an-extension-for-store.md` — Store preparation checklist
- `basics-publish-an-extension.md` — Publish flow

## Implementation Conventions

Follow these conventions when writing Raycast extensions:

1. **Exports**: Export a default function for each command. For view commands, return a React component. For no-view commands, export an async function.
2. **Error handling**: Always handle errors with `showToast`. Show loading states. Never let the user see unhandled errors.
3. **Actions**: Always wrap actionable items in `<ActionPanel>` with relevant actions (Copy, Paste, Open, etc.).
4. **Performance**: Use `useCachedPromise` or `useFetch` for API calls with caching. Show `isLoading` while data loads.
5. **Publishing**: Run `npm run build` to validate, then `npm run publish` to publish to the Raycast Store.

## Helpful `@raycast/api` Import Patterns

```typescript
// Most common imports
import {
  Action, ActionPanel, List, Detail, Form, Grid, Icon, Color,
  showToast, Toast, showHUD,
  Clipboard, Cache, environment, AI, LaunchType,
  getPreferenceValues, open, popToRoot,
  useNavigation, confirmAlert, Alert,
  updateCommandMetadata, launchCommand,
} from "@raycast/api";

// Common utils imports
import {
  useFetch, useCachedPromise, useForm, useAI, FormValidation,
  showFailureToast, runAppleScript,
} from "@raycast/utils";
```

## Reference Loading Strategy

Do NOT load all reference files at once. Load them on demand:

- When designing the manifest → load `information-manifest.md`
- When building a list → load `user-interface-list.md`
- When building a form → load `user-interface-form.md` and `react-hooks-useform.md`
- When making API calls → load `react-hooks-usefetch.md` and `react-hooks-usecachedpromise.md`
- When adding AI features → load `api-reference-ai.md`
- When handling auth → load `api-reference-oauth.md` and `oauth.md`
