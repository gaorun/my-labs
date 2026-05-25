# getFavicon

Icon showing the favicon of a website.

A favicon (favorite icon) is a tiny icon included along with a website, which is displayed in places like the browser's address bar, page tabs, and bookmarks menu.

![Favicon example](/files/MF8rBzZXaFDx4I5MdQWu)

## Signature

```ts
function getFavicon(
  url: string | URL,
  options?: {
    fallback?: Image.Fallback;
    size?: boolean;
    mask?: Image.Mask;
  },
): Image.ImageLike;
```

* `name` is a string of the subject's name.
* `options.fallback` is a [Image.Fallback](https://developers.raycast.com/utilities/icons/pages/-MiwANRdFuMoKkR6at_E#image.fallback) icon in case the Favicon is not found. By default, the fallback will be `Icon.Link`.
* `options.size` is the size of the returned favicon. By default, it is 64 pixels.
* `options.mask` is the size of the [Image.Mask](https://developers.raycast.com/utilities/icons/pages/-MiwANRdFuMoKkR6at_E#image.mask) to apply to the favicon.

Returns an [Image.ImageLike](/api-reference/user-interface/icons-and-images.md) that can be used where Raycast expects them.

## Example

```tsx
import { List } from "@raycast/api";
import { getFavicon } from "@raycast/utils";

export default function Command() {
  return (
    <List>
      <List.Item icon={getFavicon("https://raycast.com")} title="Raycast Website" />
    </List>
  );
}
```


---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://developers.raycast.com/utilities/icons/getfavicon.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
