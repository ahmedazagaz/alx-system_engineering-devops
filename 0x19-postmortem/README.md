### Postmortem: Microsoft and CrowdStrike Web Stack Outage

**Issue Summary:**

- **Duration:** August 15, 2024, 09:00 - 12:30 UTC
- **Impact:** The outage affected Microsoft’s web services integrated with CrowdStrike’s threat detection platform. Users experienced significant delays in accessing Microsoft services, with up to 70% of users facing slow response times or connection failures. Critical operations for many organizations were disrupted.

**Timeline:**

- **09:00 UTC** - Initial reports of service degradation from users and internal monitoring alerts.
- **09:10 UTC** - Engineers identified high latency and intermittent failures in Microsoft’s web services.
- **09:20 UTC** - Investigation began into potential issues with the web stack and third-party integrations, including CrowdStrike.
- **09:45 UTC** - Misleading assumption that the issue was due to a DNS configuration error led to unnecessary reconfigurations.
- **10:00 UTC** - Escalated to the network and security teams for further analysis.
- **10:30 UTC** - Discovery that the issue was related to a CrowdStrike API rate limit being exceeded, causing service interruptions.
- **11:00 UTC** - CrowdStrike engineering team notified and confirmed that API throttling limits were being reached due to an unexpected surge in traffic.
- **12:00 UTC** - Rate limits were adjusted, and traffic was normalized.
- **12:30 UTC** - Services fully restored and operational.

**Root Cause and Resolution:**

- **Cause:** The outage was caused by CrowdStrike’s API rate limiting being exceeded. This occurred due to an unexpected surge in traffic, which overwhelmed the API’s capacity to handle requests. This issue was exacerbated by a lack of proper handling for burst traffic scenarios in the integration layer between Microsoft’s web services and CrowdStrike’s threat detection system.

- **Resolution:** The immediate resolution involved increasing the API rate limits in CrowdStrike’s configuration to handle the surge in traffic. Additionally, Microsoft implemented temporary request throttling on their end to prevent future rate limit breaches. Long-term, an improved traffic management strategy and more robust error handling were put in place.

**Corrective and Preventative Measures:**

- **Improvements:**
  - Implement better traffic management and load balancing strategies to handle unexpected surges.
  - Enhance monitoring and alerting systems to detect potential rate limit breaches earlier.
  - Improve communication protocols with third-party service providers to anticipate and mitigate integration issues.

- **Tasks:**
  - **Patch CrowdStrike API Rate Limits:** Update API configuration to handle higher traffic volumes and configure dynamic rate limiting.
  - **Update Monitoring Systems:** Enhance monitoring tools to detect and alert on unusual traffic patterns and rate limit issues.
  - **Review Integration Handling:** Audit and optimize the integration layer between Microsoft services and CrowdStrike for better handling of burst traffic.
  - **Improve Documentation:** Ensure comprehensive documentation for handling API rate limits and integration issues.

This postmortem provides a concise overview of the outage, its impact, and the steps taken to resolve the issue while offering actionable insights to prevent similar issues in the future.
