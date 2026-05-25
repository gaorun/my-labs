# Window Management

The Window Management API provides developers with some functions to create commands with some advanced logic to move [Window](#windowmanagement.window)s around.

{% hint style="info" %}
Some users might not have access to this API. If a user doesn't have access to Raycast Pro, they will be asked if they want to get access when your extension calls the Window Management API. If the user doesn't wish to get access, the API call will throw an error.

You can check if a user has access to the API using [`environment.canAccess(WindowManagement)`](/api-reference/environment.md).

The API is not accessible on Windows for now.
{% endhint %}

## API Reference

### WindowManagement.getActiveWindow

Gets the active [Window](#windowmanagement.window).

#### Signature

```typescript
async function getActiveWindow(): Promise<Window>;
```

#### Example

```typescript
import { WindowManagement, showToast } from "@raycast/api";

export default async function Command() {
  try {
    const window = await WindowManagement.getActiveWindow();
    if (window.positionable) {
      await WindowManagement.setWindowBounds({ id: window.id, bounds: { position: { x: 100 } } });
    }
  } catch (error) {
    showToast({ title: `Could not move window: ${error.message}`, style: Toast.Style.Failure });
  }
}
```

#### Return

A Promise that resolves with the active [Window](#windowmanagement.window). If no window is active, the promise will be rejected.

### WindowManagement.getWindowsOnActiveDesktop

Gets the list of [Window](#windowmanagement.window)s on the active [Desktop](#windowmanagement.desktop).

#### Signature

```typescript
async function getWindowsOnActiveDesktop(): Promise<Window[]>;
```

#### Example

```typescript
import { WindowManagement, showToast } from "@raycast/api";

export default async function Command() {
  const windows = await WindowManagement.getWindowsOnActiveDesktop();
  const chrome = windows.find((x) => x.application?.bundleId === "com.google.Chrome");
  if (!chrome) {
    showToast({ title: "Couldn't find chrome", style: Toast.Style.Failure });
    return;
  }
  WindowManagement.setWindowBounds({ id: chrome.id, bounds: { position: { x: 100 } } });
}
```

#### Return

A Promise that resolves with an array of Windows.

### WindowManagement.getDesktops

Gets the list of [Desktop](#windowmanagement.desktop)s available across all screens.

#### Signature

```typescript
async function getDesktops(): Promise<Desktop[]>;
```

#### Example

```typescript
import { WindowManagement, showToast } from "@raycast/api";

export default function Command() {
  const desktops = await WindowManagement.getDesktops();
  const screens = Set(desktops.map((desktop) => desktop.screenId));
  showToast({ title: `Found ${desktops.length} desktops on ${screens.size} screens.` });
}
```

#### Return

A Promise that resolves with the desktops.

### WindowManagement.setWindowBounds

Move a [Window](#windowmanagement.window) or make it fullscreen.

#### Signature

```typescript
async function setWindowBounds(
  options: { id: string } & (
    | {
        bounds: {
          position?: { x?: number; y?: number };
          size?: { width?: number; height?: number };
        };
        desktopId?: string;
      }
    | {
        bounds: "fullscreen";
      }
  )
): Promise<void>;
```

#### Example

```typescript
import { WindowManagement, showToast } from "@raycast/api";

export default async function Command() {
  try {
    const window = await WindowManagement.getActiveWindow();
    if (window.positionable) {
      await WindowManagement.setWindowBounds({ id: window.id, bounds: { position: { x: 100 } } });
    }
  } catch (error) {
    showToast({ title: `Could not move window: ${error.message}`, style: Toast.Style.Failure });
  }
}
```

#### Parameters

| Name                                      | Description | Type                                                                                                                                                                      |
| ----------------------------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| options<mark style="color:red;">\*</mark> |             | `{ id: string }` or `{ bounds: { position?: { x?: number; y?: number }; size?: { height?: number; width?: number } }; desktopId?: string }` or `{ bounds: "fullscreen" }` |

#### Return

A Promise that resolves with the window was moved. If the move isn't possible (for example trying to make a window fullscreen that doesn't support it), the promise will be rejected.

## Types

### WindowManagement.Window

A Window from an [Application](/api-reference/utilities.md#application) on a [Desktop](#windowmanagement.desktop).

#### Properties

| Property                                             | Description | Type                                                                                                |
| ---------------------------------------------------- | ----------- | --------------------------------------------------------------------------------------------------- |
| active<mark style="color:red;">\*</mark>             |             | `boolean`                                                                                           |
| bounds<mark style="color:red;">\*</mark>             |             | `{ position: { x: number; y: number }; size: { height: number; width: number } }` or `"fullscreen"` |
| desktopId<mark style="color:red;">\*</mark>          |             | `string`                                                                                            |
| fullScreenSettable<mark style="color:red;">\*</mark> |             | `boolean`                                                                                           |
| id<mark style="color:red;">\*</mark>                 |             | `string`                                                                                            |
| positionable<mark style="color:red;">\*</mark>       |             | `boolean`                                                                                           |
| resizable<mark style="color:red;">\*</mark>          |             | `boolean`                                                                                           |
| application                                          |             | [`Application`](/api-reference/utilities.md#application)                                            |

### WindowManagement.Desktop

A Desktop represents a virtual desktop on a Screen.

#### Properties

| Property                                   | Description | Type                                                            |
| ------------------------------------------ | ----------- | --------------------------------------------------------------- |
| active<mark style="color:red;">\*</mark>   |             | `boolean`                                                       |
| id<mark style="color:red;">\*</mark>       |             | `string`                                                        |
| screenId<mark style="color:red;">\*</mark> |             | `string`                                                        |
| size<mark style="color:red;">\*</mark>     |             | `{ height: number; width: number }`                             |
| type<mark style="color:red;">\*</mark>     |             | [`WindowManagement.DesktopType`](#windowmanagement.desktoptype) |

### WindowManagement.DesktopType

The type of a [Desktop](#windowmanagement.desktop).

#### Enumeration members

| Name       | Description                                                                               |
| ---------- | ----------------------------------------------------------------------------------------- |
| User       | The default Desktop type. It can contain any number of [Window](#windowmanagement.window) |
| FullScreen | A Desktop made of a single fullscreen window                                              |


---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://developers.raycast.com/api-reference/window-management.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
