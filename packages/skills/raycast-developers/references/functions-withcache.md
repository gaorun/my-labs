# withCache

Higher-order function which wraps a function with caching functionality using Raycast's Cache API. Allows for caching of expensive functions like paginated API calls that rarely change.

## Signature

```tsx
function withCache<Fn extends (...args: any) => Promise<any>>(
  fn: Fn,
  options?: {
    validate?: (data: Awaited<ReturnType<Fn>>) => boolean;
    maxAge?: number;
  },
): Fn & { clearCache: () => void };
```

### Arguments

`options` is an object containing:

* `options.validate`: an optional function that receives the cached data and returns a boolean depending on whether the data is still valid or not.
* `options.maxAge`: Maximum age of cached data in milliseconds after which the data will be considered invalid

### Return

Returns the wrapped function

## Example

```tsx
import { withCache } from "@raycast/utils";

function fetchExpensiveData(query) {
  // ...
}

const cachedFunction = withCache(fetchExpensiveData, {
  maxAge: 5 * 60 * 1000, // Cache for 5 minutes
});

const result = await cachedFunction(query);
```


---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://developers.raycast.com/utilities/functions/withcache.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
