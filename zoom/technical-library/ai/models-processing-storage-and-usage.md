> For the complete documentation index, see [llms.txt](https://library.zoom.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://library.zoom.com/ai/ai-whitepaper/models-processing-storage-and-usage.md).

# Models, Processing, Storage, and Usage

An overview of Zoom's AI model providers, service approaches, and data handling

Zoom's artificial intelligence architecture provides organizations with three distinct deployment models, each engineered to balance AI capability requirements with specific organizational security, compliance, and operational preferences. Understanding these deployment models enables administrators and decision-makers to select the optimal AI implementation that aligns with their business goals.

The following diagram provides an overview of Zoom's AI Deployment Service Models, detailed in the sections below. Diagrams across the AI Whitepaper default to the federated approach, but you can mentally substitute the relevant dataflows with your selected deployment model. For instance, customers interested in ZMO (Zoom-Hosted Models Only) can disregard the outbound Third-Party Model connections.

<div data-with-frame="true"><figure><img src="https://1175968039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FctBXUMeBy4rtLMmMkKRG%2Fuploads%2FtIZct0TTpcdjEAJX2Z5l%2FZoom-AI-Service-Models.png?alt=media&amp;token=293c8c54-5a8a-4fd2-b71a-fea9a66f9dfa" alt=""><figcaption><p>An overview of Zoom's AI Service Models: Federated, ZM+, and ZMO</p></figcaption></figure></div>

## Zoom's Federated Approach

The Federated Approach: Maximum Flexibility Through Multiple AI Model Providers\
The Federated Approach represents Zoom's most flexible AI deployment, designed to deliver maximum functionality by integrating multiple leading AI model providers. This deployment approach utilizes communication pathways between Zoom's platform and multiple best-in-class AI model providers, creating an intelligent routing system that dynamically selects the optimal AI model for each specific task requirement.

<div data-with-frame="true"><figure><img src="https://1175968039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FctBXUMeBy4rtLMmMkKRG%2Fuploads%2FKEYDQV41igiVfqtgerLz%2FServiceModel-Federated-v2.png?alt=media&amp;token=af3b1ae9-5f9f-4caf-8f35-0eff15778d87" alt="" width="375"><figcaption><p>Diagram illustrating Zoom's federated approach</p></figcaption></figure></div>

### **AI Models**

Zoom’s federated approach to AI utilizes multiple AI models and AI services to provide generative AI-powered features. Below is a summary of the models used by Zoom to provide high-quality results in response to users’ interactions with Zoom’s product.

* Zoom-hosted models
* Anthropic models
* OpenAI models
* Google Gemini models

Zoom also uses other model providers for particular generative features, including:

* Zoom uses Perplexity to provide certain web content search results.
* Zoom uses ElevenLabs to generate audio for the Zoom Clips AI Avatars feature.
* Zoom uses AWS (Amazon Rekognition) to provide moderation services on the generated images for the Virtual Background Generation feature.
* Zoom uses Azure Speech Translation API to translate live audio.

Changes to the models used in federation can occur at any time to improve the service or resolve issues and outages. In addition, maintenance of the models hosted by Zoom may include changes to their capabilities and responses.

This deployment approach provides organizations with:<br>

* **Broadest Feature Support**: Access to the widest range of available Zoom AI-powered features without functional limitations.
* **Intelligent Workload Distribution**: Automatic routing of AI requests to the most suitable provider based on task characteristics and performance optimization.
* **Maximum Flexibility**: Ability to leverage specialized AI capabilities from multiple providers within a unified Zoom interface
* **Scalability Optimization**: Dynamic load balancing across multiple AI services designed to provide consistent performance during peak usage periods

#### <mark style="color:blue;">**Federated Implementation Considerations**</mark>

Organizations using the Federated Approach should evaluate data routing implications, as AI processing may occur across multiple third-party environments. This model is optimal for enterprises prioritizing maximum AI functionality and feature availability while maintaining standard enterprise security protocols.

## Additional Deployment Options

In addition to the Federated Approach, customers using AI in Zoom Workplace have two additional deployment options available that offer different approaches to data processing and third-party models. Customers can reach out to Zoom support to understand their default deployment and to select their preferred alternate deployment option based upon account and feature availability.

### Zoom-Hosted Models Plus (ZM+)

#### <mark style="color:blue;">Third-Party Model Access Through Amazon Bedrock</mark>

The Zoom-Hosted Models Plus (ZM+) deployment represents a balanced approach that combines extensive AI capabilities without third-party AI model provider processing. Through Amazon Bedrock’s managed AI service infrastructure, Zoom provides access to instances of third-party models through Zoom’s existing cloud services provider Amazon Web Service (AWS). This approach enhances data control for organizations while preserving access to diverse AI capabilities. (Currently available in the US, EU, AU.)

<div data-with-frame="true"><figure><img src="https://1175968039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FctBXUMeBy4rtLMmMkKRG%2Fuploads%2FlaxZFKLYpLqAF3BQwUOH%2FZM%2B-Diagram.png?alt=media&amp;token=4d49d7c3-abd7-47e4-b4c7-cd516b464426" alt="" width="375"><figcaption><p>Diagram illustrating Zoom's ZM+ approach</p></figcaption></figure></div>

#### <mark style="color:blue;">**ZM+ Technical Architecture and Service Delivery Approach**</mark>

Through the Amazon Bedrock integration, Zoom maintains instances of select AI models, creating a hybrid approach that delivers:<br>

* **Zoom-Managed Model Instances**: Data is processed on Zoom-managed instances where information is not sent to third-party AI model providers.
* **Multi-Model Support**: Access to third-party AI models, though with potentially different model versions or configurations compared to direct federated access.
* **Data Control**: Processing occurs within Amazon's enterprise infrastructure, and is controlled by Zoom.

While ZM+ provides substantial AI capabilities, organizations should anticipate that some features available in the Federated Approach may have limited availability or modified functionality with ZM+.

#### <mark style="color:blue;">**ZM+ Implementation Considerations**</mark>

This deployment approach serves enterprises requiring enhanced data control while maintaining multi-model optimization and access to advanced AI capabilities.

### Zoom-Hosted Models Only: Models Through Proprietary AI Infrastructure

The Zoom-Hosted Models Only deployment represents the most restrictive AI implementation option, exclusively utilizing models hosted within Zoom's dedicated infrastructure.

<div data-with-frame="true"><figure><img src="https://1175968039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FctBXUMeBy4rtLMmMkKRG%2Fuploads%2FAf9dxUGBFsIRPGRGLCvw%2FZMO.png?alt=media&amp;token=5668e150-5538-44a8-a4e1-e8b807431fcc" alt="" width="188"><figcaption><p>Diagram illustrating Zoom's<br>Zoom-Hosted Models Only approach</p></figcaption></figure></div>

#### <mark style="color:blue;">**ZMO Technical Infrastructure and Service Limitations**</mark>

This deployment approach operates through:

* **Zoom-Hosted Models Utilization**: AI feature processing conducted through Zoom's hosted models.
* **Dedicated Infrastructure**: Model processing occurs within Zoom's controlled environment.
* **Simplified Data Flow**: Eliminates external AI model provider data routing, creating the most straightforward architecture.

Organizations selecting this deployment model should anticipate:

* **Limited Feature Set**: This model may result in a reduction of available AI features compared to Federated and ZM+ approaches.
* **Reduced Capability Scope**: AI functionality limited to capabilities supported by Zoom hosted models.
* **Performance Variations**: Response quality and task handling may differ significantly from multi-model approaches, particularly for specialized use cases.

#### <mark style="color:blue;">**ZMO Implementation Considerations**</mark>

The Zoom-Hosted Models Only (ZMO) deployment serves organizations with stringent data control requirements, regulatory compliance obligations, or security policies that prohibit third-party AI model provider utilization. While providing the least flexible AI experience when compared to other deployment models, this approach offers simplified compliance documentation while maintaining the benefits of modern AI.

## Generative AI Approaches Overview

The following tables summarize the differences between Zoom’s three generative AI service models.

| Deployment Model                  | Architecture & AI Access                          | Feature Scope                                          | Ideal Use Cases                                                                     |
| --------------------------------- | ------------------------------------------------- | ------------------------------------------------------ | ----------------------------------------------------------------------------------- |
| **Federated Approach**            | Direct connections to multiple AI model providers | Broadest feature access without functional limitations | Organizations prioritizing maximum AI functionality and feature availability        |
| **Zoom-Hosted Models+ (ZM+)**     | Amazon Bedrock and Zoom’s self-hosted models      | Potential feature limitations                          | Privacy-conscious enterprises requiring advanced AI with additional data governance |
| **Zoom-Hosted Models Only (ZMO)** | Zoom's self-hosted models                         | Potential feature limitations                          | Organizations with stringent compliance or security requirements                    |

## **Regional Availability**

Zoom AI features are subject to limitations in certain regions that are not supported by our third-party AI model providers, as well as for customers in specific industry verticals. For customers with accounts specifically hosted in a region outside of the US, supported AI features are made available using ZM+ or ZMO. For customers hosted in the EU or AU, Zoom uses ZM+ (or customers can choose ZMO) to support account data residency preferences for available features. Customers hosted in other regions can also access available AI features through ZMO. Furthermore, if the underlying product is not available in a particular region, related AI features will not be available.

Refer to Zoom’s [AI Regional Availability Table](/ai/ai-whitepaper/feature-availability.md) for more information on feature availability by region and service model.

{% hint style="info" %}
**Note**

The linked table above provides a summary of the current regional availability and supported model deployment options of key Zoom AI features in Zoom Workplace, Zoom Webinars and Events, and Zoom Contact Center.
{% endhint %}

This table is not exhaustive and may not include all available features. Zoom may update regional availability and deployment approaches for features at its discretion. Access to and use of these features will also depend on other factors such as subscription plan, license assignment, and administrator settings.

## **Data Usage**

Zoom does not use any customer audio, video, chat, screen sharing, attachments, or other communications-like customer content (such as poll results, whiteboard, and reactions) to train Zoom’s or its third-party artificial intelligence models.

Zoom AI features must use certain content to provide the service.

## **Data Access**

Consistent with Zoom’s [Privacy Statement](https://www.zoom.com/en/trust/privacy/privacy-statement/?ampDeviceId=bb815bd9-9fc2-43c5-8323-028b2011295a\&ampSessionId=1777925804236), Zoom employees may not access or use customer content, including meeting, webinar, messaging, or email content (specifically, audio, video, files, in-meeting whiteboards, messaging, or email content), any content generated or shared as part of other collaborative features (such as out-of-meeting whiteboards), or content generated by AI features, unless authorized by the account owner or administrator of the account hosting the Zoom product or service where the customer content was generated, or as required for legal, safety, security, or support reasons.

Zoom's access to customer data and content used to provide Zoom AI features is role-based and restricted based on least privilege, in accordance with Zoom's access control policies and standards. Controls are in place to prevent Zoom employees from accessing customer content as described above, unless authorized by the account owner or administrator of the account hosting the Zoom product or service where the customer content was generated, or as required for legal, safety, security, or support reasons. Zoom's access to customer data and content is logged and monitored for suspicious activity or unauthorized access. Zoom's data access controls are assessed by independent audit firms where indicated in our security certifications and attestations, which are available to our customers on [Zoom's Trust Center](https://zoom.us/trust/legal-compliance).

## **Data Processing and Storage Locations**

Zoom processes and stores data based on the hosted data center region and applicable settings of the host, owner or user, as applicable. See also the [Managing Data & Storage location](https://support.zoom.com/hc/en/article?id=zm_kb\&sysparm_article=KB0066473) support article for more information on storage locations.\
\
When interacting with external participants, content (e.g., chats, meeting transcripts) exchanged between accounts may be processed according to the external account settings.

See “Additional Deployment Options” and “Regional Availability” above for more information.

## **Data Retention**

Zoom stores and retains customer content and personal data for as long as required to engage in the uses described in its [Privacy Statement](https://www.zoom.com/en/trust/privacy/privacy-statement/?ampDeviceId=bb815bd9-9fc2-43c5-8323-028b2011295a\&ampSessionId=1777925804236), unless a longer retention period is required by applicable law, including for reasons such as trust and safety. In the context of data retention and processing, “trust and safety purposes” refers to measures taken to protect the safety and integrity of a service and its users. This involves retaining certain data for a period of time to help prevent abuse and misuse. Additional information on Zoom’s Trust and Safety processes may be found in [Zoom's Safety Center](https://safety.zoom.us/?ampDeviceId=bb815bd9-9fc2-43c5-8323-028b2011295a\&ampSessionId=1777925804236). Content that would ordinarily be retained by the associated Zoom service is stored in accordance with the retention period for that service. Customers may also set custom retention periods for certain content.

With respect to third-party generative AI model providers used as part of Zoom AI’s federated approach, Zoom has zero data retention policies in place, which provide that they do not retain customer content, with limited exceptions for trust and safety purposes, such as to detect and report CSAM.

### Zero Data Retention for Meeting Summary

#### <mark style="color:blue;">Zero Data Retention for Zoom Meeting Summary allows meeting summaries to be generated without retaining the transcript</mark>

Administrators can **disable** and **lock** the Meeting transcript setting on the account or group-level. When configured in this manner, Zoom uses temporary speech-to-text data, optical character recognition (OCR), and in-meeting chat data for the purpose of generating a meeting summary and does not retain a persistent transcript of the meeting conversation, unless the in-meeting chat is otherwise saved by an attendee. Alternatively, administrators can choose to enable the Meeting transcript setting, but set the transcript retention duration to zero (0) days. When configured in this manner, users can still request to view the transcript in real time in the Transcript panel during the meeting.

In both cases, once summary generation is successful, the temporary speech-to-text data, OCR, and in-meeting chat data is discarded and cannot later be recovered, re-obtained, or reused. If the initial attempt to generate a summary is unsuccessful, Zoom uses the temporary speech-to-text, OCR, and in-meeting chat data to allow additional attempts to complete the summary. If summary generation still does not succeed, the speech-to-text, OCR, and in-meeting chat data is discarded.

Because no persistent transcript is retained under these configurations, meeting summaries generated in this manner cannot later be reprocessed, regenerated, or used with a different or custom summary template. These options are intended for organizations that prioritize minimizing transcript retention over preserving the ability to perform later transcript-based reprocessing.

Zoom Meetings features that require access to meeting transcripts such as My Notes and archival will be impacted when transcript generation is disabled, as these features depend on the availability of transcripts. Additionally, if a cloud recording feature is enabled, it can generate and retain a meeting transcript as part of the cloud recording files independent of this configuration. Additional transcript settings for My Notes, archival, and cloud recordings will continue to be managed in separate locations in the web portal. These settings also do not prevent participants or third parties from independently creating, storing, or retaining separate transcript cop

Refer to Zoom’s support center for more information on [allowing users to retain transcripts generated with meeting summary](https://support.zoom.com/hc/en/article?id=zm_kb\&sysparm_article=KB0076631) or [accessing meeting transcripts](https://support.zoom.com/hc/en/article?id=zm_kb\&sysparm_article=KB0076632).

## **Third-Party Sub-Processors**

As part of Zoom’s federated approach to AI, artificial intelligence models from third parties, such as Anthropic and OpenAI, may be used for certain Zoom AI features alongside Zoom’s artificial intelligence models to provide high-quality results. Zoom also uses other model providers for particular features, discussed above.\
\
Zoom requires its [sub-processors](https://www.zoom.com/en/trust/subprocessors/) to satisfy obligations equivalent to those outlined in Zoom’s Data Processing Addendum. Zoom’s sub-processors are subject to security assessments on at least an annual basis as part of Zoom’s third-party risk management program. Zoom’s third-party risk management controls are assessed by independent audit firms in many of its security certifications and attestations, which are available to customers on [Zoom’s Trust Center](https://www.zoom.com/en/trust/legal-compliance/).


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation by asking a question.

Perform an HTTP GET request on the following URL with the `ask` and `goal` query parameters:

```
GET https://library.zoom.com/ai/ai-whitepaper/models-processing-storage-and-usage.md?ask=<question>&goal=<user_goal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is what the user is ultimately trying to achieve, the reason they need the answer. Sharing it helps GitBook give you a better, more relevant answer. A goal is most helpful when it describes the outcome the user wants rather than restating the question. For example, with `ask=how do I create an API token`, a goal like `automate deployments from our CI pipeline` lets GitBook tailor the answer to that use case.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
