> For the complete documentation index, see [llms.txt](https://library.zoom.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://library.zoom.com/ai/ai-whitepaper.md).

# Zoom AI Whitepaper

The Zoom AI Whitepaper for Zoom Workplace, Webinars, and Events

Welcome to Zoom's Artificial Intelligence Whitepaper documentation for Zoom Workplace, Webinars, and Events.

### How to Use this Document

These pages explain how Zoom uses artificial intelligence across its products and services for Zoom Workplace, Webinars, and Events. Other Zoom products are not currently included across these pages. Some sections describe shared AI capabilities that support many features across the platform, while other sections explain specific features one by one. Because Zoom’s AI capabilities are broad and often work in different ways depending on the product, this document is organized into sections that move from general platform concepts to more specific features and data flows.

### Disclaimer

This document is provided for informational purposes only. It describes and illustrates AI features and capabilities across the Zoom platform, but it does not guarantee that any feature, capability, integration, or service described here is currently available based on account or deployment environment.

Access to and use of these features may depend on factors such as subscription plan, license assignment, administrator settings, regional availability, product configuration, technical compatibility, credit availability, usage limits, and other commercial or operational requirements.

Last updated: September 25, 2026

{% content-ref url="/pages/ccJZGWshwGl5W2iawBmN" %}
[Introduction: AI at Zoom](/ai/ai-whitepaper/introduction-ai-at-zoom.md)
{% endcontent-ref %}

{% content-ref url="/pages/nfwptY90SC3RkQf5GMvU" %}
[Models, Processing, Storage, and Usage](/ai/ai-whitepaper/models-processing-storage-and-usage.md)
{% endcontent-ref %}

{% content-ref url="/pages/OcAnZEz2A939uctFHclG" %}
[Zoom AI Features](/ai/ai-whitepaper/zoom-ai-features.md)
{% endcontent-ref %}

{% content-ref url="/pages/pjXLF8zPHeyF9pXhkPo5" %}
[My Notes](/ai/ai-whitepaper/my-notes.md)
{% endcontent-ref %}

{% content-ref url="/pages/HpcmmUjaZoYTq2kOfadl" %}
[ZoomMate](/ai/ai-whitepaper/zoommate.md)
{% endcontent-ref %}

{% content-ref url="/pages/woDTHqjNYuwqZOYBOPrZ" %}
[AI Productivity Suite](/ai/ai-whitepaper/ai-productivity-suite.md)
{% endcontent-ref %}

{% content-ref url="/pages/t7VIDHxkOkomFgrcHReu" %}
[Diagrams and Data Flows](/ai/ai-whitepaper/diagrams.md)
{% endcontent-ref %}

{% content-ref url="/pages/u35SbLPJyMhURYfJmEte" %}
[Feature Availability Table](/ai/ai-whitepaper/feature-availability.md)
{% endcontent-ref %}

{% content-ref url="/pages/xZltS1g6KFFvI4bLmDF1" %}
[APIs](/ai/ai-whitepaper/apis.md)
{% endcontent-ref %}

{% content-ref url="/pages/8P5ghDH4nbe3bEAEOrcS" %}
[Administrative Controls](/ai/ai-whitepaper/administrative-controls.md)
{% endcontent-ref %}

{% content-ref url="/pages/v4O85zZi0JV53JXctQim" %}
[Zoom's Commitment to Responsible AI](/ai/ai-whitepaper/zooms-commitment-to-responsible-ai.md)
{% endcontent-ref %}

{% content-ref url="/pages/pWjbnkgEWElN7yI4VKFy" %}
[Data Governance and Privacy](/ai/ai-whitepaper/data-governance-and-privacy.md)
{% endcontent-ref %}

{% content-ref url="/pages/Dge7YkzuG937s0kv3hZS" %}
[Security Framework](/ai/ai-whitepaper/security-framework.md)
{% endcontent-ref %}

{% content-ref url="/pages/ZqrYSBKr8P6iNwW2waxV" %}
[User Transparency and Notice](/ai/ai-whitepaper/user-transparency-and-notice.md)
{% endcontent-ref %}

*Authored by Jakob Ganschow*


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation by asking a question.

Perform an HTTP GET request on the following URL with the `ask` and `goal` query parameters:

```
GET https://library.zoom.com/ai/ai-whitepaper.md?ask=<question>&goal=<user_goal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is what the user is ultimately trying to achieve, the reason they need the answer. Sharing it helps GitBook give you a better, more relevant answer. A goal is most helpful when it describes the outcome the user wants rather than restating the question. For example, with `ask=how do I create an API token`, a goal like `automate deployments from our CI pipeline` lets GitBook tailor the answer to that use case.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
