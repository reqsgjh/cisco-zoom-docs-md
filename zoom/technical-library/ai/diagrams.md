> For the complete documentation index, see [llms.txt](https://library.zoom.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://library.zoom.com/ai/ai-whitepaper/diagrams.md).

# Diagrams and Data Flows

Zoom AI diagrams and data flows for Zoom Workplace, Webinars, and Events

Zoom’s AI capabilities span a wide range of products, services, and workflows, which means no single diagram can reasonably or fully capture how AI works across the entire Zoom platform. Different features rely on different inputs, processing paths, storage behaviors, model interactions, and outputs. Some operate only on live, ephemeral data during an active interaction, while others create retained artifacts that can later support additional features. Some functions remain entirely within Zoom’s first-party environment, while others rely on Zoom’s federated AI architecture and, in some cases, connected external systems. To make this dynamic and expansive system easier to understand, this page presents a series of diagrams rather than relying on a single visual model. Each one highlights a different layer, pathway, or feature pattern within the broader Zoom AI platform. At the bottom of these sections are tables that outline which features are applicable, their associated product, and their artifact retention status. Later sections then examine certain bespoke product features individually, offering more focused explanations of how those specific capabilities work.

The sequence begins below with a simplified overview of Zoom AI in its most basic form, showing the platform in a first-party-centric state that uses Zoom’s standard federated model architecture but does not yet introduce third-party business integrations or external customer data sources beyond Zoom’s third-party AI model providers. From there, the diagrams gradually introduce more specialized parts of the platform, including Zoom’s AI approach options, the transformation of live audio into AI-usable artifacts, and the ways those artifacts can later support other features and workflows. Taken together, these diagrams are intended to make a highly complex system more approachable by breaking it into smaller, easier-to-follow views that reflect how different parts of Zoom’s AI platform work in practice.

## **Zoom AI**

<div data-with-frame="true"><figure><img src="https://1175968039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FctBXUMeBy4rtLMmMkKRG%2Fuploads%2F2U0TxpBDyYeXwPrgYc4C%2Fb7f1f3_UzmpbRMaSQe1r5xsXwWmQg_Zoom-AI-Architecture-v1_0.png?alt=media&amp;token=54f00b3a-833e-4cc7-a2e3-df492d45f26f" alt=""><figcaption><p>A simple overview of Zoom AI</p></figcaption></figure></div>

The diagram above presents Zoom’s AI platform in a simplified form, showing the platform in one of its most foundational states. It illustrates how different parts of Zoom’s broader product and service architecture known as the Zoom Web backend—including areas such as Meetings, Phone, Contact Center, automatic speech recognition, and other Zoom offerings—feed into the larger Zoom platform and contribute to the body of user-accessible content that can support downstream AI functionality.

A central concept in this diagram is **Zoom user content**. This refers to the content generated through a user’s interactions with Zoom products and services that may later serve as input, context, or artifacts for AI-powered experiences. Depending on the product and feature involved, this can include materials such as Zoom Chat messages, meeting summaries, transcripts, Canvas documents, My Notes, recordings, and other similar user-facing artifacts. These materials form an important part of the contextual layer that can support later AI-assisted retrieval, reasoning, summarization, and follow-through.

Some of this content may also be prepared for future AI use through retrieval infrastructure such as indexed retrieval or retrieval-augmented generation modules. In those cases, relevant artifacts can be ingested and indexed so they can be more efficiently located and used in later AI queries or processes. This helps Zoom AI work not only with live interactions, but also with retained context and prior user-generated materials across the platform.

Lastly, the diagram also introduces **Zoom AI** itself as the shared AI layer that operates across this broader ecosystem. In this simplified view, Zoom AI is shown through Zoom’s standard federated approach, in which Zoom can use both Zoom-hosted models running within Zoom’s own infrastructure and selected third-party AI model providers when appropriate for the task at hand. This federated model allows Zoom to route AI tasks through the most suitable available model environment while maintaining a unified AI experience across the platform.

## Zoom AI Service Model Approaches

<div data-with-frame="true"><figure><img src="https://1175968039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FctBXUMeBy4rtLMmMkKRG%2Fuploads%2FQp3shGm7hdT8CwqDc05v%2FZoom-AI-Service-Models---v1_1.png?alt=media&amp;token=f9794e05-fe6a-4077-8f32-a1ce53499227" alt=""><figcaption><p>Overview of Zoom's AI approaches, including Federated, ZM+, and ZMO</p></figcaption></figure></div>

The diagram above illustrates Zoom’s three AI approaches: the Federated Approach, Zoom-Hosted Models Plus (ZM+), and Zoom-Hosted Models Only (ZMO). Together, these represent the three primary ways Zoom provides AI services to customers, each offering a different balance of feature breadth, model flexibility, and data control.

The Federated Approach is Zoom’s standard and most feature-complete approach. It allows Zoom to work with multiple AI providers, including Zoom-hosted models and selected third-party model partners, so tasks can be routed to the model best suited for the request. ZM+ provides a more controlled deployment model by using Zoom-managed dedicated model instances, while ZMO keeps AI processing within Zoom-hosted models only, offering the most restrictive and controlled model path but with a more limited feature set.

For the purposes of this page, the diagrams that follow generally illustrate the federated approach, as it reflects Zoom’s standard approach and the broadest view of Zoom AI functionality. Organizations using ZM+ or ZMO can often interpret these same diagrams by mentally removing the third-party AI model providers and focusing on the remaining Zoom-managed portions of the flow.

Refer to the Zoom AI Models, Processing, Storage, and Usage page for more information.

## Live Media Features and Artifacts

<div data-with-frame="true"><figure><img src="https://1175968039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FctBXUMeBy4rtLMmMkKRG%2Fuploads%2F1qx2z9BKVCrRDN6aI2wG%2FLive-Media-Features-and-Artifacts-v3_1.png?alt=media&amp;token=3a25dc7c-2a97-4aa2-8fb8-671a24956d3e" alt=""><figcaption><p>Overview of how live media is transformed into speech-to-text data that powers Zoom AI features</p></figcaption></figure></div>

The diagram above illustrates how live media interactions—such as meetings and phone calls—can produce downstream AI-powered features and artifacts across the Zoom platform. In each case, live audio enters Zoom through the connection point associated with that product or service. For meetings, this is generally the **Multimedia Router (MMR)**. For telephony, audio typically enters through **SIP zones**.

Once the audio is ingested, it is routed to Zoom’s **Automatic Speech Recognition (ASR)** service, which converts the live audio into **speech-to-text data**. That speech-to-text data can be used in multiple ways depending on the enabled settings and features. In some cases, it is delivered immediately to users as **live captions**. In supported contexts, it may also be passed to Zoom’s **Live Translation** service, which translates the speech-to-text output into translated captions for participants in other languages.

Speech-to-text data can also support more persistent or derivative features. If **transcription** is enabled, or if a user is using **My Notes**, the ASR service can produce a transcript after the live session concludes. If transcript retention is not enabled, however, the speech-to-text data used during the interaction is not retained as a persistent transcript. Even in those cases, Zoom AI may still use the speech-to-text data ephemerally during the session to support live AI features.

For example, a user may ask **in-meeting questions** through Zoom AI during a meeting. In that case, Zoom AI can use the live speech-to-text data from the meeting to interpret the user’s question and generate a relevant answer grounded in the ongoing conversation.

A key distinction in this flow is that Zoom AI does not necessarily retain a transcript of the conversation simply because speech-to-text data was used during the session. Unless transcript retention is specifically enabled, or the data is being retained through a feature such as **My Notes**, the speech-to-text data itself may remain ephemeral. At the same time, some downstream artifacts produced from that data may persist. For example, if a user asks questions during a meeting, the resulting AI conversation or related notes may later remain available as a retained artifact even when a persistent transcript is not produced.

Some retained artifacts can also become the basis for additional downstream artifacts and workflows. A meeting summary, webinar summary, call summary, or a user’s My Notes may be converted into a **Zoom Canvas** document, where it can continue to be edited, expanded, and used as a working artifact. In turn, those resulting documents may later serve as context for other AI features or workflows discussed elsewhere in this document. In this way, live audio can lead not only to immediate AI features, but also to a chain of retained artifacts that continue to support later AI-assisted work across the Zoom platform.

This diagram is applicable to the following features:

|          Feature         |                                         Description                                         |     Product(s)     | Artifact Retention |
| :----------------------: | :-----------------------------------------------------------------------------------------: | :----------------: | :----------------: |
|       Live Captions      |                     Real-time speech-to-text captions for live sessions.                    | Meetings, Webinars |     Unretained     |
|    Translated Captions   |            Real-time translated captions generated from live speech-to-text data.           | Meetings, Webinars |     Unretained     |
|        Transcripts       |                   Retained text records of meeting speech-to-text content.                  |   Meetings, Phone  |      Retained      |
|      Meeting Summary     |     AI-generated summary of key meeting discussion points, decisions, and action items.     |      Meetings      |      Retained      |
|      Webinar Summary     |            AI-generated summary of key webinar content shared after the session.            |      Webinars      |      Retained      |
|       Call Summary       |               AI-generated post-call summary of key details and action items.               |        Phone       |      Retained      |
|         My Notes         | Personal notes, transcript, and meeting context retained for later reference and follow-up. |      Meetings      |      Retained      |
|      Follow-up Tasks     |                AI-suggested follow-up actions based on conversation details.                |     Zoom Tasks     |      Retained      |
| Voicemail Prioritization |                  AI-based ranking of voicemails by user-defined importance.                 |        Phone       |      Retained      |
|     Meeting Questions    |                 AI answers to meeting questions using live meeting context.                 |      Meetings      |      Retained      |
|     Webinar Questions    |                 AI answers to webinar questions using live webinar context.                 |      Webinars      |      Retained      |
|      Call Questions      |                    AI answers to call questions using live call context.                    |        Phone       |      Retained      |

## Recording Features

<div data-with-frame="true"><figure><img src="https://1175968039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FctBXUMeBy4rtLMmMkKRG%2Fuploads%2FQk8rEkziflIo1LRszVES%2FAI-Recording-Features-v1_1.png?alt=media&amp;token=95a406db-cf3c-4172-b92c-8c71f4e41c88" alt=""><figcaption><p>Overview of how Zoom processes recordings and AI features</p></figcaption></figure></div>

The diagram above illustrates how Zoom AI supports **recording-based AI features** by operating on the completed recording after the live session has ended. As with other audio-based Zoom experiences, the original media enters through the infrastructure associated with the product in use—such as the **MMR** for meetings or the relevant **SIP zone** for telephony. As part of that flow, the recording is created and sent to Zoom’s recording service, where the completed recording is then stored in Zoom content storage.

Once the recording has been finalized, the audio associated with that recording is sent to Zoom’s **Automatic Speech Recognition (ASR)** service for transcription. This process produces a **recording-specific transcript**, which may differ from speech-to-text data generated during the live session itself. In other words, the transcript associated with a completed recording is generated as part of the post-recording processing flow rather than simply copied from the live interaction layer.

After the recording transcript is produced, it can then be submitted to **Zoom AI** for additional analysis. In this stage, Zoom AI processes the transcript to identify higher-level recording artifacts such as summaries, highlights, chapters, and other structured representations of the conversation. This analysis is performed using Zoom’s AI processing layer, including Zoom-hosted models where applicable, to transform the raw recording transcript into more usable post-meeting or post-call outputs.

Once that analysis is complete, the resulting AI-generated artifacts are associated with the recording itself. This is what allows users viewing a recording to see not only the recording and transcript, but also the additional AI-generated layers that make the content easier to navigate and understand. In this way, the diagram shows how a completed recording can become the basis for a second stage of AI processing, producing enriched recording features that extend beyond the original stored media.

This diagram is applicable to the following features:

|                    Feature                    |                                                      Description                                                     |  Product(s) | Artifact Retention |
| :-------------------------------------------: | :------------------------------------------------------------------------------------------------------------------: | :---------: | :----------------: |
|                Smart Recording                |                        AI-generated highlights, chapters, and summaries for recorded meetings                        |   Meetings  |      Retained      |
|    Generate titles, descriptions, and tags    |                                AI-generated titles, descriptions, and tags for clips.                                |    Clips    |      Retained      |
| AI Content Creation for Recordings and Videos | Uses event recording transcripts to generate written content and AI-curated video snippets from key session moments. | Zoom Events |      Retained      |

## Derivative AI Features

<div data-with-frame="true"><figure><img src="https://1175968039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FctBXUMeBy4rtLMmMkKRG%2Fuploads%2FmRE1NMTpfCGXF0TbyAzt%2FAI-Derivative-Content-Generation-v3_1.png?alt=media&amp;token=389a8562-e8cc-4a2e-8871-7d8fafac9bdc" alt=""><figcaption><p>Overview of how Zoom processes derivative AI content generation features</p></figcaption></figure></div>

The diagram above illustrates how **derivative AI features** operate by using available user content as context for later AI-assisted tasks and outputs. In these cases, Zoom AI is no longer working only from live interaction data. Instead, it is drawing on artifacts that already exist within the user’s broader content environment in order to answer a question, synthesize information, or help produce a new result.

Depending on the task, this contextual material may include artifacts such as chat messages, meeting summaries, My Notes, transcripts, Zoom Canvas documents, Zoom Slide decks, Zoom Paper documents, Zoom Mail or Zoom Calendar content, connected third-party email or calendar data, or files uploaded by the user to support a particular request. In this way, Zoom AI is using previously created Zoom artifacts, along with integrated personal-level data where available, to help achieve a user’s requested end.

The diagram also reflects that this process can itself generate **new user content**. For example, Zoom AI may use existing materials to create a new Zoom Sheet, Zoom Canvas document, Zoom Slide deck, or Zoom Paper document. Once created, those new artifacts become part of the user’s broader content repository and may later be used again as context for future AI-assisted functions and workflows. This creates a layered progression in which earlier user content can support later outputs, and those outputs can in turn become new contextual artifacts over time.

This same pattern can appear in other Zoom surfaces as well. In environments such as **Zoom Hub** or the **AI Chat panel**, users may ask questions across the platform or interact with documents and materials available through Zoom’s AI productivity suite. In those cases, Zoom AI is again working from existing user-accessible artifacts to provide retrieval, synthesis, question answering, or follow-through, showing how derivative AI features extend the value of prior content into new tasks and outcomes.

{% hint style="info" %}
**Note**

Local user file uploads [can be disabled](https://support.zoom.com/hc/en/article?id=zm_kb\&sysparm_article=KB0077150).
{% endhint %}

This diagram is applicable to the following features:

|       Feature      |                                                                           Description                                                                          |           Product(s)          | Artifact Retention |
| :----------------: | :------------------------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------: | :----------------: |
| Content Generation | Content generation uses AI to create, refine, summarize, and organize documents, presentations, spreadsheets, and other outputs from natural language prompts. | Canvas, Sheets, Paper, Slides |      Retained      |
|    AI Chat panel   |                        Conversational AI assistance for asking questions, generating content, and working across available Zoom context.                       |         AI Chat panel         |      Retained      |
|    Ask Questions   |                                           AI-generated answers based on selected documents and materials in Zoom Hub.                                          |              Hub              |      Retained      |

## Generative and Composition Features

<div data-with-frame="true"><figure><img src="https://1175968039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FctBXUMeBy4rtLMmMkKRG%2Fuploads%2FtxyUNKDKQeruF5FlzS2j%2FGenerative-Text-Composition-and-Image-Creation-v2.png?alt=media&amp;token=dc5cdb13-d88d-4f31-8b6d-e629bf5a7e20" alt=""><figcaption><p>Overview of how Zoom processes generative and composition AI requests</p></figcaption></figure></div>

The diagram above illustrates how **generative and composition features** operate within the Zoom AI platform. Unlike derivative AI features, which rely on pre-existing user content to help achieve a later task or output, generative and composition features are often driven more directly by the user’s immediate input. In many cases, these features do not depend on retained Zoom artifacts already stored elsewhere in the user’s content environment. Instead, they are primarily powered by direct user prompts, queries, uploaded files, or the immediate on-screen content associated with the active product experience.

This distinction is especially important for features that work from content visible in the user’s current context rather than from previously indexed or retained artifacts. For example, when a user summarizes a chat thread, summarizes an email, or asks Zoom AI to draft a reply to an email, the relevant content is typically taken from the active client context and packaged into a request payload for Zoom AI processing. In other words, Zoom is not necessarily retrieving that content from a separate server-side repository in order to fulfill the task. Instead, the relevant information from the active thread, message set, or other visible interface context is converted into text form and submitted to Zoom AI from the Zoom Workplace app so the service can perform natural language processing, summarization, or generation.

The diagram also includes generative use cases that rely primarily on direct user instruction rather than textual source material. For example, when a user requests image generation, the user describes the desired output through a prompt, and the model generates the image based on that description. In some product contexts, such as Zoom Whiteboard, this image generation may rely on third-party AI model providers. In other contexts, Zoom may use its own hosted models. For example, Zoom’s virtual background image generation can rely on a Zoom-hosted model that uses embeddings and related processing to generate visual outputs, with the resulting content passing through moderation controls before being returned to the user.

Taken together, the diagram shows that generative and composition features often depend less on retained artifacts and more on immediate user intent, active client-side context, or uploaded supporting materials. In this way, they represent another major mode of Zoom AI operation: not only retrieving and reasoning across prior content, but also generating new outputs directly from the user’s current request and surrounding context.

This diagram is applicable to the following features:

|            Feature           |                                                                       Description                                                                       |         Product(s)        |  Artifact Retention |
| :--------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------: | :-----------------------: | :-----------------: |
|      Virtual Background      |                              Uses AI to create custom virtual background images from user prompts for use in Zoom sessions.                             | Meetings, Events, Webinar | Retained (if saved) |
|       Image Generation       |               Uses AI to transform whiteboard drawings or rough visual artifacts into more polished, rendered, or stylized visual outputs.              |         Whiteboard        | Retained (if saved) |
|       Image Generation       |            Uses AI to create branded images and other visual assets for events, such as headers, session images, and expo-related materials.            |           Events          | Retained (if saved) |
|      Content Generation      | Uses AI to generate on-screen whiteboard content such as text, sticky notes, tables, mind maps, and other structured visual elements from user prompts. |         Whiteboard        | Retained (if saved) |
|      Content Generation      |                 Uses AI to generate written event content such as descriptions, session details, speaker bios, and lobby announcements.                 |           Events          | Retained (if saved) |
|         Email Compose        |                             Uses AI to draft and refine email content, including message bodies, subject lines, and replies.                            |           Email           |  Retained (if sent) |
|         Chat Compose         |                           Uses AI to draft and revise chat messages based on user prompts and available conversation context.                           |            Chat           |  Retained (if sent) |
|         Email Summary        |                                            Uses AI to summarize the key content of an email or email thread.                                            |           Email           |      Unretained     |
| Message, Thread, Doc Summary |                   Uses AI to summarize chat messages, conversation threads, and supported attached documents or linked Canvas content.                  |            Chat           |      Unretained     |
|         Smart Upload         |                       Extracts event details from uploaded files to automatically build sessions, speakers, and custom questions.                       |        Zoom Events        | Retained (if saved) |

## My Notes

### My Notes in Zoom Meetings

<div data-with-frame="true"><figure><img src="https://1175968039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FctBXUMeBy4rtLMmMkKRG%2Fuploads%2F1J2L6ZTHOfpSR12iIeTo%2FMy-Notes-in-Zoom-Meetings-v3.png?alt=media&amp;token=e419736a-3ae1-4f0f-88a9-7222ab47c380" alt=""><figcaption><p>Overview of My Notes data flows in Zoom meetings</p></figcaption></figure></div>

The diagram above shows how, within Zoom Meetings, My Notes uses the meeting’s existing audio path rather than relying on other audio present on the user’s device. When My Notes is enabled during a Zoom Meeting, it accesses the shared meeting audio routed through the meeting’s Multi-Media Router (MMR) session. That audio is then processed by Zoom’s Automatic Speech Recognition (ASR) service to generate a transcript, which is delivered to the user’s device and can later support post-meeting note generation.

In this flow, transcription is based specifically on the Zoom Meeting audio associated with that meeting session. It is not based on unrelated local device audio outside the meeting itself. After the meeting concludes, the resulting transcript and notes can remain available according to the user’s applicable retention settings, while the underlying audio used for transcription is not retained after processing is complete.

### My Notes Outside of Zoom Meetings

<div data-with-frame="true"><figure><img src="https://1175968039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FctBXUMeBy4rtLMmMkKRG%2Fuploads%2Fvi76T0ydpQuhTKCQjp7k%2FMy-Notes-in-Third-Party-Meetings-v7.png?alt=media&amp;token=44ca74c0-2307-42ba-ab6f-a3aa8185116e" alt=""><figcaption><p>Overview of My Notes data flows outside of Zoom meetings</p></figcaption></figure></div>

The diagram above shows how, outside Zoom Meetings, My Notes operates through the user’s local device audio rather than through a shared Zoom meeting session. If enabled during a third-party meeting or an in-person discussion, My Notes can use operating system–level access to the user’s microphone and, where applicable, system audio to capture the local audio available on that device. This audio is then routed through a single-user MMR session and processed by Zoom’s Automatic Speech Recognition (ASR) service to generate a transcript, which is delivered to the user’s device and can later support post-meeting note generation.

This means that, outside Zoom Meetings, transcription is based exclusively on the audio transmitted from the user’s local device rather than from a shared Zoom meeting audio stream. My Notes may also prompt the user to begin a new note when device microphone activity is detected, helping surface the feature in situations such as third-party meetings, browser-based recordings, or other microphone-active workflows. As with the in-meeting flow, the audio used for transcription is not retained after transcription is complete, while the resulting notes and transcripts can remain saved in the user’s account according to the applicable retention settings.

## ZoomMate

<div data-with-frame="true"><figure><img src="https://1175968039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FctBXUMeBy4rtLMmMkKRG%2Fuploads%2FvysqwhYkSz3T5mnjci1c%2FZoomMate-Architecture-minus-Memory-v2.png?alt=media&amp;token=ae9e2f47-4349-426f-bb85-8e92152da77b" alt=""><figcaption><p>Overview of ZoomMate data flows</p></figcaption></figure></div>

The diagram above illustrates how **ZoomMate functions as a primary work surface within Zoom Workplace**, operating at the point where user context, connected knowledge, and execution capabilities come together. Rather than existing only as a standalone assistant, ZoomMate sits at the center of a broader working environment in which users can search, reason, create, and act across the materials and systems that support their day-to-day work.

A major part of this role comes from ZoomMate’s access to **first-party Zoom content**. This can include artifacts such as summaries, My Notes, recordings, Canvas documents, chat messages, and other user-generated materials created across the Zoom platform. These artifacts help provide ZoomMate with the context it needs to answer questions, synthesize information, generate outputs, and support follow-through. ZoomMate can also use **memory**, allowing it to incorporate relevant user preferences or work-related details when helping complete a task.

The diagram also shows how ZoomMate extends beyond Zoom-native content by integrating with **third-party knowledge sources**. For example, connected cloud storage services such as Google Drive or OneDrive can serve as external repositories of user-accessible information. When these sources are integrated, Zoom can index approved content to support retrieval across those materials, allowing ZoomMate to use **agentic search** to work across both Zoom content and connected third-party knowledge. In this way, ZoomMate can search not only across what exists within Zoom, but also across the documents and materials a user is authorized to access in connected external platforms.

Other personal data sources, such as **email and calendar** (excluding end-to-end encrypted emails), can also support ZoomMate, but they operate differently. Rather than being indexed, these sources generally communicate with ZoomMate through direct API-based retrieval. This makes them useful for tasks such as locating relevant email context, reviewing calendar information, or helping schedule events, without treating them as part of the indexed retrieval layer used for broader document search.

The diagram further reflects that ZoomMate can connect with a wider range of **third-party services and connectors** that support action-taking as well as knowledge access. These may include systems such as Jira, HubSpot, ServiceNow, Workday, and other connected business platforms. Through these connections, ZoomMate can perform **agentic tasks** on the user’s behalf, such as creating or updating records, retrieving information from external services, or carrying out other connected actions within those systems. This makes ZoomMate more than a retrieval and synthesis surface; it also functions as an execution layer that can help turn context into action.

This same foundation also helps power **agents** and **workflows** within the ZoomMate environment. Agents can use the same underlying context, retrieval paths, and connected systems to perform more dynamic, reasoning-based assistance, helping users carry out broader multi-step tasks with greater continuity and adaptability. Workflows, by contrast, can provide more structured and repeatable automation, allowing users to define recurring processes that operate across Zoom content and, where supported, connected external systems. In this way, ZoomMate serves not only as a conversational interface, but also as a point of orchestration for both dynamic agentic activity and more structured automation.

**Sandbox** can also support some of ZoomMate’s more advanced execution capabilities. For tasks that require code execution, file generation, automation, or other more sophisticated processing, ZoomMate can use a separate sandbox environment rather than relying only on standard conversational processing. This sandbox runs on Zoom’s AWS infrastructure and provides a short-lived, isolated execution layer for higher-complexity tasks, helping ZoomMate carry out certain operations in a more controlled environment. In this way, the same broader ZoomMate foundation that supports retrieval, reasoning, agents, and workflows can also support more advanced task execution when the requested work requires it.

Lastly, the diagram does not depict every underlying component that helps power ZoomMate. It does not explicitly show foundational capability layers such as skills, or other supporting structures that are part of Zoom AI’s broader infrastructure and design. Those elements are assumed to operate within the underlying AI system that enables ZoomMate’s behavior. The purpose of this diagram is instead to show the primary context, knowledge, and action surfaces through which ZoomMate functions as a unified work surface across Zoom and connected systems.

### ZoomMate Third-Party Connections and Indexing

<figure><img src="https://1175968039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FctBXUMeBy4rtLMmMkKRG%2Fuploads%2F16AaKIHy9GVIq6srhS4p%2FZoomMate-Third-Party-Connections-v1_1.png?alt=media&amp;token=122bae52-9f9e-49b3-a941-fb4250e600d8" alt="" width="375"><figcaption><p>Overview of how ZoomMate connects to third-party connections and data sources</p></figcaption></figure>

The diagram above illustrates two related but distinct parts of ZoomMate’s third-party data architecture. The first is how ZoomMate connects to supported third-party applications and services so it can retrieve information or take action within those systems. The second is how certain supported third-party content sources can be ingested and indexed so ZoomMate can later retrieve that content more efficiently through retrieval-augmented generation.

#### <mark style="color:blue;">ZoomMate can connect directly to third-party applications and services</mark>

One part of the diagram shows how ZoomMate connects to supported third-party applications such as Jira, Confluence, Salesforce, ServiceNow, Workday, cloud storage platforms, and other external business systems. These connections allow ZoomMate to operate beyond Zoom-native content by interacting with tools that store business data or support operational work outside the Zoom platform.

These connections are established over a TLS connection through authorized access models, such as API-based integrations or MCP-based connections. In either case, ZoomMate operates within the permissions granted by the connected service. This allows ZoomMate to retrieve relevant information from those systems, and where supported, take action within them on the user’s behalf. For example, ZoomMate may retrieve details from a Jira issue, search a Confluence page, update a record in ServiceNow, or use another connected system as part of carrying out a broader task.

This direct connection model is especially important for tasks that depend on current system state or live access to third-party tools. In those cases, ZoomMate can use the connected application as an active service endpoint rather than only as a repository of previously indexed content.

#### <mark style="color:blue;">ZoomMate can index approved third-party content for later retrieval</mark>

A second part of the diagram shows how ZoomMate can ingest and index content from supported third-party sources so that material can later be retrieved as part of a search or AI-assisted response. This indexed retrieval model is most relevant for connected content repositories such as cloud storage systems, knowledge bases, document platforms, and other supported sources where ZoomMate may need to search across a larger body of retained external content.

Once a supported source is connected and approved for indexing, ZoomMate can retrieve content from that source and prepare it for later search. This preparation process can include breaking larger files or records into smaller units and attaching metadata such as source, update time, ownership, and permission information. That content is then written into Zoom's indexing layer so it can later be searched through both exact matching and meaning-based retrieval.

When a user submits a request that depends on indexed third-party content, ZoomMate can search that indexed material, evaluate which results are most relevant, and apply the permission information associated with the original source so that only authorized content is eligible to appear. The most relevant authorized content can then be passed into ZoomMate’s AI layer as supporting context for the response. In this way, the diagram shows how indexed third-party content can help ZoomMate produce answers that are grounded in actual connected business materials rather than relying only on general model knowledge.

## Custom Avatars

### Avatar Creation

<div data-with-frame="true"><figure><img src="https://1175968039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FctBXUMeBy4rtLMmMkKRG%2Fuploads%2FAThLjvKEc1JVanLMyuf8%2Fimage.png?alt=media&amp;token=d62f86b5-43ea-4305-9343-a810938a01cd" alt=""><figcaption><p>Overview of the Custom Avatar creation process</p></figcaption></figure></div>

The diagram above illustrates how a custom avatar is created from a user’s recorded video and voice. The process begins when the user is presented with a script and prompted to record themselves reading it. This guided recording step allows Zoom to capture the audiovisual material needed to generate both the user’s avatar likeness and the associated voice model used in later avatar-based outputs.

After the user completes the recording, the audio and video components are processed through different paths. The audio is sent to a third-party service that generates a voice likeness based on the user’s recorded speech. Once that processing is complete, the third-party service returns a unique voice identifier to Zoom. Zoom stores this identifier as the user’s voice reference so it can be used later when generating avatar-based clips or other supported outputs that rely on that synthesized voice.

At the same time, the video component is sent to a Zoom-hosted avatar generation module, where Zoom processes the recorded visual material to create the user’s avatar representation. This results in an avatar template that Zoom stores for future use. Taken together, these two retained outputs—the stored voice identifier and the stored avatar template—allow Zoom to generate future clips or avatar-based media that reflect both the user’s likeness and their synthesized voice.

### Clip Creation

<div data-with-frame="true"><figure><img src="https://1175968039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FctBXUMeBy4rtLMmMkKRG%2Fuploads%2Fj2o9NYXibPtVTyctuHvq%2Fimage14.png?alt=media&amp;token=33174f0b-8f48-4de0-93a1-ee63ad8eac11" alt=""><figcaption><p>Overview of the Custom Avatar clip creation process</p></figcaption></figure></div>

The diagram above illustrates how a custom avatar clip is created from a user’s stored avatar and synthesized voice profile. The process begins when the user uploads the script they want the avatar to present. That script serves as the source content for the generated clip.\
\
From there, Zoom’s web backend coordinates two parallel inputs needed to create the final output. First, it sends the user’s stored voice identifier together with the script to the third-party voice generation service, which produces the audio for the clip using the user’s synthesized voice. Second, it sends the user’s stored avatar template to Zoom’s avatar generation module so the visual component of the clip can be prepared using the user’s previously created avatar likeness.\
\
Once the third-party voice generation service has produced the audio, that audio is returned to Zoom and passed into the avatar generation module. The avatar generation module then combines the stored avatar template with the generated voice audio, synchronizing the avatar’s facial and mouth movements to the spoken content. After this lip-syncing and rendering process is complete, Zoom produces the finished avatar clip and delivers it back to the user.

## Custom Dictionary

<div data-with-frame="true"><figure><img src="https://1175968039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FctBXUMeBy4rtLMmMkKRG%2Fuploads%2F4wdZuiAXND1LIsoho6Q8%2F818655_mV1OiRYaRC2-cqN80It6Bw_CAIC-Custom-Dictionary-v5.png?alt=media&amp;token=0eb0a608-e461-49c0-9248-80b0789c9304" alt=""><figcaption><p>Custom Dictionary data flows</p></figcaption></figure></div>

The diagram above illustrates how the Custom Dictionary feature helps improve the accuracy of speech-based Zoom outputs by giving Zoom’s Automatic Speech Recognition (ASR) service additional vocabulary context. This feature is designed to support words, abbreviations, jargon, product names, or specialized terminology that may be specific to a company, industry, team, or region and that might not otherwise be recognized or rendered correctly during transcription.

The process begins when an account administrator creates and stores a custom dictionary in the Zoom web portal. That dictionary contains the list of approved words or phrases the organization wants Zoom to recognize more accurately. Once the dictionary has been saved at the account level, it becomes available for use in supported meeting and speech-processing contexts.

When a user later starts a meeting, Zoom’s AASR service can receive the account’s custom dictionary as part of its processing context. As the ASR service converts live audio into speech-to-text data, it can compare perceived spoken language against the custom dictionary and attempt to map recognized sounds to the stored terms. This gives the ASR additional guidance about which words to look for, how certain terms may be spelled, and how abbreviations or specialized language should be interpreted.

The result is that the initial speech-to-text output can more accurately reflect the terminology actually used in the meeting. That improved accuracy can then carry forward into downstream artifacts derived from the conversation. For example, if a meeting summary, captions, transcript, or another speech-to-text data-based asset is later generated, those outputs can reflect a more accurate representation of the words spoken during the meeting, helping improve the quality and usefulness of the resulting AI-generated artifact.

## Custom Meeting Summary Templates

<div data-with-frame="true"><figure><img src="https://1175968039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FctBXUMeBy4rtLMmMkKRG%2Fuploads%2Figd7zj6YLNIds7iHCerA%2F786f73_aFTdIy-3TIKILtvQ0oxm2w_CAIC-Meeting-Summary-Templates-v5.png?alt=media&amp;token=0177d9ed-d411-450f-9bae-033ca1f7e928" alt=""><figcaption><p>Custom Meeting Summary Templates data flows</p></figcaption></figure></div>

The diagram above illustrates how custom meeting summaries are generated from a user-defined or account-defined template. The process begins when a template is created and saved in Zoom. At the account level, an administrator can define a custom meeting summary template for organizational use. At the individual level, a user can create a personal meeting summary template based on their own preferences. Once created, the selected template is stored so it can be applied during later summary generation.

As a meeting concludes, Zoom AI can use the meeting’s speech-to-text data to generate a summary that follows the structure and emphasis of the chosen custom template. If the custom template was selected before the meeting summary was generated, Zoom AI applies that template directly when producing the summary. This allows the resulting output to reflect the specific format, sections, or priorities defined in the template rather than only a default summary structure.

If a custom template was not selected before the summary was first generated, Zoom can only apply that template later if the meeting transcript was retained. In that case, Zoom AI can reprocess the retained transcript using the template’s configuration and produce a new summary aligned to that structure. If the transcript was not retained, however, Zoom does not have the underlying transcript available for reprocessing, which means the custom template cannot be applied after the fact.

## Live Voice Translation

<div data-with-frame="true"><figure><img src="https://1175968039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FctBXUMeBy4rtLMmMkKRG%2Fuploads%2FhEoS4i8vNntdOIimBl6g%2F7ca031_FbKGyC4eSZ-mHZ4Ibw-07A_Voice-Translator-Aug-25-update-v3.png?alt=media&amp;token=c5889183-1531-4d96-9455-bd00570140e9" alt=""><figcaption><p>Overview of Live Voice Translation data flows</p></figcaption></figure></div>

The diagram above illustrates how **Live Voice Translations** works by ingesting, the speaker’s native audio through a meeting's Multimedia Router (MMR). That audio is then passed through real-time media streaming (RTMS) to the translation service, where the original speech is processed and translated into the target language. The service then generates a new translated voice audio stream, which is returned through RTMS to the MMR and delivered back into the meeting for participants listening in the selected language.

## Personal Audio Isolation

<div data-with-frame="true"><figure><img src="https://1175968039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FctBXUMeBy4rtLMmMkKRG%2Fuploads%2FiuobcSga2Z6kGJEqFwtO%2Fimage22.png?alt=media&amp;token=387af679-5d1c-4aa0-aa62-9085d334a40b" alt=""><figcaption><p>Overview of how Personal Audio Isolation isolate's a user's voice</p></figcaption></figure></div>

The diagram above illustrates how **Personal Audio Isolation** works by using a voice imprint stored locally on the user’s device to distinguish the user’s speech from surrounding background noise. The process begins when the user records a voice sample through the Personal Audio Isolation feature in the Zoom Workplace app. That recording is used to create a local voice imprint that helps the application recognize the user’s voice characteristics. This voice imprint remains on the local machine and is not transmitted to the Zoom cloud.

When the user later speaks during a meeting in an environment with ambient noise, the Zoom Workplace app uses that locally stored voice imprint to help identify the user’s speech patterns and separate them from surrounding sounds. This allows the application to reduce background noise and isolate the user’s voice more effectively before the audio is sent onward through the meeting flow.

As a result, the audio transmitted to the Zoom cloud is the refined meeting audio with ambient noise filtered out to the extent supported by the feature. The user’s underlying voice imprint itself is not sent to Zoom’s cloud infrastructure. In this way, Personal Audio Isolation operates as a local device-level processing feature that improves audio clarity before the cleaned audio is transmitted into the live Zoom session.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation by asking a question.

Perform an HTTP GET request on the following URL with the `ask` and `goal` query parameters:

```
GET https://library.zoom.com/ai/ai-whitepaper/diagrams.md?ask=<question>&goal=<user_goal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is what the user is ultimately trying to achieve, the reason they need the answer. Sharing it helps GitBook give you a better, more relevant answer. A goal is most helpful when it describes the outcome the user wants rather than restating the question. For example, with `ask=how do I create an API token`, a goal like `automate deployments from our CI pipeline` lets GitBook tailor the answer to that use case.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
