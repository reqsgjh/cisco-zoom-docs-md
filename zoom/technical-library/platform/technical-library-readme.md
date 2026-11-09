> For the complete documentation index, see [llms.txt](https://library.zoom.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://library.zoom.com/start-here/readme.md).

# Welcome to the Zoom Technical Library

The Zoom Technical Library is your destination for advanced Zoom product documentation and processes! We understand there are many settings, switches, and knobs available across our platform, and we want to support Zoom platform admins with the best resources we can, so we’ve created this library with systems admins and technical folks in mind. Below is a sneak peek at the types of resources you can expect to see added over time:

<table data-view="cards" data-full-width="false"><thead><tr><th></th><th></th><th data-hidden data-card-cover data-type="files"></th></tr></thead><tbody><tr><td><strong>Explainers</strong></td><td>Explainers are scannable resources designed to make Zoom’s products easier to understand.<br><br>By blending the structure of an FAQ with some elements of a whitepaper, these documents break down technical concepts into short summaries and fuller explanations.<br><br>Each section header delivers a quick takeaway, while the accompanying content offers clarity for those seeking more depth.<br><br><br><br><br><br><br><br><br></td><td><a href="https://1175968039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FctBXUMeBy4rtLMmMkKRG%2Fuploads%2FUiK9cwjv8476yPvZWQMm%2Fexplainer-header.png?alt=media&amp;token=2b1e88bf-81b5-4008-ace4-75a1c332f659">explainer-header.png</a></td></tr><tr><td><strong>Field Guides</strong></td><td>Field Guides act as navigation tools and deployment guides for Zoom products and features.<br><br>These documents focus on helping IT admins complete complex tasks or processes, like deploying the Zoom Phone Local Survivability Module or configuring advanced Zoom Contact Center features.<br><br>Within these documents, you can expect clear, step-by-step instructions and practical tips that streamline implementation and support successful, organization-wide deployments.<br><br><br><br><br></td><td><a href="https://1175968039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FctBXUMeBy4rtLMmMkKRG%2Fuploads%2Fgit-blob-b57b3483deae1f1383af951ff63fe8d588d61042%2FCEF12B57-636A-4ECD-9955-857E2FFF55CA.png?alt=media">field guide-header.png</a></td></tr><tr><td><strong>Bluepapers</strong></td><td>Bluepapers, named after Zoom’s signature color, serve as in-depth strategic resources that expand on standard whitepapers.<br><br>These documents explore entire product lines or services—like Zoom Phone and Zoom Contact Center—with comprehensive overviews, key insights, and summaries of essential topics.<br><br>Ideal for gaining a complete understanding, Bluepapers serve as a go-to resource for deep insight into Zoom's products.<br><br><br><br><br><br><br><br></td><td><a href="https://1175968039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FctBXUMeBy4rtLMmMkKRG%2Fuploads%2Fgit-blob-bbd65be889befaf94e8a709b40032a5c46d4a03d%2F3D7AD506-BF06-4D2D-801A-A7E65F231AE1.png?alt=media">3D7AD506-BF06-4D2D-801A-A7E65F231AE1.png</a></td></tr></tbody></table>

Whether you’re a seasoned Zoom admin, or you're just getting started, there will be something for everyone. Bookmark this site and check back for updates as we grow this space.

When you’re ready to jump in, use the menu on the left to choose a product, expand its documentation options, and select the resource that best fits your needs.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation by asking a question.

Perform an HTTP GET request on the following URL with the `ask` and `goal` query parameters:

```
GET https://library.zoom.com/start-here/readme.md?ask=<question>&goal=<user_goal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is what the user is ultimately trying to achieve, the reason they need the answer. Sharing it helps GitBook give you a better, more relevant answer. A goal is most helpful when it describes the outcome the user wants rather than restating the question. For example, with `ask=how do I create an API token`, a goal like `automate deployments from our CI pipeline` lets GitBook tailor the answer to that use case.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
