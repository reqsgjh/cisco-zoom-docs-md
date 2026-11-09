> For the complete documentation index, see [llms.txt](https://library.zoom.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://library.zoom.com/admin-corner/architecture-and-design.md).

# Architecture and Design

This documentation provides technical implementation details, configuration workflows, and strategic practices designed specifically for administrators deploying Zoom solutions.

You'll find step-by-step procedures that streamline complex configurations, troubleshooting resources that accelerate resolution times, and practical examples that demonstrate real-world application scenarios.

Topics within connect technical specifications to measurable business outcomes, enabling you to architect solutions, support client implementations, and identify opportunities for feature expansion. Whether you're conducting initial deployments, optimizing existing environments, or evaluating advanced capabilities for your organization, this documentation serves as your definitive resource for successful Zoom product utilization.

{% content-ref url="/pages/tNHUOLjkVSj9grI0EKHJ" %}
[Business Continuity and Disaster Recovery Whitepaper](/admin-corner/architecture-and-design/bcdr-whitepaper.md)
{% endcontent-ref %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation by asking a question.

Perform an HTTP GET request on the following URL with the `ask` and `goal` query parameters:

```
GET https://library.zoom.com/admin-corner/architecture-and-design.md?ask=<question>&goal=<user_goal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is what the user is ultimately trying to achieve, the reason they need the answer. Sharing it helps GitBook give you a better, more relevant answer. A goal is most helpful when it describes the outcome the user wants rather than restating the question. For example, with `ask=how do I create an API token`, a goal like `automate deployments from our CI pipeline` lets GitBook tailor the answer to that use case.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
