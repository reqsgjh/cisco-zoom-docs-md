Cisco Catalyst Center Platform Overview
=======================================

[Cisco Catalyst Center](https://www.cisco.com/site/us/en/products/networking/catalyst-center/index.html) simplifies campus networking by providing automated device deployment and configuration, policy-based management, dynamic network insights and monitoring, and advanced analytics. Catalyst Center enables network administrators to efficiently manage and optimize their network infrastructure, ensuring consistent policies and compliance, while using the UI or API and Integrations.

[Catalyst Center platform](https://developer.cisco.com/catalyst-center/) offers opportunities to integrate API operations for custom integrations and automations, allowing you to tailor network operations to meet specific business needs. By integrating with existing Cisco tools and third-party applications, you can extend the functionality of Catalyst Center and create innovative solutions that enhance network capabilities.

> **Note**: Cisco DNA Center is now Catalyst Center. During this transition, you might encounter both names in different materials, but they refer to the same product.

What can you do with Catalyst Center API?
-----------------------------------------

* Use REST Intent API for policy-driven network operations with standard REST methods and JSON.
* Access 1,000+ API operations for device lifecycle, provisioning, software management, compliance, and inventory.
* Connect with IT Service Management (ITSM) and other systems via API, webhooks, and event notifications.
* Subscribe to event notifications for proactive network monitoring and external system integration.
* Explore API, test requests interactively, and generate sample code in multiple languages to speed development.
* Use synchronous calls for immediate data and asynchronous for scheduled operations with status tracking.
* Efficiently manage large datasets with bulk API operations for scalability.
* Implement Role-Based Access Control (RBAC) and backward compatibility for secure, scalable automation.
* Use Python SDK, Ansible collections, and Terraform providers for repeatable network management.
* Access documentation, OpenAPI specs, sample code, Sandboxes, and community support on Cisco DevNet.

Intent API (Northbound)
-----------------------

The Intent API is a *Northbound* REST API that exposes specific capabilities of the Catalyst Center platform.
The Intent API provides policy-based abstraction of business intent, allowing focus on an outcome rather than struggling with individual mechanisms steps.
The RESTful Catalyst Center Intent API uses HTTPS verbs (GET, POST, PUT, and DELETE) with JSON structures to discover and control the network.
The Intent API organizes hierarchically into functional 'domains' and 'subdomains' of service.

Events and Notifications (Eastbound)
------------------------------------

The Catalyst Center platform enables setting up notification handlers for specific events, including Assurance and Automation (Software Image Management) events. This allows external systems to respond automatically to these events—for example, triggering a software upgrade when devices are out of compliance. Also, internal Catalyst Center events can generate notifications, such as customized Assurance events for ITSM incidents, facilitating integration with IT workflows and automation.

Integration API (Westbound)
---------------------------

Integration capabilities are part of Westbound interfaces. To meet the need to scale and accelerate operations in modern data centers, IT operators require intelligent, end-to-end work flows built with OpenAPI. The Catalyst Center platform provides mechanisms for integrating Assurance workflows and data with the third-party **IT Service Management (ITSM)** solutions.

**IT Service Management (ITSM)** minimizes handoffs, reduces duplication of issues, and optimizes processes by integrating the Catalyst Center platform into incident-management, change-management, and problem-management systems. It also integrates the Catalyst Center platform into approval and pre-approval chains, and it links the Catalyst Center platform with formal change and maintenance window schedules.

The platform also integrates with Reporting and Analytics capabilities for capacity planning, asset management, compliance control, and auditing. The Catalyst Center platform boosts IT efficiency and automation by integrating seamlessly with other IT systems through RESTful API.

The Catalyst Center platform supports the [IT4IT™ Reference Architecture](https://www.opengroup.org/it4it), including the standards for events, incidents, problems, and request for changes. If you are using an ITSM system that supports this reference architecture, then the Catalyst Center platform can integrate with your system.