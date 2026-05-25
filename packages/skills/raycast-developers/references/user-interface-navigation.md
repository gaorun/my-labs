# Navigation

## API Reference

### useNavigation

A hook that lets you push and pop view components in the navigation stack.

You most likely won't use this hook too often. To push a new component, use the [Push Action](https://developers.raycast.com/api-reference/user-interface/pages/-MiwANRaRK1jG1WJw3dy#action.push). When a user presses `ESC`, we automatically pop to the previous component.

#### Signature

```typescript
function useNavigation(): Navigation;
```

#### Example

```typescript
import { Action, ActionPanel, Detail, useNavigation } from "@raycast/api";

function Ping() {
  const { push } = useNavigation();

  return (
    <Detail
      markdown="Ping"
      actions={
        <ActionPanel>
          <Action title="Push" onAction={() => push(<Pong />)} />
        </ActionPanel>
      }
    />
  );
}

function Pong() {
  const { pop } = useNavigation();

  return (
    <Detail
      markdown="Pong"
      actions={
        <ActionPanel>
          <Action title="Pop" onAction={pop} />
        </ActionPanel>
      }
    />
  );
}

export default function Command() {
  return <Ping />;
}
```

#### Return

A [Navigation](#navigation) object with [Navigation.push](#navigation) and [Navigation.pop](#navigation) functions. Use the functions to alter the navigation stack.

## Types

### Navigation

Return type of the [useNavigation](#usenavigation) hook to perform push and pop actions.

#### Properties

| Property                               | Description                                           | Type                                                      |
| -------------------------------------- | ----------------------------------------------------- | --------------------------------------------------------- |
| pop<mark style="color:red;">\*</mark>  | Pop current view component from the navigation stack. | `() => void`                                              |
| push<mark style="color:red;">\*</mark> | Push a new view component to the navigation stack.    | `(component: React.ReactNode, onPop: () => void) => void` |


---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://developers.raycast.com/api-reference/user-interface/navigation.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
