# Juniper Trainer

This repository is a collection of tools to help study for Juniper certifications.

## Slash Commands

The following slash commands are available:

*   `/quizme`: Starts a quiz with multiple choice questions.
    *   `question_style`: The style of the questions. Can be `multiple choice` or `flashcard`. Defaults to `multiple choice`.
    *   `topic`: The topic of the quiz. See the available topics below.
    *   `num_questions`: The number of questions to ask. Defaults to 10.
*   `/run_bandit`: Runs a bandit scan on the specified path.
    *   `path`: The path to run the scan on. Defaults to `.`.
*   `/run_duckduckgo`: Performs a DuckDuckGo search.
    *   `query`: The query to search for. Defaults to `Python programming`.
*   `/generate_gns3_config`: Generates GNS3 configuration files for a given topic.
    *   `topic`: The topic to generate the configuration for. Currently only `OSPF` is supported.

### Available Quiz Topics

*   Chapter_1_Initial_Configuration_and_Platform_Troubleshooting
*   Chapter_2_Interface_Configuration_and_Testing
*   Chapter_3_OSPF_Configuration_and_Testing
*   Chapter_4_IS-IS_Configuration_and_Testing
*   Chapter_5_BGP_Configuration_and_Testing
*   Chapter_6_Routing_Policies
*   Chapter_7_Class_of_Service
*   Chapter_8_Multicast
*   Chapter_9_MPLS
*   Chapter_10_System_Logging_Archiving_and_SNMP
*   Chapter_11_Putting_It_All_Together
