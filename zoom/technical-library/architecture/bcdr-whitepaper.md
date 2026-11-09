> For the complete documentation index, see [llms.txt](https://library.zoom.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://library.zoom.com/admin-corner/architecture-and-design/bcdr-whitepaper.md).

# Business Continuity and Disaster Recovery Whitepaper

## **Introduction**

Zoom delivers AI-first Unified Communications as a Service (UCaaS) and Contact Center as a Service (CCaaS) through a single, integrated platform. This document details the innovations and architecture behind Zoom’s best-in-class services and products, explaining how we deliver a consistent, secure, and manageable experience for end users and IT across UCaaS and CCaaS.

## **Built from Experience**

Zoom’s cloud-first vision helps organizations move beyond the cost and complexity of legacy on-premises systems. Rather than bolting features onto aging stacks, we’ve invested in full-stack engineering across clients, media services, and room systems to optimize end-to-end quality, resiliency, and usability as one cohesive platform—anchored by a single-client strategy with a common codebase across platforms that takes advantage of each OS’s native UX.

That cloud-first approach shows up in the Zoom Workplace app: a single, modern application that gives users centralized access to Meetings, Chat, Phone, Contact Center, Events, Webinars, Rooms, Whiteboard, Canvas, and more. Access is governed by licensing, so IT can turn products and features on or off without deploying a patchwork of separate installers or managing conflicting client versions.

For IT, the model reduces overhead—fewer servers to buy, rack, and patch; fewer bespoke integrations to maintain; and no need for entire teams dedicated to keeping on-prem infrastructure running. Capacity, updates, and security improvements are delivered from the cloud, so admins can focus on policy, adoption, and outcomes rather than maintenance.

## Real-Time Media Architecture and Resiliency

The following sections discuss Zoom’s design approach to enable a best-in-class real-time media experience.

### Zoom Meetings, Webinars, and Events

The foundation of our architecture is an intelligent transport layer that selects the best path based on real network conditions and policies. UDP is used when available, with seamless fallback to TCP/TLS (including HTTPS/443) in more restrictive environments. Screen sharing uses Reliable UDP for smooth motion whenever possible, with automatic fallback if needed. When connecting to a meeting, webinar, or event, the Zoom Workplace app is steered by geolocation to the nearest available resources to minimize latency. Where organizational policies or performance require, traffic can traverse Zoom’s global backbone via dedicated links to different data centers.

<div data-with-frame="true"><figure><img src="https://1175968039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FctBXUMeBy4rtLMmMkKRG%2Fuploads%2FnFxtmNHVYydGwOrYTGFv%2F226B9D5D-5C3B-422D-91F5-A157C60A67BD.png?alt=media&amp;token=ee2ef06d-f83a-490c-9fba-e52f4dbe29b3" alt="Diagram detailing how the Zoom App maintains active-active connectivity to failover data centers, zone controllers, and multi-media routers." width="563"><figcaption><p>An Overview of Zoom's Meeting, Webinar, and Events active-active architecture and design.</p></figcaption></figure></div>

The next layer is a reactive quality-of-service layer that adapts to real-time network and device conditions. It monitors bandwidth, packet loss, latency, and jitter, and also collects local CPU usage, memory, and network I/O. These signals inform the upper layers to take the appropriate adaptive actions to maintain quality and reliability.

Zoom’s custom, adaptive codec at the session layer is tuned for real-time performance. Surrounding algorithms continuously optimize frame rate and resolution to match device and network conditions. To provide the best possible experience as conditions allow, Zoom uses multiple simultaneous streams, and the Zoom Workplace app dynamically selects the most appropriate layer. Thanks to efficient compression, sessions remain usable with packet loss up to \~45%; in those cases, audio is prioritized over video to keep conversations clear. The multi-stream approach also adjusts bandwidth to each participant’s ability to send and receive audio and video.

Zoom’s distributed conferencing layer uses subscription-based switching without server-side transcoding or mixing. Traditional services often transcode and mix streams, adding CPU and memory overhead; our switching approach is designed to reduce resource use and scale efficiently. Participants are routed by geolocation to the nearest data center and assigned to the least-loaded server; when attendees are co-located, they can be grouped on the same server for efficiency. The architecture supports flexible on-premises and hybrid deployments and provides cascaded traffic paths for large enterprises.

The Meeting Server is our MMR (multi-media router), and each MMR is grouped in a “Meeting Zone.” Zone Controllers manage all of the MMRs and report their status to the Global Cloud Controller for each Meeting Zone. The Meeting Zones are duplicated for each data center with the exact same architecture, and we can easily add more zones on the fly for added capacity in each region. The three layers (the MMR, Zoom Controller, and Global Cloud Controller) are used to balance resources in different locations. If just two participants are in a meeting, Zoom can utilize peer-to-peer connections for excellent speed and reliability. All of this allows Zoom to maintain meeting services availability of 99.9% uptime and provide a dependable video conferencing experience.

### Zoom Phone

Zoom Phone was built in the cloud and for the cloud, using the proven audio quality adaptations already available in our Zoom Meetings and Webinars products. Zoom’s architecture has redundancy and resiliency built in, resulting in a highly-available solution that can scale to meet even the largest organization’s needs.

Zoom Phone utilizes intelligent transport mechanisms for reliable connectivity across diverse network environments. For media, it uses SRTP over UDP when available, with seamless fallback to TCP/TLS, along with adaptive bitrate and packet-loss mitigation to preserve audio quality under poor conditions. For connectivity, calls route to the nearest available SIP Zone to minimize latency, with automatic failover across data centers when needed.

<div data-with-frame="true"><figure><img src="https://1175968039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FctBXUMeBy4rtLMmMkKRG%2Fuploads%2Fc7qphWNnzClbmFTFUBJt%2F39E3A87C-8C89-457C-BDA5-305F26CDFA27.png?alt=media&amp;token=44860c84-cd37-450d-a10e-846c73b8ca48" alt="Diagram showing a Zoom Phone device connected to a primary data center, with a secondary connection to an additional data center for failover events." width="563"><figcaption><p>Zoom Phone's active-active architecture</p></figcaption></figure></div>

Zoom has redundant Session Border Controllers (SBCs) in each of its data centers that secure client and carrier communications. These carrier-grade SBCs facilitate easy access for a broad range of organizations, from the smallest of customers to global enterprises. Load Balancers redirect SIP-based communications to Zoom’s Call Switches to evenly distribute the call volume. This distribution enables a smooth experience for users, even during peak registration and busy call hours.

Call Switches are the core call control of Zoom Phone. These scalable components not only support base PBX functionality, but also facilitate telemetry data to the Zoom Phone Dashboard and enable features like elevating Zoom Phone calls to Zoom meetings.

<div data-with-frame="true"><figure><img src="https://1175968039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FctBXUMeBy4rtLMmMkKRG%2Fuploads%2FzpgEaRrGK5oT6NQfmFRp%2FB9547F0B-E921-4EFD-B16D-B03FD320F31B.png?alt=media&amp;token=e10984d8-d5e4-4ee2-a9e2-82e612353d5f" alt="A diagram showing the active-active architecture for hardware and SIP zones hosted within a data center" width="563"><figcaption><p>Active-active architecture for hardware and SIP zones hosted within a data center</p></figcaption></figure></div>

The Zoom Workplace app leverages proprietary logic to monitor the app’s bandwidth, packet loss, latency, and jitter, while also collecting the app’s CPU usage, memory, and network I/O. This technology actively monitors calls and makes real-time adjustments to overcome poor network conditions to provide superior call quality and reliability for various network environments and different devices.

The Zoom Phone Dashboard captures real-time and historical quality of service data, as well as usage and adoption metrics, call logs, and metrics related to nomadic emergency services. Zoom automatically rates each call with a Mean Opinion Score (MOS), allowing IT administrators to track the performance of all calls traversing the network and isolate potential network-related issues.<br>

### Zoom Contact Center

Similar to Zoom Phone, Zoom Contact Center’s active-active architecture helps provide resiliency and redundancy across its omni-channel environment. Building on proven architectures from Zoom Meetings and Phone services, Contact Center seamlessly integrates real-time communication capabilities with web functionality, creating an intuitive interface that benefits both your team of agents and your customers.

Each data center features two identical, interconnected Session Initiation Protocol (SIP) zones. SIP zones allow voice calls to be made and received over the internet, and each zone is equipped with dedicated hardware and services for independent sustainability. Within a data center, a load balancer evenly distributes calls between both SIP zones. Calls are distributed among a cluster of call switches, which are responsible for various functions such as call routing, setup, and teardown.

From the call switches, calls connect to an SBC within each zone, which either connects to Zoom’s underlying network of providers or a customer-provided carrier for PSTN routing until the call reaches its final destination. SBCs, load balancers, and call switches are supplemented with redundant hardware on standby for resiliency.

Voice in Zoom Contact Center benefits from the same client adaptation and transport behavior as Zoom Phone—using UDP when available with fallback to TCP/TLS—so audio stays clear even on constrained networks. For video and digital channels, the service leverages Zoom’s real-time media backbone and cloud resiliency for consistent quality and failover.

#### Cobrowse

Zoom Contact Center’s Cobrowse service runs on infrastructure that is separate from the core Zoom Contact Center service. When a session begins, the software development kit (SDK) establishes a persistent WebSocket connection to the Cobrowsing Hub Server (CHS) for bidirectional communication, with traffic routed by geolocation to the nearest available data center to reduce latency. The service uses a stateless, distributed architecture with dynamic load balancing across CHS nodes to support elastic scaling across cloud, hybrid, and on-premises deployment models.

To help maintain session continuity, the SDK automatically reconnects to healthy CHS nodes if connectivity is interrupted and can fail over across data centers with minimal disruption. Combined with continuous health monitoring and Zoom’s broader active-active resiliency approach, this architecture is designed to provide reliable, scalable cobrowsing performance for enterprise environments.

<div data-with-frame="true"><figure><img src="https://1175968039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FctBXUMeBy4rtLMmMkKRG%2Fuploads%2FqgrjZ7zNepHGpbyeVtdB%2F2bbf10_uubksQ_iRI6klG25EenQ5w_260403-Cobrowse-SDK-Diagram-1-v2.png?alt=media&amp;token=a734884a-1888-47f3-a03f-f7d896eda153" alt="" width="563"><figcaption><p>Active-active architecture for Cobrowse SDK zones hosted within a data center</p></figcaption></figure></div>

## **Zoom Node for Hybrid & On-Premises Deployments**

[Zoom Node](https://library.zoom.com/advanced-enterprise-services/zoom-node/zoom-node-explainer) is a cloud-managed, hybrid platform that links your data center resources with Zoom’s cloud, enabling you to deploy Zoom Service Modules (workloads) on-premises and manage them from the Zoom web portal. Two modules stand out for resiliency: Zoom Meetings Hybrid and Zoom Phone Local Survivability (ZPLS).

[Zoom Meetings Hybrid](https://library.zoom.com/advanced-enterprise-services/zoom-node/zoom-node-explainer/zoom-meetings-hybrid) routes real-time media for internal participants through your local Node while signaling, admin, and policy remain in the Zoom cloud, and it includes a local survivability option if Zoom data centers become unreachable. Internal users get low-latency paths and reduced internet egress, while external participants can join over the cloud as usual. Accounts can also add Recording Connector for local capture when required, with automatic cloud failover if local capacity isn’t available.

<div data-with-frame="true"><figure><img src="https://1175968039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FctBXUMeBy4rtLMmMkKRG%2Fuploads%2FC0GcdeoEhnCKSkpoLPeD%2FC5C3B116-A2C7-46B9-963B-5BDA9FCAFB8B.png?alt=media&amp;token=751a33a1-7c01-4ed3-b6f0-81a036a0887c" alt="Zoom Meetings Hybrid Module shows how users in a local network connect to the Hybrid MMR, cascading to the cloud." width="563"><figcaption><p>Zoom Meetings Hybrid Module shows how users in a local<br>network connect to the Hybrid MMR, cascading to the cloud.</p></figcaption></figure></div>

[Zoom Phone Local Survivability](https://library.zoom.com/advanced-enterprise-services/zoom-node/zoom-node-explainer/zoom-phone-local-survivability) (ZPLS) keeps core calling available at a site if the WAN or provider path goes down. Phones register locally, internal extension calling continues, and, when configured, critical outbound calling can be maintained through an on-premises PSTN path. When connectivity returns, service automatically resumes normal cloud operation.

<div data-with-frame="true"><figure><img src="https://1175968039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FctBXUMeBy4rtLMmMkKRG%2Fuploads%2FUsoAHP6CgWryBUz2JjOz%2FC3998DFD-40AC-4CD0-A76D-32AC5898BE41.png?alt=media&amp;token=7e0b4233-6ab2-4409-801f-961728bb6814" alt="Diagram showing how the ZPLS module supports PSTN, intra-site, and cross-site survivability." width="563"><figcaption><p>Zoom Phone Local Surviability supports multiple failback scenarios for PSTN and<br>cross-site connectivity in the event of a service-impacting event.</p></figcaption></figure></div>

## **Global Distributed Data Centers and Redundancy**

Zoom has brokers and communications servers distributed among multiple interconnected data centers across the globe. We are constantly evaluating our data centers and Internet service providers (ISPs) to optimize performance for our customers in regards to bandwidth, latency, and disaster recovery isolation. Our data centers are situated in secure co-location facilities that are ISP carrier neutral and provide physical security, redundant power, and simultaneous access to top-tier ISPs and peering partners. We also have certain deployments on public cloud providers where regional or capacity requirements warrant. Our co-location facilities are built with fault-tolerant architecture with full redundancy and rapid failover capability. Zoom dynamically load balances the communications servers to automatically move new sessions to the data center that has the best response time.

These facilities are engineered for resilience at the physical layer as well. Each colocation facility is built with N+1 redundancy and a full set of environmental controls intended to keep the facility operational through component failures and physical hazards:

* Temperature and humidity controls
* Power systems that are fully redundant and scaled to accommodate component failure
* Resilient emergency lighting
* Fire protection
* Water damage protection

Data centers include uninterruptible power supply (UPS) redundancy models such as N, N+1, or 2N, and generator redundancy using an N+1 design, with power maintenance and testing handled by the applicable data center provider. Where Zoom uses AWS to host portions of its cloud infrastructure, the existence and operation of AWS controls are reviewed annually by Zoom's Security team through external service auditor reports; any exceptions identified are discussed with AWS and, where they present a risk to Zoom's systems or data, escalated to Zoom management.

<div data-with-frame="true"><figure><img src="https://1175968039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FctBXUMeBy4rtLMmMkKRG%2Fuploads%2FI74U4hZkRltHhURZmGZz%2FDB57E664-C00F-4E57-B8CD-A2A98C9FBBFD.png?alt=media&amp;token=4f3a6c81-c583-4f68-9d65-3e0443d2d9eb" alt="" width="563"><figcaption><p>Zoom Commercial Data Center Locations Across the Globe (November, 2024)</p></figcaption></figure></div>

## **Capacity**

Zoom maintains 50% excess capacity in all aspects of our infrastructure to accommodate our growing business and to meet peak usage requirements. We are confident in our ability to provide service and scale based on our current and future customer needs.

## **Business Continuity and Disaster Recovery**

Reliability under normal conditions is only part of the story; equally important is how the platform behaves when something goes wrong. Disruptions — such as natural disasters, power or facility failures, cyber incidents, network outages, and hardware faults — are an inevitable reality for any global service, and Zoom's resilience comes from how it prepares for, withstands, and recovers from these events. That resilience rests on four distinct but connected layers, each operating at a different point before, during, and after a disruption:

* **High Availability** — the architectural layer that reduces the likelihood and impact of failures before they occur, by eliminating single points of failure.
* **Business Continuity** — the operational layer that keeps essential business functions running when a disruption does occur.
* **Disaster Recovery** — the restoration layer that brings affected technology systems and services back to normal operation after a disruptive event.
* **Testing** — the validation layer that confirms these practices work and surfaces lessons for continuous improvement.

These layers build on one another: high availability lowers how often recovery is needed, business continuity governs what stays running while it happens, disaster recovery restores what was affected, and testing validates the whole. The architecture described throughout this document — active-active data centers, geolocation-based routing, automatic failover, and N+1 deployment — is the high-availability layer in practice. The sections below describe the remaining three.

### High Availability

High availability refers to system and service design intended to support continuous operation and minimal downtime, and it is engineered into Zoom's systems with the goal of minimizing or eliminating critical points of failure. Services are designed to withstand full data center outages, and automated processes move traffic away from an affected area when a failure occurs. Core applications are deployed to an N+1 standard, so that if a data center becomes unavailable, sufficient capacity remains to load-balance traffic to the surviving sites. This design philosophy spans the full set of systems a communications platform depends on — redundant facilities, telephony infrastructure, internet and LAN connectivity, security infrastructure, relational database systems, mass storage, backups, hardware, and the associated capacity-management and maintenance practices — so that the failure of any single component, system, or facility does not result in a loss of service.

### Business Continuity

Zoom's business continuity planning is designed to minimize the impact of disruptions on operations, protect assets, and maintain essential services for customers and stakeholders. It identifies the business functions that must be preserved or restored first, the people, technology, vendors, and workplace resources those functions depend on, and the potential impact if those dependencies are disrupted. This gives Zoom a structured basis for coordinating response and recovery when normal operations are affected, particularly when multiple functions or resources require attention at the same time.

Underpinning this planning is a Business Impact Analysis (BIA), the systematic process Zoom uses to identify and evaluate the potential effects of disruptions on critical business functions. Zoom performs a BIA for critical functions at least annually, or upon a significant change to a critical business process. The analysis covers four key components:

1. **Identification of critical business functions** — documenting the key processes essential to Zoom's operations and determining the dependencies and interdependencies between them.
2. **Impact assessment** — evaluating the potential impact of disruptions on each function, considering financial loss, operational downtime, legal and regulatory implications, and reputational harm.
3. **Resource requirements** — identifying the personnel, technology, facilities, and third-party services needed to support recovery, and assessing their availability and adequacy.
4. **Prioritization of recovery efforts** — sequencing the recovery of critical functions based on their impact and the established recovery objectives, so the most critical functions are restored first.

### Disaster Recovery

Zoom regularly validates its disaster recovery capabilities through annual testing across its products. The company maintains a formal, documented Disaster Recovery Plan (DRP) that defines procedures for restoring critical systems and services following a disruption, including recovery strategies, roles and responsibilities, and communication protocols. Zoom's DRP is designed to address various disaster scenarios that may include one or more of the following: power outages, network connectivity loss, hardware failures, natural disasters, and other disruptive events, up to and including total facility failure. Information security standards governing disaster recovery are documented, approved, communicated, and reviewed at least annually.

Rather than maintaining a dedicated hot recovery site for cloud services, Zoom relies on redundant architecture, multi-location data centers, and several cloud providers including AWS, OCI, and GCP to support continuity. At the platform level, the recovery pattern differs by service type:

* **Web cluster and non-real-time communications** use AWS high-availability infrastructure in a multi-region active-active configuration, rely on DNS records to enable failover between data centers, and include multiple components with replication capabilities within each data center.
* **Regional data centers and real-time communications** operate in an active-active configuration across geographically dispersed Tier 3-and-above providers, with redundant and resilient components and connectivity within each regional data center, diverse carriers supporting connectivity, and failover between regions requiring reconnection.

Zoom's documented recovery strategies include region failover, which shifts traffic or services away from an affected region, and rollback through blue-green deployment, which returns services to a previously known-good environment or deployment state to recover from software or deployment-related issues.

These strategies are measured against defined recovery objectives. The recovery time objective (RTO) — the target time to restore service after a disruption — has a goal of under five minutes. The recovery point objective (RPO) — the target amount of tolerable data loss — has a goal of no data loss, supported by replication of cloud-stored data across multiple availability zones. These objectives inform Zoom's design and testing rather than functioning as service guarantees.

Effective data backup and restoration is a core component of this approach, protecting critical information so it can be restored in the event of a disruption to maintain business continuity. Zoom does not externally share its complete disaster recovery plan or detailed test results, as those materials contain internal and sensitive confidential business information. Refer to [Zoom's Trust Center](https://www.zoom.com/en/trust/legal-compliance/) for more information on publicly available documentation.&#x20;

### Testing

Zoom validates its recovery practices through annual tabletop and failover testing performed by third-party auditors. This testing confirms that response and recovery processes work as intended, identifies gaps, and supports continuous improvement through lessons learned. Testing has spanned a broad set of products and service areas across the platform, including Zoom Meetings, Zoom Phone, Zoom Contact Center, Zoom Virtual Agent, Zoom Rooms, Zoom Events, Whiteboard, Workspace Reservation, and the RTC and Telephony Gateways, among others. Combined with the redundant, active-active architecture described throughout this document, this layered approach is designed to keep Zoom's services available and recoverable across a wide range of disruptive conditions.

## **Conclusion**

Zoom’s reliability is supported by a layered architecture that combines cloud-first service design, adaptive media routing, redundant global infrastructure, capacity planning, and formal business continuity and disaster recovery practices. Across Meetings, Phone, Contact Center, Zoom Node, global data centers, and related services, Zoom’s platform is designed to support consistent communications across diverse networks, regions, devices, and deployment models.

The same design principles that support day-to-day service quality also support resilience at scale. Active-active architecture, intelligent routing, adaptive transport, redundant facilities, recovery planning, backup practices, and regular testing work together to help maintain essential services and support recovery when operational events occur.

For customers and IT teams, this approach provides a platform designed for dependable communication, operational continuity, and manageable enterprise deployment across UCaaS and CCaaS environments.

*Authored by Jakob Ganschow and Sam Azimipour*


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation by asking a question.

Perform an HTTP GET request on the following URL with the `ask` and `goal` query parameters:

```
GET https://library.zoom.com/admin-corner/architecture-and-design/bcdr-whitepaper.md?ask=<question>&goal=<user_goal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is what the user is ultimately trying to achieve, the reason they need the answer. Sharing it helps GitBook give you a better, more relevant answer. A goal is most helpful when it describes the outcome the user wants rather than restating the question. For example, with `ask=how do I create an API token`, a goal like `automate deployments from our CI pipeline` lets GitBook tailor the answer to that use case.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
