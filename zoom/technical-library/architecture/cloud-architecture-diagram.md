> For the complete documentation index, see [llms.txt](https://library.zoom.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://library.zoom.com/admin-corner/architecture-and-design/cloud-architecture-diagram.md).

# Cloud Architecture Diagram

{% hint style="info" %}
Use the fullscreen arrows in the upper-right corner of the embedded Figma prototype to take a closer look at the Zoom Cloud Architecture diagram. Many product flows have been consolidated into a single "Common Platform Flows" page while some products have unique flows that are detailed on their own page.\
\
Please use the Feedback buttons to let us know if this is helpful and leave a comment with any other ideas we could implement in the future!
{% endhint %}

{% embed url="<https://www.figma.com/proto/NqxH9YSo3XzOKHSSe4zK6O/Architecture-Diagram-2025-%F0%9F%93%90?node-id=1771-8779&p=f&page-id=page-id=923:2401&scaling=width&starting-point-node-id=1771:8779&t=4OIRd8tmt5vIt1gU-1&viewport=1248,670,0.12>" %}

{% hint style="warning" %}
Having trouble loading the embedded view? Be sure to accept or reject the GitBook cookie request.
{% endhint %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation by asking a question.

Perform an HTTP GET request on the following URL with the `ask` and `goal` query parameters:

```
GET https://library.zoom.com/admin-corner/architecture-and-design/cloud-architecture-diagram.md?ask=<question>&goal=<user_goal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is what the user is ultimately trying to achieve, the reason they need the answer. Sharing it helps GitBook give you a better, more relevant answer. A goal is most helpful when it describes the outcome the user wants rather than restating the question. For example, with `ask=how do I create an API token`, a goal like `automate deployments from our CI pipeline` lets GitBook tailor the answer to that use case.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
