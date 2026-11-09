> For the complete documentation index, see [llms.txt](https://library.zoom.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://library.zoom.com/business-services/zoom-contact-center/zoom-customer-experience/overview/zoom-contact-center-architecture.md).

# Architecture

Zoom Contact Center is designed with an active-active architecture for reliability and resiliency.

The following sections provide a general overview of Zoom Contact Center’s architecture.

### Zoom Contact Center Data Center SIP Zones

In an active-active architecture, resiliency and redundancy are key. To support the voice channel and telephony needs, each Zoom Contact Center data center features two identical, interconnected SIP zones equipped with dedicated hardware and services for independent resiliency and sustainability.

During normal operations, a load balancer evenly distributes calls between both SIP zones within a data center. Within each SIP zone, calls are equitably distributed among a cluster of call switches, which are responsible for various functions such as call routing, setup, and teardown. From the call switches, calls connect to a Session Border Controller (SBC) within each zone, which either connects to Zoom's underlying network of providers or the customer-provided carrier (BYOC-P) for PSTN routing until the call reaches its final destination.

Within this framework, each integral piece of architecture—i.e., SBCs, load balancers, and call switches—is supplemented with redundant hardware on standby for resiliency. In the event that one SIP zone experiences a service-impacting event, a call’s active media, signaling, and registration will failover to the other zone for uninterrupted service. Further, because Zoom strives for no greater than 50% capacity within each SIP zone at any given time, in the event of a service-impacting event within a SIP zone, calls should failover to the opposing zone without issue until standard operations resume.

The following diagram illustrates a SIP zone’s active-active architecture design at a high level:

<div data-with-frame="true"><figure><img src="https://1175968039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FctBXUMeBy4rtLMmMkKRG%2Fuploads%2Fq98WhB6gPiO2XHt8t7wK%2Fimage4.png?alt=media&amp;token=0cb2610a-853b-4a55-a6a3-b862eb5634fe" alt=""><figcaption><p>Overview of a SIP Zone's Active-Active Architecture</p></figcaption></figure></div>

### Zoom Contact Center Data Centers At Large

From a physical perspective, Zoom's presence in data centers are located within highly secure colocation facilities with physical security, redundant power and cooling systems, and access to leading carrier-neutral internet service providers (ISPs) and peering partners.

From a technological perspective, Zoom’s presence in data centers are built with fault-tolerant architecture, including full redundancy and rapid failover capabilities from a primary data center to a secondary data center, to enhance reliability and minimize downtime across all contact center channels.

In the unlikely event of a complete data center outage or service-impacting event, Zoom Contact Center media, signaling, and registration information may be temporarily lost, requiring a convergence on the standby, secondary data center. In such cases, voice channel sessions will re-register with the secondary data center, directing all incoming calls through the location's backup carrier. Subsequently, all new calls will be processed through the secondary data center and its relevant active-active zones until service is fully restored. Following the restoration of service, a maintenance window will be employed to return operations to normal at the appropriate primary data center.

The following image illustrates Zoom’s data center redundancy design at a high level:

<div data-with-frame="true"><figure><img src="https://1175968039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FctBXUMeBy4rtLMmMkKRG%2Fuploads%2FHwgqOR49uylTiWcQMbHk%2Fimage.png?alt=media&amp;token=cc462744-8890-4cd4-b3e2-b0efdbb282e1" alt=""><figcaption><p>Overview of Zoom's data center redundancy</p></figcaption></figure></div>

Readers are encouraged to refer to Zoom’s [Status](https://status.zoom.us/) and [Uptime](https://uptime.zoom.us/) sites for additional information on service availability.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation by asking a question.

Perform an HTTP GET request on the following URL with the `ask` and `goal` query parameters:

```
GET https://library.zoom.com/business-services/zoom-contact-center/zoom-customer-experience/overview/zoom-contact-center-architecture.md?ask=<question>&goal=<user_goal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is what the user is ultimately trying to achieve, the reason they need the answer. Sharing it helps GitBook give you a better, more relevant answer. A goal is most helpful when it describes the outcome the user wants rather than restating the question. For example, with `ask=how do I create an API token`, a goal like `automate deployments from our CI pipeline` lets GitBook tailor the answer to that use case.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
