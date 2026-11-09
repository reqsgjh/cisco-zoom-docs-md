> For the complete documentation index, see [llms.txt](https://library.zoom.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://library.zoom.com/advanced-enterprise-services/zoom-node/zoom-node-overview.md).

# Overview

Authored by Jakob Ganschow

### Overview <a href="#id-44zramp4bgy" id="id-44zramp4bgy"></a>

#### <mark style="color:blue;">Zoom Node is a hybrid-service and business continuity solution that brings key Zoom services to your own data centers</mark> <a href="#b3bllktwqftc" id="b3bllktwqftc"></a>

Zoom Node is a hybrid-service and business continuity platform that integrates your data center servers with Zoom’s cloud. With the Zoom Node platform, you deploy Zoom Service Modules (workloads) on your premises, and control them through the Zoom Web portal.

Featuring a cloud-driven deployment model, Zoom Node allows administrators to quickly deploy Zoom workloads to their data centers from Zoom Web Portal. This portal also includes tools for service management, upgrades, log management, performance reporting and troubleshooting.

#### <mark style="color:blue;">Zoom Node is a modular design, where you only deploy the service modules you need</mark> <a href="#pm3z9giol4ur" id="pm3z9giol4ur"></a>

Zoom Node is an all-in-one modular platform that allows companies to manage and deploy multiple hybrid and business continuity services using one common framework. This approach provides significant improvements over existing solutions which only allow standalone deployments of unique workloads, resulting in disparate, inefficient admin deployment and management efforts.

Zoom Node achieves this goal by introducing an integrated turn-key image of the Zoom Node OS and core services. This system image is installed onto enterprise datacenter virtual machines (VMs), transforming them into *Nodes*. Once the Zoom Node software is installed, configured, and registered to the Zoom Node Platform in the cloud, a Node can install Service Modules to provide common Zoom workloads.

Zoom administrators assign Service Modules to Nodes through the Zoom Node dashboard on the web portal, with each Node supporting a maximum of **four** Services Modules. After the administrator selects the Service Module, the Zoom Node Platform pushes the configuration from Zoom’s cloud to the on-premises Node and is automatically installed. Once installation is complete, the service provided by the Service Module is ready for configuration and deployment into the production environment.

The following service modules are currently available:

{% content-ref url="/pages/VibDvwWzJY3iJYd77TKs" %}
[Zoom Meetings Hybrid](/advanced-enterprise-services/zoom-node/zoom-meetings-hybrid.md)
{% endcontent-ref %}

{% content-ref url="/pages/4JPS3oqhBQ7EAWwPpWtO" %}
[Zoom Recording Hybrid](/advanced-enterprise-services/zoom-node/zoom-recording-hybrid.md)
{% endcontent-ref %}

{% content-ref url="/pages/DCanhrKBdhKPNP0J0Y3q" %}
[Zoom Chat Hybrid](/advanced-enterprise-services/zoom-node/zoom-chat-hybrid.md)
{% endcontent-ref %}

{% content-ref url="/pages/nvyHtyKJENTc6yJkC3t9" %}
[Zoom Conference Room Connector Hybrid](/advanced-enterprise-services/zoom-node/zoom-conference-room-connector-hybrid.md)
{% endcontent-ref %}

{% content-ref url="/pages/Nz4NCFDK3QOujGXS6MlZ" %}
[Zoom Phone Local Survivability](/advanced-enterprise-services/zoom-node/zoom-phone-local-survivability.md)
{% endcontent-ref %}

{% content-ref url="/pages/tkcsX8eoPwLhD19XBzz6" %}
[Zoom Meetings & Recording Connectors (On-Premises)](/advanced-enterprise-services/zoom-node/zoom-meetings-and-recording-connectors-on-premises.md)
{% endcontent-ref %}

#### <mark style="color:blue;">Zoom Node is comprised of multiple components</mark> <a href="#id-3ju510895sgb" id="id-3ju510895sgb"></a>

Zoom Node Service Modules generally provide the same capabilities delivered by their Zoom Cloud counterparts. To enable seamless functioning of these modules, Zoom Node provides the following common platform services:\\

* **Secure OS**: A Linux-based Zoom Node image, fully maintained and supported by Zoom via periodic updates.
* **Agent**: A proxy providing communication between the Zoom Node platform and the administrator.
* **Workload Monitoring Relay**: A service that forwards on-premises data to the Cloud Alerting Service.
* **Software Management Client**: A service used to manage module configuration.
* **Debug/Logging Relay**: A service that forwards logging data to the Cloud Logging Console.
* **Real-time Statistics Relay**: A service that forwards on-premises data to the Cloud Analytics Dashboard.
* **Registration Client:** A service that interacts with the Cloud Registration Service.
* **Bootstrap/Debugging Console:** A feature used for management of Zoom Node and Service Module installations.

#### <mark style="color:blue;">Zoom Node includes a feature-rich dashboard</mark> <a href="#id-9bap7tor7k6b" id="id-9bap7tor7k6b"></a>

As a central hub for managing Zoom Node and Service Module deployments, the feature-rich Zoom Node dashboard includes tools for service management, deployments, upgrades, log management, performance reporting, and a robust troubleshooting framework.

#### <mark style="color:blue;">Zoom Node supports end-to-end automated PKI certificate generation (Auto-PKI)</mark> <a href="#d3ek6ieh1ds" id="d3ek6ieh1ds"></a>

Zoom Node includes end-to-end automated public certificate management through DigiCert. All costs for generating and renewing certificates are paid by Zoom, but Zoom does not handle or have access to customer's private keys through this process.

Customers with an existing certificate strategy can choose to generate, renew, and support certificates manually with a certificate authority of their preference, but these costs will not be paid for by Zoom. Customers that intend to use an alternative certificate authority should speak with their account team in advance.

#### <mark style="color:blue;">Zoom Node supports auto-DNS using an account’s Vanity URL</mark> <a href="#id-8e4nieccyxbn" id="id-8e4nieccyxbn"></a>

Zoom Node automatically generates dynamic DNS entries for each server under the \*.zoomonprem.com domain using the host account’s existing vanity URL, e.g. success01.zoomonprem.com.

This convention simplifies firewall management when connecting to Zoom Node deployments used by other Zoom customers. Individual customers will no longer require firewall rules to connect to another Zoom Node customer, but can instead approve the entire zoomonprem.com domain using wildcard values.

#### <mark style="color:blue;">Zoom Node runs on virtual machines</mark> <a href="#ugws32mitvjv" id="ugws32mitvjv"></a>

Zoom Node is designed to run on server-grade hardware, using virtual machines, installed with the hardened Zoom Node operating system image. All services will require static internal IP addresses, with some services requiring public IPs for external connectivity.

The hardware requirements and specifications will be unique to your hybrid deployment goals. Please refer to Zoom Support articles and your account team for more information on identifying your organization’s needs for a hybrid deployment.

#### <mark style="color:blue;">Zoom Node supports managed, automatic updates</mark> <a href="#wge4lm8m1uaq" id="wge4lm8m1uaq"></a>

To ensure potential vulnerabilities are addressed in a timely fashion, the Zoom Node platform supports a robust, managed, automatic update functionality. With this design, admins can configure cloud-based automatic updates, specifying update times on a weekly or monthly basis, configure levels of automation for updates, or postpone updates until a later time.

### Use Cases <a href="#id-2ossapp0avfe" id="id-2ossapp0avfe"></a>

#### <mark style="color:blue;">Zoom Node is designed to address specific requirements</mark> <a href="#id-2ossapp0avfe" id="id-2ossapp0avfe"></a>

Every enterprise has unique requirements when it comes to unified communication services. These needs must be carefully considered before making a decision to deploy a hybrid environment. In most cases, the traditional Zoom cloud configuration is the optimal solution for most companies; however, there are organizations that benefit from hybrid configurations. Organizations should be thorough in considering the implications of establishing and maintaining a hybrid environment.

#### <mark style="color:blue;">When to deploy Zoom Node</mark> <a href="#rz3dq8sqif9" id="rz3dq8sqif9"></a>

Zoom Node modules can be considered when traditional Zoom cloud offerings cannot address the requirements in the following areas:

**Security**

Zoom Node modules can minimize enterprise boundary ingress and egress points, and can secure media traversal by creating an alternative to media proxies, which have inadequate performance and do not support UDP.

**Bandwidth**

Zoom Node modules can reduce bandwidth requirements for Meeting, Webinars, and Events by keeping or redistributing media on-premises.

**Compliance**

Future Zoom Node modules will aim to help enterprises or government organizations adhere to local regulatory requirements. This includes keeping media at-rest and in-transit within country or regional boundaries.

**Survivability**

Zoom Node modules can be used to enable Zoom services to persist during external Internet failures, cloud failures, or natural disasters.

### Deployment Considerations <a href="#id-2dqs4f37xy7x" id="id-2dqs4f37xy7x"></a>

Businesses examining Zoom Node are encouraged to consider the following points:

**Scaling**

Scaling the hardware to support a large number of users in hybrid environments can be costly. Depending on the services deployed, supporting 10,000 users could require between 7-13 Nodes, while supporting 100,000 users may require between 60-120 Nodes. Managing, maintaining, and supporting the hardware and/or hypervisor infrastructure required for Zoom Node also creates additional overhead for any organization and should be accounted for when budgeting hybrid deployments.

**Security**

Zoom Node does not offer additional encryption methods or major security advantages over the native Zoom cloud service, apart from single media ingress/egress point or local log residency. Hybrid deployments also require additional firewall rules and configurations to make Node endpoints available with external services. Network security teams should be mindful of these additional firewall and security requirements when considering deploying hybrid environments.

**VPNs**

Remote employees may require a VPN connection or a split-tunnel configuration to route their meeting traffic to Zoom Node services if desired. This increase in traffic can potentially overwhelm the VPN infrastructure if it cannot handle the additional bandwidth being sent and received. Careful planning is required when combining hybrid services with remote workers and remote network infrastructure.

**Log Sharing**

Hybrid service logs are maintained locally by default, and include data, diagnostics, and other information not available to Zoom for viewing. However, in order to effectively troubleshoot hybrid configurations and quality concerns, hybrid data logs are often required to be shared with Zoom support for troubleshooting purposes. Zoom Node offers a secure log file upload service through the web portal at customer discretion, but uploading these logs can provide service metadata that is otherwise not shared with Zoom in hybrid deployments. This data may include names of participants joining locally, Zoom version number, operating system information, and more.

### Zoom Node Deployment Example <a href="#id-3knmb2qzxacg" id="id-3knmb2qzxacg"></a>

Fundamentally, each Zoom Node can support up to **four** Service Modules per machine, with the option to add additional Nodes for scaling needs. Depending on the service module being deployed, businesses should ensure they have sufficient virtual machines deployed to meet the demand.

For example, if a national company is deploying a Zoom Node service module—like Zoom Meetings Hybrid—across their data centers in New York, Chicago, and Los Angeles, the admin should first deploy a sufficient number of Zoom Nodes to meet their demand within each respective region.

Each primary Zoom Meetings Hybrid service module—known as the Hybrid Multimedia Router (HMMR)—supports up to 400 users at one time. Consequently, if there are 4,000 users within the New York office, the account admin may want to deploy at least **10** Meetings Hybrid Modules to meet maximum demand (400 users per module x 10 modules = 4,000 supported users). Further, because each Zoom Node supports four service modules, the account admin will require at least **three** Zoom Node machines (3 machines x 4 service modules each = 12 total service modules).

Next, the admin should ensure the Chicago and Los Angeles offices also meet their supported targets, and then stand up the necessary number of virtual machines and install the Zoom Node OS. The following image provides an example of the deployment across each location.

<figure><img src="https://1175968039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FctBXUMeBy4rtLMmMkKRG%2Fuploads%2Fgit-blob-28c1843bf1ac9b52123957615c0bc09728ae6249%2F12.png?alt=media" alt="Diagram depicting Zoom Nodes across multiple data centers" width="563"><figcaption><p>Diagram depicting Zoom Nodes across multiple data centers</p></figcaption></figure>

After all Zoom Node virtual machines are configured, the admin must deploy the required service modules onto each machine. To do this, the admin navigates to the Node dashboard, selects the intended machine(s), and then selects the service modules to deploy. After selecting the appropriate modules, the Zoom Node web platform pushes and installs the selected modules to the respective Nodes. After the installation is complete, the hybrid services are ready for use, as seen in the following image.

<figure><img src="https://1175968039-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FctBXUMeBy4rtLMmMkKRG%2Fuploads%2Fgit-blob-c426729ad3aa9562c04ef554e9aff007ab487173%2F13.png?alt=media" alt="Diagram depicting Zoom Nodes with deployed service modules" width="563"><figcaption><p>Diagram depicting Zoom Nodes with deployed service modules</p></figcaption></figure>

{% hint style="warning" %}
**Heads Up**

There are additional configuration steps not addressed in this example, including IP configuration, assigning hostnames, and more. These steps have been excluded for the sake of brevity and illustration.\\

If you have questions about the service modules required for a product or a deployment, speak with your Zoom account team.
{% endhint %}


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation by asking a question.

Perform an HTTP GET request on the following URL with the `ask` and `goal` query parameters:

```
GET https://library.zoom.com/advanced-enterprise-services/zoom-node/zoom-node-overview.md?ask=<question>&goal=<user_goal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is what the user is ultimately trying to achieve, the reason they need the answer. Sharing it helps GitBook give you a better, more relevant answer. A goal is most helpful when it describes the outcome the user wants rather than restating the question. For example, with `ask=how do I create an API token`, a goal like `automate deployments from our CI pipeline` lets GitBook tailor the answer to that use case.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
