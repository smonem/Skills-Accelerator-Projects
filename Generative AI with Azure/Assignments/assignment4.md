# Assignment: Structure of Prompt Flow

### Part 1: Fundamentals of Prompt Flow

**Application Task:**

#### Use Case: Technical Support and Troubleshooting Chatbot  
The chatbot will help users diagnose and resolve technical issues related to software, hardware, or network configurations. It will provide step-by-step troubleshooting guidance, recommend fixes, and escalate unresolved issues.  

#### Inputs, Prompts, and Outputs

*Inputs*
- User query (ex: "My Wi-Fi keeps disconnecting.")
- Device details (OS version, hardware model)
- Error messages

*Prompt*
- “Analyze the user's technical issue based on the input and provide troubleshooting steps. If the issue is unclear, ask follow-up questions to gather more details. Given the gathered data, provide the most likely solution with step-by-step instructions. If the issue remains unresolved, suggest contacting support and provide relevant ticket details.” 

*Outputs*
- Troubleshooting steps ("Restart the router, check cable connections, update drivers.")
- Follow-up questions ("Are other devices affected?")
- Escalation notice ("Directing you to IT support.")


#### Integrations & APIs

*LLM Model*
- GPT-4, Claude, or an open-source model, fine-tuned if domain-specific expertise is needed for specialized technologies or support 

*APIs*

- Knowledge Base: Pulls information from a technical documentation database 
- Device Diagnostics: Fetches system logs, error reports from user system for analysis 
- Ticketing System:  Escalates unresolved issues to IT

### Part 2: Building LLM Applications

1. Prompt Flow

In my prototype content generation tool, the *input node* allows the user to input a topic for the blog post. This is achieved using a text input widget, where users can type in keywords or a phrase that specifies the topic they want the generated blog to explore. The *model node* leverages a general-purpose LLM to generate the blog post draft based on the user's selected topic. The input node passes the desired details to the model node / LLM, which includes a dynamic prompt that instructs the model to generate the blog post based on the topic. The *output node* displays the final generated draft to the user. The result is shown in a text display widget, which allows users to review the draft, edit it, or refine the topic for further iteration if needed.

2. Reflection

While Azure's visual editor makes it easy to get started with creating AI tool, I still found that there was a bit of a learning curve in navigating the interface and ensuring that the tool worked as intended. The first challenge I faced was understanding how to structure the flow and connect the nodes properly. Azure’s interface is intuitive but requires some practice to understand how to link input, model, and output nodes correctly. Once I became familiar with the interface, I assembled the prototype quickly, but ensuring the tool produced a useful output, the qualtities I wanted being those of relevance, detail, and accuracy, required multiple iterations of the tool. To address generated responses being either too general or lacking depth, I refined the prompt I supplied, adjusting the wording and adding more specific instructions for the model to follow. Aside from prompt engineering, I also used Azure’s features to further fine-tune the model’s hyperparameters and settings. This allowed me to enhance the model’s ability to produce high-quality and useful blog drafts. Although I faced setbacks, the adjustments I made improved the tool’s output, ultimately resulting in a functional prototype content generation tool.

### Part 3: Monitoring and Maintaining LLM Applications

Monitoring key metrics like latency and error rates is highly important for optimizing the user experience of any LLM application. High latency can frustrate users by slowing response times, while a high error rate may indicate issues with model performance or infrastructure. By tracking these metrics, we can proactively identify bottlenecks and improve system reliability. Azure's Prompt Flow provides various tools that can be used to monitor response times and detect anomalies. Azure AI monitoring can also provide real-time alerts for spikes in errors or slow responses, which would allow me to troubleshoot and resolve issues promptly, preventing possible downtime. Additionally, I could leverage these analytics to analyze trends over time and optimize resource allocation for the applications. For more granular insights, I could also use tools to help detect deviations in model behavior. By continuously monitoring, analyzing, and fine-tuning performance, we can ensure that LLM applications remains responsive and reliable, leading to a seamless and trouble-free experience for all users.