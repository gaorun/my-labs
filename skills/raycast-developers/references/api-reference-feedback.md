# Feedback

Raycast has several ways to provide feedback to the user:

* [Toast](/api-reference/feedback/toast.md) *- when an asynchronous operation is happening or when an error is thrown*
* [HUD](/api-reference/feedback/hud.md) *- to confirm an action worked after closing Raycast*
* [Alert](/api-reference/feedback/alert.md) *- to ask for confirmation before taking an action*

![](/files/p2Ao61w6yFE9oEI2qsvA)


---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://developers.raycast.com/api-reference/feedback.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
