> For the complete documentation index, see [llms.txt](https://library.zoom.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://library.zoom.com/ai/ai-whitepaper/introduction-ai-at-zoom.md).

# Introduction: AI at Zoom

An Introduction to the Zoom AI Whitepaper for Zoom Workplace, Webinars, and Events

Artificial Intelligence is rapidly evolving and becoming an integral part of everyday life, powering everything from large and small language models to specialized algorithmic functions. While generative AI enables seamless interaction between humans and machines for content creation, problem-solving, and decision-making, AI also exists in more specialized applications. Automation tools streamline workflows, while services like captioning and translation break down communication barriers, making collaboration more efficient and accessible. As AI continues to advance, its applications are transforming industries by enhancing efficiency, accuracy, and innovation, fundamentally reshaping the way businesses operate.

Given AI’s expanding role in the modern workplace, this document explains how AI is used across the Zoom platform. It describes Zoom’s shared AI foundation, the product-specific AI features built into different Zoom products, and ZoomMate as the broader AI work surface that helps users move from conversation to completion. Together, these sections are intended to help readers understand how Zoom uses AI across communication, collaboration, productivity, and follow-through.

## **Zoom AI**

Zoom AI is the shared artificial intelligence layer that powers AI-enabled experiences across the Zoom platform. It includes the broader set of AI technologies, models, and supporting systems Zoom uses to deliver intelligent features across its products. In practical terms, Zoom AI is the foundation that allows Zoom to provide AI-assisted experiences across communication, collaboration, productivity, and follow-through, rather than limiting AI to a single standalone feature or application.

This shared AI layer supports ZoomMate as well as a wide range of product-specific capabilities, including features such as real-time translation, transcription, in-meeting questions, personal audio isolation, chat compose, and other AI-assisted experiences. It includes Zoom’s multi-model and multi-deployment approach to AI, including its federated architecture, Zoom-Hosted Models Plus (ZM+), Zoom-Hosted Models Only (ZMO), and on-premises AI offerings. Together, these approaches form the technical foundation for AI across the Zoom platform.

## **AI Features**

#### <mark style="color:blue;">AI Features: Embedded AI capabilities that provide focused assistance across Zoom products</mark>

Zoom AI features are product-specific capabilities that use artificial intelligence within particular Zoom products and workflows, and are usually embedded directly into the product experience where the task occurs. They are designed to help with specific activities such as summarizing a meeting, drafting a chat message, suggesting an email reply, answering a question during a live meeting, or generating a post-call recap.

These features can work on their own within the product where they appear, but they can also produce outputs that support broader ZoomMate experiences. For example, a Meeting Summary created after a Zoom Meeting may later become useful context for ZoomMate, while a feature such as Chat Compose or Meeting Questions is mainly designed to help in that immediate product experience. In this way, Zoom AI features are the distributed, product-level layer of AI across Zoom.

Examples include features across Meetings, Chat, Whiteboard, Events, Mail, Calendar, and Phone, such as meeting summaries, in-meeting questions, transcription, My Notes, chat compose, chat summarization, channel summaries, translation, email drafting and replies, scheduling assistance, call summaries, voicemail features, and task extraction.

## **ZoomMate**

#### <mark style="color:blue;">ZoomMate: Your intelligent Workplace teammate helping you accomplish more from conversation to completion</mark>

ZoomMate is an intelligent, conversational digital teammate at the core of the Zoom Workplace platform, designed to enhance productivity, streamline collaboration, and reduce employee workload.

Every day, AI tools are increasingly integrated into the modern workforce and are no longer limited to performing specific tasks — like automating data entry, drafting emails, generating reports, or performing basic algorithmic functions. Rather, emerging AI tools represent a transformative shift, fundamentally changing the way we work. ZoomMate exemplifies this, going beyond simple task automation by acting as a dedicated teammate that helps users accomplish more from conversation to completion.

For example, consider a sales leader preparing for a high-stakes customer meeting. The work may begin with a recent Zoom Meeting in which the team discusses the customer’s priorities, competitive risks, and open technical questions. From that conversation, Zoom’s AI features can generate a meeting summary, identify action items, and surface the follow-up responsibilities assigned to different team members. A user can then turn to ZoomMate to continue the work from there rather than starting over in a separate tool.

Using context from across Zoom Workplace and connected systems, ZoomMate can gather the meeting summary, review related chat discussions, reference supporting materials in Zoom Canvas, pull account context from a connected CRM, and incorporate additional research from approved internal or external sources. From that combined context, ZoomMate can help produce a customer briefing, draft a proposal outline, create follow-up tasks, and generate a structured strategy document. If the user needs to present that work, ZoomMate can also help turn the same underlying context into presentation materials using Zoom Slides.

What makes ZoomMate different from a conventional, generative AI assistant is that the work does not stop at summarization or drafting. ZoomMate can help carry context forward across the full process, from the original conversation, to the decisions that were made, to the documents and actions that follow. In that sense, ZoomMate functions less like a single-purpose tool and more like a workplace teammate that helps users connect information, coordinate follow-through, and turn work in progress into finished outcomes.

## **Interface Protocols**

Before moving into more detailed features and data flows, it is helpful to understand some of the underlying protocols that help power Zoom’s AI capabilities. This section explains Model Context Protocol (MCP), one of the leading interoperability standards that help AI connect to tools, data, workflows, and other agents.

### Model Context Protocol

#### <mark style="color:blue;">Model Context Protocol (MCP): A Standard for Connecting AI to Tools to Accomplish More</mark>

As part of its AI architecture, Zoom uses the Model Context Protocol (MCP)—an open standard that enables secure connections between models, tools, data sources, and workflows. MCP plays a key role in advancing agentic AI by replacing the need for one-off integrations that each company must build and maintain separately. Instead, it provides a shared, structured framework that exposes capabilities to AI models in a consistent way. This foundation allows AI systems to act more like intelligent agents—by not only answering questions, but also taking action directly within the systems users rely on.

Refer to Zoom’s Developer Docs for more information on [MCP at Zoom](https://developers.zoom.us/docs/mcp/).

#### <mark style="color:blue;">How MCP Works in Practice — Like ordering off a menu</mark>

At its core, MCP is built on a client–server model. Think of the AI environment (like ChatGPT or Claude) like a client that wants to get work done, and external systems (like Jira, Confluence, or a database) as servers that publish what they can do. Each server provides a clear list of functions—like “search knowledge base” or “create task.” The AI client then decides, in the middle of a conversation, when and how to use those functions.

In other words, connecting AI with an MCP server is just like ordering at a restaurant. You (the AI) walk into a restaurant, receive a menu (a list of services or functions available via the MCP server), and you (the AI) tell it what you want, and it responds. There is no guesswork of what is or isn’t available—everything is provided in the menu up front.

The following sections provide additional details for how MCP works:

#### <mark style="color:blue;">Step 1: Expose Capabilities Through Servers</mark>

Any system can run an MCP server. That server acts as the “menu,” publishing a structured description of the actions it supports. For example, Jira might publish functions like “search issues” or “update ticket.” Because these functions follow MCP’s shared format, the AI can understand them immediately without custom engineering.

#### <mark style="color:blue;">Step 2: AI Acts as a Client</mark>

On the other side, the AI environment plays the role of the client. It reads the menu of available functions, remembers them, and decides which to call when responding to a user. This means the AI doesn’t need to be programmed ahead of time with thousands of possible integrations—it simply learns what’s available when the connection is made.

#### <mark style="color:blue;">Step 3: Securely Pass Context</mark>

MCP also defines how context and permissions are passed along. This helps ensure that when the AI uses a function, it does so only within the boundaries of what the user is allowed to access. For example, if a user has permission to see only their team’s Jira tickets, MCP makes sure the AI respects that scope. This security layer is what makes MCP practical for enterprise use, where sensitive data and access controls are non-negotiable.

#### <mark style="color:blue;">Why MCP Matters</mark>

By standardizing how AI connects to external systems, MCP removes the friction of custom integrations and ensures safety and consistency. Users benefit because the AI can not only answer questions but also take informed actions across a variety of tools in a way that feels seamless and secure.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation by asking a question.

Perform an HTTP GET request on the following URL with the `ask` and `goal` query parameters:

```
GET https://library.zoom.com/ai/ai-whitepaper/introduction-ai-at-zoom.md?ask=<question>&goal=<user_goal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is what the user is ultimately trying to achieve, the reason they need the answer. Sharing it helps GitBook give you a better, more relevant answer. A goal is most helpful when it describes the outcome the user wants rather than restating the question. For example, with `ask=how do I create an API token`, a goal like `automate deployments from our CI pipeline` lets GitBook tailor the answer to that use case.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
