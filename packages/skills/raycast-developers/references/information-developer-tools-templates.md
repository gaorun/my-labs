# Templates

Raycast provides a variety of templates to kickstart your extension.

Raycast provides 3 types of templates:

* **Commands:** These are templates for [commands](/information/terminology.md).
* **Tools:** These are templates for [tools](/information/terminology.md#tool). You can select a different one for each tool that you add to your extension.
* **Extension Boilerplates:** These are fully built extensions designed to be tweaked by organizations for internal use.

## Commands

### Show Detail

<details>

<summary>Renders a simple Hello World from a markdown string.</summary>

![Detail Template Render](/files/G6k4UqVCeOxnyLcpFELZ)

{% hint style="info" %}
See the [API Reference](/api-reference/user-interface/detail.md) for more information about customization.
{% endhint %}

</details>

### Submit Form

<details>

<summary>Renders a form that showcases all available form elements.</summary>

![Submit Form Template Render](/files/kQ8WUHCqiV8I8wmTZMn0)

{% hint style="info" %}
See the [API Reference](/api-reference/user-interface/form.md) for more information about customization.
{% endhint %}

</details>

### Show Grid

<details>

<summary>Renders a grid of Icons available from Raycast.</summary>

Defaults to a large grid, but provides a selection menu to change the size.

![Grid Template Render](/files/Llhwy68VUmKTH5iCwNR5)

{% hint style="info" %}
See the [API Reference](/api-reference/user-interface/grid.md) for more information about customization.

See here for information about [Icons](/api-reference/user-interface/icons-and-images.md).
{% endhint %}

</details>

### Show List and Detail

<details>

<summary>Renders a list of options. When an option is selected, a Detail view is displayed.</summary>

![List and Detail Template Render](/files/CwvfYfZterHjj9ylTWQB)

{% hint style="info" %}
See the [API Reference](/api-reference/user-interface/list.md) for more information about customization.
{% endhint %}

</details>

### Menu Bar Extra

<details>

<summary>Adds a simple Menu Bar Extra with a menu.</summary>

![Menu Bar Extra Template Render](/files/7Vja3ck2uJKuSafp0sWU)

{% hint style="info" %}
See the [API Reference](/api-reference/menu-bar-commands.md) for more information about customization.
{% endhint %}

</details>

### Run Script

A example of a no-view command which shows a simple [HUD](/api-reference/feedback/hud.md).

### Show List

<details>

<summary>Renders a static list with each entry containing an icon, title, subtitle, and accessory.</summary>

![List Template Render](/files/FtiFMQa0ExqV4EY8w74z)

{% hint style="info" %}
See the [API Reference](/api-reference/user-interface/list.md) for more information about customization.
{% endhint %}

</details>

### Show Typeahead Results

<details>

<summary>Renders a dynamic and searchable list of NPM packages. The command fetches new items as the search is updated by the user.</summary>

![Typeahead Results Template Render](/files/4Q11BTzvQYdwOIYyZSbR)

</details>

### AI

<details>

<summary>Renders the output of an AI call in a Detail view.</summary>

![AI Template Render](/files/oOZkCZ9unzfRP2poom7U)

</details>

## Tools

<details>

<summary>A simple tool which asks for confirmation before executing.</summary>

![Tool with Confirmation Template Render](/files/7U1RxNZjfRJw06nyrd5D)

{% hint style="info" %}
See the [API Reference](/api-reference/tool.md) for more information about customization.
{% endhint %}

</details>

## Extension Boilerplates

The Raycast Team has created high-quality templates to reinforce team experiences with the Raycast API.

Run `npm init raycast-extension -t <template-name>` to get started with these extensions. All templates can be found on the [templates page](https://www.raycast.com/templates).

Specific instructions about customizing the template can be found on the relevant [template page](https://www.raycast.com/templates). Simply customize the template as you see fit, then run `npm run publish` in the extension directory to allow your team to install the extension.


---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://developers.raycast.com/information/developer-tools/templates.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
