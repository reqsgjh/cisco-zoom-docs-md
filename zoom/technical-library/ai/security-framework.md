> For the complete documentation index, see [llms.txt](https://library.zoom.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://library.zoom.com/ai/ai-whitepaper/security-framework.md).

# Security Framework

An overview of the Zoom AI security framework

## **Security Framework**

Zoom’s secure software development lifecycle (SDLC) is a set of practices and processes designed to integrate security into each phase of the software development lifecycle. Zoom’s secure software development controls are assessed by independent audit firms as indicated in Zoom’s security certifications and attestations, which are available to customers on [Zoom’s Trust Center](https://www.zoom.com/en/trust/legal-compliance/?ampDeviceId=bb815bd9-9fc2-43c5-8323-028b2011295a\&ampSessionId=1777925804236). Zoom AI features follow Zoom’s standard secure SDLC process, which includes the following sections.

## **Design Review**

Zoom’s Engineering Security team is engaged during the design phase when a feature is being conceptualized so that key security controls can be built into the requirements. Security design reviews, which include threat analysis, are performed to identify potential threats and mitigations. Zoom maintains vulnerability remediation standards governing the remediation or mitigation of security vulnerabilities identified during the security design review.

## **Code Review**

Peer code reviews are a key element of Zoom’s secure software development lifecycle and are enforced in Zoom’s software development platform. In addition to peer code reviews, high-risk areas identified during the security design review require secure code reviews. Where appropriate manual testing is also performed on a release by release basis.

## **Static Analysis Testing**

Zoom utilizes static analysis security testing (SAST) tools to scan its source code for coding errors and common security vulnerabilities, including Open Web Application Security Project’s (OWASP) Top 10 and National Vulnerability Database (NVD). Zoom maintains vulnerability remediation standards governing the remediation or mitigation of security vulnerabilities identified through static analysis testing.

## **Dynamic Analysis Testing**

Zoom utilizes dynamic analysis security testing (DAST) tools to identify common security vulnerabilities, including OWASP’s Top 10 and NVD. Zoom maintains vulnerability remediation standards governing the remediation or mitigation of security vulnerabilities identified through dynamic analysis testing.

## **Third-Party Code Reviews**

Where open source software (OSS) is used, the OSS package must undergo Zoom’s third-party code review process, which includes a set of OSS evaluation criteria and scanning for common security vulnerabilities. Zoom maintains vulnerability remediation standards governing the remediation or mitigation of security vulnerabilities identified through third-party OSS scanning tools.

## **Deployment**

Security approval is required for the deployment of new products and features, including Zoom AI features. Zoom has a dedicated Release Security Assurance function responsible for scanning Zoom client builds prior to release. The final Zoom client build scans are designed to identify potential vulnerabilities or malicious content, and the build is digitally signed to maintain its integrity and authenticity.

## **Generative AI Model Security**

In addition to the steps outlined in Zoom’s secure SDLC above, models hosted by Zoom are subject to security reviews to assess security threats specific to generative AI models. The generative AI model review includes commonly known LLM model vulnerabilities, in line with OWASP’s Top 10 for LLMs and other secure AI frameworks. Vulnerabilities identified in the generative AI security reviews must be remediated in accordance with Zoom’s vulnerability remediation standards.

Zoom’s third-party subprocessors are subject to security assessments on at least an annual basis as part of Zoom’s third-party risk management program. Zoom’s third-party risk management controls are assessed by independent audit firms as indicated in Zoom’s security certifications and attestations, which are available to customers on [Zoom’s Trust Center](https://www.zoom.com/en/trust/legal-compliance/?ampDeviceId=bb815bd9-9fc2-43c5-8323-028b2011295a\&ampSessionId=1777925804236).

## **Security Assessments**

Zoom has a dedicated offensive security team that performs ongoing vulnerability research and red team exercises across Zoom’s platform, including for Zoom AI features. In addition to Zoom’s dedicated offensive security team, penetration tests are performed by an independent third party on at least an annual basis.

## **Vulnerability Disclosure Program**

Zoom believes that the independent security research community can provide key contributions to the security of Zoom’s products. Zoom maintains a [vulnerability disclosure program](https://www.zoom.com/en/trust/vulnerability-disclosure/?ampDeviceId=bb815bd9-9fc2-43c5-8323-028b2011295a\&ampSessionId=1777925804236) as well as a Bug Bounty program through HackerOne that incentivizes security researchers to responsibly report potential security vulnerabilities so Zoom can fix them and keep its users safe.

## **Compliance Certifications**

Zoom’s AI features adhere to the same security and compliance requirements as the primary Zoom products within which they are incorporated and key Zoom AI features in Zoom Workplace (previously named AI Companion) are ISO 27001, ISO 27701, and ISO 27017/18 certified and included within the scope of Zoom’s SOC 2 report, available on [Zoom’s Trust Center](https://www.zoom.com/en/trust/legal-compliance/?ampDeviceId=bb815bd9-9fc2-43c5-8323-028b2011295a\&ampSessionId=1777925804236).


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation by asking a question.

Perform an HTTP GET request on the following URL with the `ask` and `goal` query parameters:

```
GET https://library.zoom.com/ai/ai-whitepaper/security-framework.md?ask=<question>&goal=<user_goal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is what the user is ultimately trying to achieve, the reason they need the answer. Sharing it helps GitBook give you a better, more relevant answer. A goal is most helpful when it describes the outcome the user wants rather than restating the question. For example, with `ask=how do I create an API token`, a goal like `automate deployments from our CI pipeline` lets GitBook tailor the answer to that use case.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
