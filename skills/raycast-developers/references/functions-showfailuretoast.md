# showFailureToast

Function that shows a failure [Toast](/api-reference/feedback/toast.md) for a given Error.

## Signature

```ts
function showFailureToast(
  error: unknown,
  options?: {
    title?: string;
    primaryAction?: Toast.ActionOptions;
  },
): Promise<T>;
```

### Arguments

* `error` is the error to report.

With a few options:

* `options.title` is a string describing the action that failed. By default, `"Something went wrong"`
* `options.primaryAction` is a Toast [Action](https://developers.raycast.com/utilities/functions/pages/ZQGaxRdMQYCgHooVmd5o#toast.actionoptions).

### Return

Returns a [Toast](/api-reference/feedback/toast.md).

## Example

```tsx
import { showHUD } from "@raycast/api";
import { runAppleScript, showFailureToast } from "@raycast/utils";

export default async function () {
  try {
    const res = await runAppleScript(
      `
      on run argv
        return "hello, " & item 1 of argv & "."
      end run
      `,
      ["world"],
    );
    await showHUD(res);
  } catch (error) {
    showFailureToast(error, { title: "Could not run AppleScript" });
  }
}
```


---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://developers.raycast.com/utilities/functions/showfailuretoast.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
