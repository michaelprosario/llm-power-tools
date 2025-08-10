START search and content
Title: Semantic Kernel Tools - Visual Studio Marketplace
URL: https://marketplace.visualstudio.com/items?itemName=ms-semantic-kernel.semantic-kernel
ID: https://marketplace.visualstudio.com/items?itemName=ms-semantic-kernel.semantic-kernel
Score: None
Published Date: 2025-04-30T07:08:04.000Z
Author: 
Image: https://ms-semantic-kernel.gallerycdn.vsassets.io/extensions/ms-semantic-kernel/semantic-kernel/0.12.1/1741867232712/Microsoft.VisualStudio.Services.Icons.Default
Favicon: None
Extras: None
Subpages: None
Text: The Semantic Kernel Tools help developers to write semantic plugins for the [Semantic Kernel](https://github.com/microsoft/semantic-kernel).

## Create a Semantic Plugin

1. Once you have installed the Semantic Kernel Tools extension you will see a new **Semantic Kernel** option in the activity bar
 - We recommend you clone the [semantic-kernel](https://github.com/microsoft/semantic-kernel) repository and open this in your VS Code workspace
2. Click the **Semantic Kernel** icon to open Semantic Kernel Functions view
3. Click the "Add Semantic Plugin" icon in the Semantic Kernel Functions view title bar
4. You will be prompted to select a folder
 - This will be the location of the [Plugin](https://github.com/microsoft/semantic-kernel/blob/main/docs/SKILLS.md) which will contain your new Semantic Function
 - Create a new folder called `MyPlugin` 1 in this directory \\semantic-kernel\\samples\\plugins
 - Select this new folder as your Plugin folder
5. You will be prompted for a function name, enter `MyFunction` 1
6. You will be prompted for a function description2
7. A new prompt text file will be automatically created for your new function
8. You can now enter your prompt. More information on [how to write semantic plugins in Semantic Kernel](https://learn.microsoft.com/en-us/semantic-kernel/howto/semanticfunctions).

**1** The name of the plugin folder and function name can contain only latin letters, 0-9 digits, and underscore.

**2** The function description is required.

## Execute a Semantic Function

First you must configure an AI endpoint to be used by the Semantic Kernel

1. Open the Command Palette i.e., View -> Command Palette or Ctrl+Shift+P
2. If you have access to an Azure subscription that contains the Azure OpenAI resource you want to use:
 - Type "Add Azure OpenAI Endpoint" and you will be prompted for the following information:
 - Endpoint type, select "completion"
 - Allow the extension to sign in to Azure Portal
 - Select the subscription to use
 - Select the resource group which contains the Azure OpenAI resource
 - Select the Azure OpenAI resource
 - Select the Azure OpenAI model
3. If you have the details of an Azure OpenAI endpoint that you want to use
 - Type "Add AI Endpoint" and you will be prompted for the following information:
 - Endpoint type, select "completion"
 - Completion label, the default of "Completion" is fine
 - Completion AI Service, select `AzureOpenAI`
 - Completion deployment or model id e.g., `gpt-4`
 - Completion endpoint URI e.g., [https://contoso-openai.azure.com/](https://contoso-openai.azure.com/)
 - Completion endpoint API key (this will be stored in VS Code secure storage)
4. If you have the details of an OpenAI endpoint that you want to use
 - Type "Add AI Endpoint" and you will be prompted for the following information:
 - Endpoint type, select "completion"
 - Completion label, the default of "Completion" is fine
 - Completion AI Service, select `OpenAI`
 - Completion deployment or model id e.g., `gpt-4`
 - Completion endpoint API key (this will be stored in VS Code secure storage)

Once you have a AI endpoint configured proceed as follows:

1. Select the semantic function you want to execute
2. Select the "Run Function" icon which is shown in the Functions view
 - You will be prompted to enter any arguments the semantic function requires
3. The response will be displayed in the Output view in the "Semantic Kernel" section

## Troubleshooting

### Enabling Trace Level Logs

You can enable trace level logging for the Semantic Kernel using the following steps:

1. Open settings (Ctrl + ,)
2. Type “Semantic Kernel”
3. Select Semantic Kernel Tools -> Configuration
4. Change the log level to “Trace”
5. Repeat the steps to execute a semantic function and this time you should see trace level debugging of the semantic kernel execution

Below is a list of possible errors you might receive and details on how to address them.

### Check Developer Tools Console

You can check the developer tools console to get more detailed information if errors occur:

1. Open Help -> Toggle Developer Tools
2. Select the 'Console' tab

### Errors creating a Prompt

- `Unable to create function prompt file for `
 - An error occurred creating the `skprompt.txt` file for a new semantic function. Check you can create new folders and files in the location specified for the semantic plugin.
- `Function already exists. Found function prompt file: `
 - A `skprompt.txt` file already exists for the semantic function you are trying to create. Switch to the explorer view to find the conflicting file.
- `Unable to create function configuration file for `
 - An error occurred creating the `config.json` file for a new semantic function. Check you can create new folders and files in the location specified for the semantic plugin.
- `Configuration file for already exists. Found function config file: `
 - A `config.json` file already exists for the semantic function you are trying to create. Switch to the explorer view to find the conflicting file.

### Errors configuring an AI Endpoint

- `Unable to find any subscriptions. Please log in with a user account that has access to a subscription where OpenAI resources have been deployed.`
 - The user account you specified to use when logging in to Microsoft does not have access to any subscriptions. Please try again with a different account.
- `Unable to find any resource groups. Please log in with a user account that has access to a subscription where OpenAI resources have been deployed.`
 - The user account you specified to use when logging in to Microsoft does not have access to any resource groups in the subscription you selected. Please try again with a different account or a different subscription.
- `Unable to find any OpenAI resources. Please log in with a user account that has access to a subscription where OpenAI resources have been deployed.`
 - The user account you specified to use when logging in to Microsoft does not have access to any Azure OpenAI resources in the resource group you selected. Please try again with a different account or a different resource group.
- `Unable to find any OpenAI model deployments. Please log in with a user account that has access to a subscription where OpenAI model deployments have been deployed.`
 - The user account you specified to use when logging in to Microsoft does not have access to any deployment models in the Azure OpenAI resource you selected. Please try again with a different account or a different Azure OpenAI resource.
- `Unable to access the Azure OpenAI account. Please log in with a user account that has access to an Azure OpenAI account.`
 - The user account you specified to use when logging in to Microsoft does not have access to the Azure OpenAI account in the Azure OpenAI resource you selected. Please try again with a different account or a different Azure OpenAI resource.
- `Unable to access the Azure OpenAI account keys. Please log in with a user account that has access to an Azure OpenAI account.`
 - The user account you specified to use when logging in to Microsoft does not have access to the Azure OpenAI account keys in the Azure OpenAI resource you selected. Please try again with a different account or a different Azure OpenAI resource.
- `Settings does not contain a valid AI completion endpoint configuration. Please run the "Add Azure OpenAI Endpoint" or "Add AI Endpoint" command to configure a valid endpoint.`
 - You have not configured an AI endpoint. Please refer to the first part of the [Execute a Semantic Function](http://marketplace.visualstudio.com/marketplace.visualstudio.com#execute-a-semantic-function) section above.
- `Tokenization logic is not available.`
 - Tokenization is only available for known models e.g., `gpt-4`. If you are using an unknown AI model then token counts cannot be computed.
- `Setting has invaid type, expected "string". Fix in JSON.`
 - The `semantic-kernel.completionEndpoint` may have been incorrectly set to `null`. Open the command palette (Ctrl+Shift+P) and select "Open User Settings (JSON)". Remove the line containing `semantic-kernel.completionEndpoint: null`.

### Errors executing a Prompt

- `ModelNotAvailable – unable to fetch the list of model deployments from Azure (Unauthorized)`

 - This failure happens when calling the Azure OpenAI REST API. Check the AzureOpenAI resource you are using is correctly configured.
- `Service not found: '__SK_DEFAULT' text completion service not available`
\- This failure happens if you execute a semantic function using an image generation model and the semantic function references another function which depends on a text completion service. Currently only a single AI service is supported when executing semantic functions.


### Using Semantic Kernel Tools with Azure API Management

For information on configuring Azure API Management please refer to [Protect your Azure OpenAI API keys with Azure API Management](https://learn.microsoft.com/en-us/semantic-kernel/deploy/use-ai-apis-with-api-management)

Instructions to test the Semantic Kernel Tools with your APIM deployment are as follows:

#### Configure AI Endpoint

1. Open the Command Palette (Ctrl+Shift+P)
2. Execute the “Add AI Endpoint” command
3. Select “AzureOpenAI” as the service type
4. Enter valid deployment name
5. Enter “https://apim...azure-api.net/” as the endpoint URI
6. Enter and empty string as the key (if you have an existing key please delete this)
7. You should get a message “Successfully configured AI endpoint: ”

1. Open Settings (Ctrl+,)
2. Search for "Semantic Kernel"
3. Select "Completion Configuration"
4. Enter the "Completion Header Name" (this will be "Ocp-Apim-Subscription-Key")
5. Enter the "Completion Header Value" (this will be "")

#### Test Function Execution

1. Switch to the Semantic Kernel view
2. Open a Function
3. Click the “Debug Function” action
4. You will be prompted to enter any required parameters
5. Next you will get a message stating “The extension “Semantic Kernel Tools” wants to sign in using Microsoft”, click the Allow button
6. This trigger the flow to authenticate against the APIM endpoint
7. A browser window will open and you can authenticate
8. Once you have authenticated the function execution will proceed and the response form the AI will be displayed in the Output view
Highlights: None
Highlight Scores: None
Summary: None

Title: Plugins in Semantic Kernel - Microsoft Learn
URL: https://learn.microsoft.com/en-us/semantic-kernel/concepts/plugins/
ID: https://learn.microsoft.com/en-us/semantic-kernel/concepts/plugins/
Score: None
Published Date: 2024-06-24T00:00:00.000Z
Author: sophialagerkranspandey
Image: https://learn.microsoft.com/en-us/media/open-graph-image.png
Favicon: None
Extras: None
Subpages: None
Text: Table of contents Exit editor mode

Ask LearnAsk LearnFocus mode

Table of contents [Read in English](https://learn.microsoft.com/learn.microsoft.com) AddAdd to plan [Edit](https://github.com/MicrosoftDocs/semantic-kernel-docs/blob/main/semantic-kernel/concepts/plugins/index.md)

#### Share via

[Facebook](https://learn.microsoft.com/learn.microsoft.com) [x.com](https://learn.microsoft.com/learn.microsoft.com) [LinkedIn](https://learn.microsoft.com/learn.microsoft.com) [Email](https://learn.microsoft.com/learn.microsoft.com) Print

Note

Access to this page requires authorization. You can try [signing in](https://learn.microsoft.com/learn.microsoft.com) or changing directories.

Access to this page requires authorization. You can try changing directories.

# What is a Plugin?

- 2024-12-10

Feedback

Plugins are a key component of Semantic Kernel. If you have already used plugins from ChatGPT or Copilot extensions in Microsoft 365, you’re already familiar with them. With plugins, you can encapsulate your existing APIs into a collection that can be used by an AI. This allows you to give your AI the ability to perform actions that it wouldn’t be able to do otherwise.

Behind the scenes, Semantic Kernel leverages [function calling](https://platform.openai.com/docs/guides/function-calling), a native feature of most of the latest LLMs to allow LLMs, to perform [planning](https://learn.microsoft.com/planning) and to invoke your APIs. With function calling, LLMs can request (i.e., call) a particular function. Semantic Kernel then marshals the request to the appropriate function in your codebase and returns the results back to the LLM so the LLM can generate a final response.

![Semantic Kernel Plugin](https://learn.microsoft.com/media/designed-for-modular-extensibility-vertical.png)

Not all AI SDKs have an analogous concept to plugins (most just have functions or tools). In enterprise scenarios, however, plugins are valuable because they encapsulate a set of functionality that mirrors how enterprise developers already develop services and APIs. Plugins also play nicely with dependency injection. Within a plugin's constructor, you can inject services that are necessary to perform the work of the plugin (e.g., database connections, HTTP clients, etc.). This is difficult to accomplish with other SDKs that lack plugins.

## Anatomy of a plugin

At a high-level, a plugin is a group of [functions](https://learn.microsoft.com/learn.microsoft.com#importing-different-types-of-plugins) that can be exposed to AI apps and services. The functions within plugins can then be orchestrated by an AI application to accomplish user requests. Within Semantic Kernel, you can invoke these functions automatically with function calling.

Note

In other platforms, functions are often referred to as "tools" or "actions". In Semantic Kernel, we use the term "functions" since they are typically defined as native functions in your codebase.

Just providing functions, however, is not enough to make a plugin. To power automatic orchestration with function calling, plugins also need to provide details that semantically describe how they behave. Everything from the function's input, output, and side effects need to be described in a way that the AI can understand, otherwise, the AI will not correctly call the function.

For example, the sample `WriterPlugin` plugin on the right has functions with semantic descriptions that describe what each function does. An LLM can then use these descriptions to choose the best functions to call to fulfill a user's ask.

In the picture on the right, an LLM would likely call the `ShortPoem` and `StoryGen` functions to satisfy the users ask thanks to the provided semantic descriptions.

![Semantic description within the WriterPlugin plugin](https://learn.microsoft.com/media/writer-plugin-example.png)

### Importing different types of plugins

There are three primary ways of importing plugins into Semantic Kernel: using [native code](https://learn.microsoft.com/adding-native-plugins), using an [OpenAPI specification](https://learn.microsoft.com/adding-openapi-plugins) or from a [MCP Server](https://learn.microsoft.com/adding-mcp-plugins) The former allows you to author plugins in your existing codebase that can leverage dependencies and services you already have. The latter two allow you to import plugins from an OpenAPI specification or a MCP Server, which can be shared across different programming languages and platforms.

Below we provide a simple example of importing and using a native plugin. To learn more about how to import these different types of plugins, refer to the following articles:

- [Importing native code](https://learn.microsoft.com/adding-native-plugins)
- [Importing an OpenAPI specification](https://learn.microsoft.com/adding-openapi-plugins)
- [Importing a MCP Server](https://learn.microsoft.com/adding-mcp-plugins)

Tip

When getting started, we recommend using native code plugins. As your application matures, and as you work across cross-platform teams, you may want to consider using OpenAPI specifications to share plugins across different programming languages and platforms. You can then also create a MCP Server from your Kernel instance, which allows other applications to consume your plugins as a service.

### The different types of plugin functions

Within a plugin, you will typically have two different types of functions, those that retrieve data for retrieval augmented generation (RAG) and those that automate tasks. While each type is functionally the same, they are typically used differently within applications that use Semantic Kernel.

For example, with retrieval functions, you may want to use strategies to improve performance (e.g., caching and using cheaper intermediate models for summarization). Whereas with task automation functions, you'll likely want to implement human-in-the-loop approval processes to ensure that tasks are completed correctly.

To learn more about the different types of plugin functions, refer to the following articles:

- [Data retrieval functions](https://learn.microsoft.com/using-data-retrieval-functions-for-rag)
- [Task automation functions](https://learn.microsoft.com/using-task-automation-functions)

## Getting started with plugins

Using plugins within Semantic Kernel is always a three step process:

1. [Define your plugin](https://learn.microsoft.com/learn.microsoft.com#1-define-your-plugin)
2. [Add the plugin to your kernel](https://learn.microsoft.com/learn.microsoft.com#2-add-the-plugin-to-your-kernel)
3. [And then either invoke the plugin's functions in either a prompt with function calling](https://learn.microsoft.com/learn.microsoft.com#3-invoke-the-plugins-functions)

Below we'll provide a high-level example of how to use a plugin within Semantic Kernel. Refer to the links above for more detailed information on how to create and use plugins.

### 1) Define your plugin

The easiest way to create a plugin is by defining a class and annotating its methods with the `KernelFunction` attribute. This let's Semantic Kernel know that this is a function that can be called by an AI or referenced in a prompt.

You can also import plugins from an [OpenAPI specification](https://learn.microsoft.com/adding-openapi-plugins).

Below, we'll create a plugin that can retrieve the state of lights and alter its state.

Tip

Since most LLM have been trained with Python for function calling, its recommended to use snake case for function names and property names even if you're using the C# or Java SDK.

```
using System.ComponentModel;
using Microsoft.SemanticKernel;

public class LightsPlugin
{
 // Mock data for the lights
 private readonly List lights = new()
 {
 new LightModel { Id = 1, Name = "Table Lamp", IsOn = false, Brightness = 100, Hex = "FF0000" },
 new LightModel { Id = 2, Name = "Porch light", IsOn = false, Brightness = 50, Hex = "00FF00" },
 new LightModel { Id = 3, Name = "Chandelier", IsOn = true, Brightness = 75, Hex = "0000FF" }
 };

 [KernelFunction("get_lights")]
 [Description("Gets a list of lights and their current state")]
 public async Task > GetLightsAsync()
 {
 return lights
 }

 [KernelFunction("get_state")]
 [Description("Gets the state of a particular light")]
 public async Task GetStateAsync([Description("The ID of the light")] int id)
 {
 // Get the state of the light with the specified ID
 return lights.FirstOrDefault(light => light.Id == id);
 }

 [KernelFunction("change_state")]
 [Description("Changes the state of the light")]
 public async Task ChangeStateAsync(int id, LightModel LightModel)
 {
 var light = lights.FirstOrDefault(light => light.Id == id);

 if (light == null)
 {
 return null;
 }

 // Update the light with the new state
 light.IsOn = LightModel.IsOn;
 light.Brightness = LightModel.Brightness;
 light.Hex = LightModel.Hex;

 return light;
 }
}

public class LightModel
{
 [JsonPropertyName("id")]
 public int Id { get; set; }

 [JsonPropertyName("name")]
 public string Name { get; set; }

 [JsonPropertyName("is_on")]
 public bool? IsOn { get; set; }

 [JsonPropertyName("brightness")]
 public byte? Brightness { get; set; }

 [JsonPropertyName("hex")]
 public string? Hex { get; set; }
}

```

```
from typing import TypedDict, Annotated

class LightModel(TypedDict):
 id: int
 name: str
 is_on: bool | None
 brightness: int | None
 hex: str | None

class LightsPlugin:
 lights: list[LightModel] = [
 {"id": 1, "name": "Table Lamp", "is_on": False, "brightness": 100, "hex": "FF0000"},
 {"id": 2, "name": "Porch light", "is_on": False, "brightness": 50, "hex": "00FF00"},
 {"id": 3, "name": "Chandelier", "is_on": True, "brightness": 75, "hex": "0000FF"},
 ]

 @kernel_function
 async def get_lights(self) -> List[LightModel]:
 """Gets a list of lights and their current state."""
 return self.lights

 @kernel_function
 async def get_state(
 self,
 id: Annotated[int, "The ID of the light"]
 ) -> Optional[LightModel]:
 """Gets the state of a particular light."""
 for light in self.lights:
 if light["id"] == id:
 return light
 return None

 @kernel_function
 async def change_state(
 self,
 id: Annotated[int, "The ID of the light"],
 new_state: LightModel
 ) -> Optional[LightModel]:
 """Changes the state of the light."""
 for light in self.lights:
 if light["id"] == id:
 light["is_on"] = new_state.get("is_on", light["is_on"])
 light["brightness"] = new_state.get("brightness", light["brightness"])
 light["hex"] = new_state.get("hex", light["hex"])
 return light
 return None

```

```
public class LightsPlugin {

 // Mock data for the lights
 private final Map lights = new HashMap<>();

 public LightsPlugin() {
 lights.put(1, new LightModel(1, "Table Lamp", false));
 lights.put(2, new LightModel(2, "Porch light", false));
 lights.put(3, new LightModel(3, "Chandelier", true));
 }

 @DefineKernelFunction(name = "get_lights", description = "Gets a list of lights and their current state")
 public List getLights() {
 System.out.println("Getting lights");
 return new ArrayList<>(lights.values());
 }

 @DefineKernelFunction(name = "change_state", description = "Changes the state of the light")
 public LightModel changeState(
 @KernelFunctionParameter(name = "id", description = "The ID of the light to change") int id,
 @KernelFunctionParameter(name = "isOn", description = "The new state of the light") boolean isOn) {
 System.out.println("Changing light " + id + " " + isOn);
 if (!lights.containsKey(id)) {
 throw new IllegalArgumentException("Light not found");
 }

 lights.get(id).setIsOn(isOn);

 return lights.get(id);
 }
}

```

Notice that we provide descriptions for the function, and parameters. This is important for the AI to understand what the function does and how to use it.

Tip

Don't be afraid to provide detailed descriptions for your functions if an AI is having trouble calling them. Few-shot examples, recommendations for when to use (and not use) the function, and guidance on where to get required parameters can all be helpful.

### 2) Add the plugin to your kernel

Once you've defined your plugin, you can add it to your kernel by creating a new instance of the plugin and adding it to the kernel's plugin collection.

This example demonstrates the easiest way of adding a class as a plugin with the `AddFromType` method. To learn about other ways of adding plugins, refer to the [adding native plugins](https://learn.microsoft.com/adding-native-plugins) article.

```
var builder = new KernelBuilder();
builder.Plugins.AddFromType ("Lights")
Kernel kernel = builder.Build();

```

```
kernel = Kernel()
kernel.add_plugin(
 LightsPlugin(),
 plugin_name="Lights",
)

```

```
// Import the LightsPlugin
KernelPlugin lightPlugin = KernelPluginFactory.createFromObject(new LightsPlugin(),
 "LightsPlugin");

```

```
// Create a kernel with Azure OpenAI chat completion and plugin
Kernel kernel = Kernel.builder()
 .withAIService(ChatCompletionService.class, chatCompletionService)
 .withPlugin(lightPlugin)
 .build();

```

### 3) Invoke the plugin's functions

Finally, you can have the AI invoke your plugin's functions by using function calling. Below is an example that demonstrates how to coax the AI to call the `get_lights` function from the `Lights` plugin before calling the `change_state` function to turn on a light.

```
using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.ChatCompletion;
using Microsoft.SemanticKernel.Connectors.OpenAI;

// Create a kernel with Azure OpenAI chat completion
var builder = Kernel.CreateBuilder().AddAzureOpenAIChatCompletion(modelId, endpoint, apiKey);

// Build the kernel
Kernel kernel = builder.Build();
var chatCompletionService = kernel.GetRequiredService ();

// Add a plugin (the LightsPlugin class is defined below)
kernel.Plugins.AddFromType ("Lights");

// Enable planning
OpenAIPromptExecutionSettings openAIPromptExecutionSettings = new()
{
 FunctionChoiceBehavior = FunctionChoiceBehavior.Auto()
};

// Create a history store the conversation
var history = new ChatHistory();
history.AddUserMessage("Please turn on the lamp");

// Get the response from the AI
var result = await chatCompletionService.GetChatMessageContentAsync(
 history,
 executionSettings: openAIPromptExecutionSettings,
 kernel: kernel);

// Print the results
Console.WriteLine("Assistant > " + result);

// Add the message from the agent to the chat history
history.AddAssistantMessage(result);

```

```
import asyncio

from semantic_kernel import Kernel
from semantic_kernel.functions import kernel_function
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion, AzureChatPromptExecutionSettings
from semantic_kernel.connectors.ai import FunctionChoiceBehavior
from semantic_kernel.contents import ChatHistory
from semantic_kernel.functions import KernelArguments

async def main():
 # Initialize the kernel
 kernel = Kernel()

 # Add Azure OpenAI chat completion
 chat_completion = AzureChatCompletion(
 deployment_name="your_models_deployment_name",
 api_key="your_api_key",
 base_url="your_base_url",
 )
 kernel.add_service(chat_completion)

 # Add a plugin (the LightsPlugin class is defined below)
 kernel.add_plugin(
 LightsPlugin(),
 plugin_name="Lights",
 )

 # Enable planning
 execution_settings = AzureChatPromptExecutionSettings()
 execution_settings.function_choice_behavior = FunctionChoiceBehavior.Auto()

 # Create a history of the conversation
 history = ChatHistory()
 history.add_message("Please turn on the lamp")

 # Get the response from the AI
 result = await chat_completion.get_chat_message_content(
 chat_history=history,
 settings=execution_settings,
 kernel=kernel,
 )

 # Print the results
 print("Assistant > " + str(result))

 # Add the message from the agent to the chat history
 history.add_message(result)

# Run the main function
if __name__ == "__main__":
 asyncio.run(main())

```

```
// Enable planning
InvocationContext invocationContext = new InvocationContext.Builder()
 .withReturnMode(InvocationReturnMode.LAST_MESSAGE_ONLY)
 .withToolCallBehavior(ToolCallBehavior.allowAllKernelFunctions(true))
 .build();

// Create a history to store the conversation
ChatHistory history = new ChatHistory();
history.addUserMessage("Turn on light 2");

List > results = chatCompletionService
 .getChatMessageContentsAsync(history, kernel, invocationContext)
 .block();

System.out.println("Assistant > " + results.get(0));

```

With the above code, you should get a response that looks like the following:

| Role | Message |
| --- | --- |
| 🔵 **User** | Please turn on the lamp |
| 🔴 **Assistant (function call)** | `Lights.get_lights()` |
| 🟢 **Tool** | `[{ "id": 1, "name": "Table Lamp", "isOn": false, "brightness": 100, "hex": "FF0000" }, { "id": 2, "name": "Porch light", "isOn": false, "brightness": 50, "hex": "00FF00" }, { "id": 3, "name": "Chandelier", "isOn": true, "brightness": 75, "hex": "0000FF" }]` |
| 🔴 **Assistant (function call)** | Lights.change\_state(1, { "isOn": true }) |
| 🟢 **Tool** | `{ "id": 1, "name": "Table Lamp", "isOn": true, "brightness": 100, "hex": "FF0000" }` |
| 🔴 **Assistant** | The lamp is now on |

Tip

While you can invoke a plugin function directly, this is not advised because the AI should be the one deciding which functions to call. If you need explicit control over which functions are called, consider using standard methods in your codebase instead of plugins.

## General recommendations for authoring plugins

Considering that each scenario has unique requirements, utilizes distinct plugin designs, and may incorporate multiple LLMs, it is challenging to provide a one-size-fits-all guide for plugin design.
However, below are some general recommendations and guidelines to ensure that plugins are AI-friendly and can be easily and efficiently consumed by LLMs.

### Import only the necessary plugins

Import only the plugins that contain functions necessary for your specific scenario. This approach will not only reduce the number of input tokens consumed but also minimize the occurrence of function
miscalls-calls to functions that are not used in the scenario. Overall, this strategy should enhance function-calling accuracy and decrease the number of false positives.

Additionally, OpenAI recommends that you use no more than 20 tools in a single API call; ideally, no more than 10 tools. As stated by OpenAI: _"We recommend that you use no more than_
_20 tools in a single API call. Developers typically see a reduction in the model's ability to select the correct tool once they have between 10-20 tools defined."_\*
For more information, you can visit their documentation at [OpenAI Function Calling Guide](https://platform.openai.com/docs/guides/function-calling#keep-the-number-of-functions-low-for-higher-accuracy).

### Make plugins AI-friendly

To enhance the LLM's ability to understand and utilize plugins, it is recommended to follow these guidelines:

- **Use descriptive and concise function names:** Ensure that function names clearly convey their purpose to help the model understand when to select each function. If a function name is ambiguous, consider renaming it for clarity.
Avoid using abbreviations or acronyms to shorten function names. Utilize the `DescriptionAttribute` to provide additional context and instructions only when necessary, minimizing token consumption.

- **Minimize function parameters:** Limit the number of function parameters and use primitive types whenever possible. This approach reduces token consumption and simplifies the function signature, making it easier for the LLM
to match function parameters effectively.

- **Name function parameters clearly:** Assign descriptive names to function parameters to clarify their purpose. Avoid using abbreviations or acronyms to shorten parameter names, as this will assist the LLM in reasoning about
the parameters and providing accurate values. As with function names, use the `DescriptionAttribute` only when necessary to minimize token consumption.


### Find a right balance between the number of functions and their responsibilities

On one hand, having functions with a single responsibility is a good practice that allows to keep functions simple and reusable across multiple scenarios. On the other hand, each function call incurs overhead in terms of network round-trip latency
and the number of consumed input and output tokens: input tokens are used to send the function definition and invocation result to the LLM, while output tokens are consumed when receiving the function call from the model.
Alternatively, a single function with multiple responsibilities can be implemented to reduce the number of consumed tokens and lower network overhead, although this comes at the cost of reduced reusability in other scenarios.
However, consolidating many responsibilities into a single function may increase the number and complexity of function parameters and its return type. This complexity can lead to situations where the model may struggle to correctly match the function parameters,
resulting in missed parameters or values of incorrect type. Therefore, it is essential to strike the right balance between the number of functions to reduce network overhead and the number of responsibilities each function has, ensuring that the model can accurately
match function parameters.

### Transform Semantic Kernel functions

Utilize the transformation techniques for Semantic Kernel functions as described in the [Transforming Semantic Kernel Functions](https://devblogs.microsoft.com/semantic-kernel/transforming-semantic-kernel-functions/#:%7E:text=Semantic%20Kernel%20provides%20a%20series,from%20an%20Open%20API%20specification) blog post to:

- **Change function behavior:** There are scenarios where the default behavior of a function may not align with the desired outcome and it's not feasible to modify the original function's implementation. In such cases, you can create a new function that wraps the
original one and modifies its behavior accordingly.

- **Provide context information:** Functions may require parameters that the LLM cannot or should not infer. For example, if a function needs to act on behalf of the current user or requires authentication information, this context is typically available to the host application but not to the LLM. In such cases, you can transform
the function to invoke the original one while supplying the necessary context information from the hosting application, along with arguments provided by the LLM.

- **Change parameters list, types, and names:** If the original function has a complex signature that the LLM struggles to interpret, you can transform the function into one with a simpler signature that the LLM can more easily understand.
This may involve changing parameter names, types, the number of parameters, and flattening or unflattening complex parameters, among other adjustments.


### Local state utilization

When designing plugins that operate on relatively large or confidential datasets, such as documents, articles, or emails containing sensitive information, consider utilizing local state to store original data or intermediate results that do not need to be
sent to the LLM. Functions for such scenarios can accept and return a state id, allowing you to look up and access the data locally instead of passing the actual data to the LLM, only to receive it back as an argument for the next function invocation.

By storing data locally, you can keep the information private and secure while avoiding unnecessary token consumption during function calls. This approach not only enhances data privacy but also improves overall efficiency in processing large or sensitive datasets.

### Provide function return type schema to AI model

Use one of the techniques described in the [Providing functions return type schema to LLM](https://learn.microsoft.com/adding-native-plugins#provide-function-return-type-information-in-function-description) section to provide the function's return type schema to the AI model.

By utilizing a well-defined return type schema, the AI model can accurately identify the intended properties, eliminating potential inaccuracies that may arise when the model makes assumptions based on incomplete or ambiguous information in the absence of the schema.
Consequently, this enhances the accuracy of function calls, leading to more reliable and precise outcomes.

## Additional resources
Highlights: None
Highlight Scores: None
Summary: None

Title: Creating Plugins with the Semantic Kernel SDK and C#
URL: https://www.willvelida.com/posts/create-plugins-semantic-kernel/
ID: https://www.willvelida.com/posts/create-plugins-semantic-kernel/
Score: None
Published Date: 2024-03-05T00:00:00.000Z
Author: Will Velida
Image: https://dev-to-uploads.s3.amazonaws.com/uploads/articles/hkz0hlcgrwnbnp3lgd98.png
Favicon: None
Extras: None
Subpages: None
Text: ![Creating Plugins with the Semantic Kernel SDK and C#](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/hkz0hlcgrwnbnp3lgd98.png)

Using the Semantic Kernel SDK, we use plugins that act as the building blocks for our AI applications. Plugins essentially define the tasks that the kernel should complete, and the kernel interfaces with large language models and run the plugins we define.

Table of Contents

- [Working with Built-in Plugins](https://www.willvelida.com/posts/create-plugins-semantic-kernel/#working-with-built-in-plugins)
- [Optimizing our prompts](https://www.willvelida.com/posts/create-plugins-semantic-kernel/#optimizing-our-prompts)
- [Saving prompts to files.](https://www.willvelida.com/posts/create-plugins-semantic-kernel/#saving-prompts-to-files)
- [Building our own prompts](https://www.willvelida.com/posts/create-plugins-semantic-kernel/#building-our-own-prompts)
- [Conclusion](https://www.willvelida.com/posts/create-plugins-semantic-kernel/#conclusion)

When we use the Semantic Kernel SDK, we use plugins that act as the building blocks for our AI applications. Plugins essentially define the tasks that the kernel should complete, and the kernel interfaces with large language models and run the plugins we define.

Plugins can include native code and natural language prompts, allowing us to use generative AI in our application. Plugins give us the flexibility of defining desired behavior in our application, and we can create custom prompt plugins to fine tune our applications precisely as we need to.

In this article, we’ll talk about how we can create our own Semantic Kernel SDK plugins to accomplish different custom tasks. We’ll also look at how we can use the built-in plugins from the Semantic Kernel SDK to create our applications.

**If you want to watch a video of this instead, check out the video I’ve posted on my YouTube channel below!**

[iframe](https://www.youtube.com/embed/GELR1bNfK6I?autoplay=0&controls=1&end=0&loop=0&mute=0&start=0)

## Working with Built-in Plugins [\#](https://www.willvelida.com/posts/create-plugins-semantic-kernel/\#working-with-built-in-plugins)

Plugins are fundamental to the Semantic Kernel SDK, as they define the tasks for the kernel to perform since they interface with LLMs. Plugins can be just native code and prompts that are invoked to the LLM. The great thing about the Semantic Kernel SDK is that it offers built-in plugins for common tasks that are ready to use.

Plugins are classes that defines a task that the kernel should perform. It can be made from a semantic prompt, or native function code. To use a plugin, we can add it to the kernel and call it using `InvokeAsync`. The kernel will then run the plugin that interfaces with the LLM, and returns the result.

Some examples of available built-in plugins include:

- `MathPlugin` = A plugin to perform mathematical operations.
- `TextPlugin` = A plugin to perform text manipulation.
- `TimePlugin` = A plugin to get time and date information.

## Optimizing our prompts [\#](https://www.willvelida.com/posts/create-plugins-semantic-kernel/\#optimizing-our-prompts)

The Semantic Kernel SDK supports a templating language that allows us to complete tasks using NLP prompts. These are conversational cues that we pass to LLMs, shaping responses based on your queries or instructions.

This involves providing rich instructions to guide the model to generate the desired response. This is important, since we need to provide clarity to our prompts to get the results we want. Here are some tips to keep in mind when we craft prompts:

- **Specific Inputs Yield Specific Outputs** \- LLMs will respond based on the input they receive. Having clear and specific prompts is crucial to get the desired output.
- **Try, and try again** \- Experimenting is key to understand how the model interprets and generates responses. Even small changes can lead to significant changes in outcomes.
- **The Context Matters** \- LLMs consider the context provided in the prompt. We need to ensure that the context is well-defined and relevant to obtain accurate responses.
- **Handling Ambiguity** \- Ambiguous queries are always fun, but even LLMs will struggle with them. Provide context and structure to avoid vague or unexpected results.
- **Length of Prompts** \- While LLMs can process both short and long prompts, you need to consider the tradeoff between clarity and brevity. Experiment with the prompt length can help you find the right balance.

## Saving prompts to files. [\#](https://www.willvelida.com/posts/create-plugins-semantic-kernel/\#saving-prompts-to-files)

One cool feature we can implement for larger projects is the ability to organize our prompts into separate files, and then import them into the kernel. For our own plugins, it’s a good idea to create separate folders for our prompts.

The Semantic Kernel SDK supports a prompt templating language with some simple syntax rules. We don’t need to write code or import any external libraries. Semantic Kernel parses your template and runs the logic behind it. This supports adding variables, calling external functions, and passing parameters to functions.

This is configured using a `config.json` file. As the name suggests, this contains the configuration details for the prompt, and is placed in the same folder as the `skprompt.txt` file. It supports the following parameters:

- `type` \- The type of prompt.
- `description` \- A description of what the prompt does. This can be used by the kernel to automatically invoke the prompt.
- `input_variables` \- Defines the variables that are used inside the prompt.
- `execution_settings` \- Defines the setting for completion models.

## Building our own prompts [\#](https://www.willvelida.com/posts/create-plugins-semantic-kernel/\#building-our-own-prompts)

Let’s see how everything works through an example. I want to build an AI agent that helps me with building out my exercise routine (especially for my legs). At the same time, I’m trying to improve my Italian, so I’ll see if my AI agent can provide me a few recommendations for leg exercises in Italian!

I’ve created a new Console Application to build my AI agent, and I’ll be using the Azure OpenAI model that I created in [this blog post](https://www.willvelida.com/posts/intro-to-semantic-kernel/). To use that model in Azure OpenAI, I’ll need to include an `appsettings.json` file that includes the following:

```
{
 "DEPLOYMENT_MODEL":"",
 "AZURE_OPEN_AI_ENDPOINT":"",
 "AZURE_OPEN_AI_KEY":""
}

```

Once we have that, we’ll need to install the following packages:

```
dotnet add package Microsoft.SemanticKernel
dotnet add package Microsoft.Extensions.Configuration --version 8.0.0
dotnet add package Microsoft.SemanticKernel.Plugins.Core --version 1.5.0-alpha

```

With all our NuGet packages installed, we can start by building our Kernel object and add a built-in plugin. Write the following:

```
using Microsoft.Extensions.Configuration;
using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.Plugins.Core;
var config = new ConfigurationBuilder()
 .AddJsonFile("appsettings.json")
 .Build();
var builder = Kernel.CreateBuilder();
builder.Services.AddAzureOpenAIChatCompletion(
 config["DEPLOYMENT_MODEL"],
 config["AZURE_OPEN_AI_ENDPOINT"],
 config["AZURE_OPEN_AI_KEY"]);
builder.Plugins.AddFromType ();
var kernel = builder.Build();

```

In this code block, we are loading our configuration and adding our connector to Azure OpenAI. We then add a `ConversationSummaryPlugin` to our kernel from the `Core.Plugins` package. We create the kernel and then add the plugin to it.

We then start to build our prompt that asks the LLM to provide a list of leg exercises in Italian. We can do this by writing the following:

```
string language = "Italian";
string input = @$"I'm new to the gym and I want to learn about body building.
 Can you give me a list of leg exercises that are beginner friendly and will
 help me build my leg muscles" in ${language}?";
var result = await kernel.InvokePromptAsync(input);
Console.WriteLine(result);

```

If we run this, our response should be similar to the following:

```
Certamente! Ecco una lista di esercizi per le gambe per principianti che possono aiutarti a costruire i muscoli delle gambe:
1. Squat a corpo libero
2. Affondi
3. Step up con sovraccarico
4. Leg press sui macchinari
5. Leg extension sui macchinari
6. Curl delle gambe sui macchinari
7. Stacchi da terra con manubri o bilanciere
8. Glute bridge
9. Hip thrust
10. Calf raises sulla macchina apposita
Ricorda che l'esecuzione corretta dell'esercizio è fondamentale per evitare infortuni e massimizzare i risultati. Ti consiglio di iniziare con un peso leggero e poi aumentare gradualmente man mano che acquisisci più forza e resistenza. Buona fortuna!

```

Bravo! We have received a response from the Azure OpenAI model that we passed to the kernel, which the Semantic Kernel SDK connects to and runs the prompt. We can improve the prompt by adding more specific instructions.

Since I’m trying to make my legs stronger, let’s update the prompt to show me how many reps and sets I should do to increase my strength:

```
string input = @$"I'm new to the gym and I want to learn about body building.
 Can you give me a list of leg exercises that are beginner friendly and will
 help me build my leg muscles in ${language}?
 Tell me how many reps and sets I should do to increase my strength. Display
 the exercises in the following format: Exercise - Reps x Sets";

```

We should see a similar response to this:

```
Certo! Ecco una lista di esercizi per le gambe che sono adatti ai principianti:
1. Squat bodyweight - 12 x 3
2. Affondi statici - 10 x 3 per gamba
3. Calf Raise - 15 x 3
In generale, per aumentare la forza si consiglia di fare 8-12 ripetizioni per serie e 2-3 serie per esercizio. Tuttavia, essendo tu un principiante, potresti cominciare con un numero inferiore di ripetizioni e serie e aumentare gradualmente man mano che acquisisci più forza e resistenza.
Buona fortuna con il tuo programma di allenamento!

```

Nice! We can also change our prompt to include some background information. I’ve been going to the gym for a while now, so let’s change our prompt to include that background:

```
string language = "Italian";
string background = @"I have been going to the gym for over 10 years, and I'm an experienced weightlifter";
string input = @$"Consider the weightlifter's background: ${background}.
 Can you give me a list of leg exercises that will
 help me build my leg muscles in ${language}?
 Tell me how many reps and sets I should do to increase my strength. Display
 the exercises in the following format: Exercise - Reps x Sets";

```

We should see an output similar to the following:

```
Certo! Ecco una lista di esercizi per le gambe che possono aiutare a sviluppare i muscoli delle gambe:
1. Squat - 8-10 x 3-4
2. Affondi con manubri - 10-12 x 3-4
3. Stacco da terra - 6-8 x 3-4
4. Curl delle gambe sdraiato - 10-12 x 3-4
5. Estensione delle gambe - 10-12 x 3-4
Per aumentare la forza, ti consiglio di fare meno ripetizioni ma con più set. Inizia con 3-4 set per ogni esercizio e aumenta gradualmente il peso. Quando ti alleni con pesi più pesanti, cerca di fare tra le 6 e le 8 ripetizioni per set.
Buona fortuna!

```

Let’s improve the quality of our responses generated by the LLM by adding a **persona** to our prompt. To do this, let’s update our prompt (I’m removing the language for now, but I’ll add it in later):

```
string input = @$"
 You are a gym instructor. You are very friendly, positive and give as much detail as possible.
 Consider the weightlifter's background: ${background}.
 Can you give me a list of leg exercises that will
 help me build my leg muscles?
 Tell me how many reps and sets I should do to increase my strength. Display
 the exercises in the following format: Exercise - Reps x Sets";

```

Here’s the response:

```
Absolutely! Here are some leg exercises that will help you build leg muscles:
1. Squats - 8-12 reps x 3-5 sets
2. Lunges - 8-12 reps (per leg) x 3-5 sets
3. Deadlifts - 8-12 reps x 3-5 sets
4. Leg Press - 10-15 reps x 3-5 sets
5. Bulgarian Split Squats - 8-12 reps (per leg) x 3-5 sets
6. Romanian Deadlifts - 8-12 reps x 3-5 sets
7. Step-Ups - 8-12 reps (per leg) x 3-5 sets
8. Calf Raises - 12-15 reps x 3-5 sets
These exercises are great for building leg muscles because they target various muscles in the legs. When performing these exercises, it's important to use proper form and technique to avoid any injuries.
In terms of reps and sets, it's recommended to do 8-12 reps per set and 3-5 sets per exercise to increase strength. However, it's important to listen to your body and adjust the reps and sets based on your fitness level and goals.
Remember to also incorporate rest days into your workout routine to allow your muscles to recover and grow. Happy lifting!

```

I’ll add the Italian back in, and I’ll get the following response:

```
Certo! Ecco una selezione di esercizi per le gambe che puoi provare:
1. Squat - 4 x 8-10
2. Affondi - 3 x 12-15 per gamba
3. Stacchi da terra - 4 x 8-10
4. Estensione delle gambe - 3 x 12-15
5. Curl delle gambe sdraiati - 3 x 12-15
È importante scegliere un peso che sia abbastanza impegnativo da sollevare ma che ti permetta comunque di mantenere una buona forma durante l'esecuzione dell'esercizio. Se vuoi aumentare la tua forza, ti consiglio di fare 4-6 serie da 6-8 ripetizioni con un peso più pesante e con 2-3 minuti di riposo tra le serie. Se invece vuoi aumentare la tua resistenza muscolare, puoi fare 3-4 serie da 12-15 ripetizioni con un peso più leggero e con 1-2 minuti di riposo tra le serie. Ricorda di inserire anche dei giorni di recupero tra le sessioni di allenamento delle gambe per permettere ai muscoli di riposare e recuperare. Buon allenamento!

```

We can provide instructions to our LLM to assume roles when generating responses, and provide requests and responses as an example. Using Semantic Kernel, we use a special syntax to define user roles. Let’s change our input and prompt to use this syntax:

```
string input = "@I enjoy compund exercises using the barbell. I tend to avoid exercise machines";
string prompt = $@"
 The following is a conversation with an AI fitness instructor. The instructor is friendly, positive and knowledgeable.
 Can you give me a list of leg exercises that will help me build my leg muscles?>/message>
 Of course! Do you have any exercises that you know and love to do? 
 ${input} ";
var result = await kernel.InvokePromptAsync(prompt);
Console.WriteLine(result);

```

Let’s see our response:

```
Great! Here are some leg exercises that you can do with a barbell:
1. Squats (squat rack required)
2. Deadlifts
3. Lunges (barbell held in front of the chest)
4. Bulgarian split squats (one foot on the bench, the other foot on the ground, holding the barbell on your shoulders)
These exercises are great for building leg muscles and can be tailored to your fitness level and goals. Let me know if you have any questions or need further guidance on how to perform these exercises.

```

These prompts have worked well for us so far, but as our project grows, we’ll want to create prompts and save them to files. We’ll also use variables and calling functions inside our prompt templates as well.

To do this, I’ve created the following folders in my project:

- Prompts
- Prompts/ExercisePlugins
- Prompts/ExercisePlugins/GetExercise
- Prompts/ExercisePlugins/SuggestExercise

To create our prompts, we need to create the `config.json` and `skprompt.txt` files. Let’s start with the GetExercise plugin. In our `config.json` file, enter the following:

```
{
 "schema": 1,
 "type": "completion",
 "description": "Identify the body area of the user's exercise plan",
 "execution_settings": {
 "default": {
 "max_tokens": 1200,
 "temperature": 0
 }
 },
 "input_variables": [
 {
 "name": "input",
 "description": "Text from the user that contains their desired body area for exercises",
 "required": true
 }
 ]
}

```

Next, in our `skprompt.txt` file, enter the following text:

```
 
Instructions: Identify the body area the user wants to exercise.
 
 
Can you give me a list of exercises that will help me build my muscles?
 
 Of course! Do you have any exercises that you know and love to do? 
 {{$input}} 

```

For our SuggestExercises plugin, we can create our `config.json` like so:

```
{
 "schema": 1,
 "type": "completion",
 "description": "Recommend weight exercises to the user",
 "execution_settings": {
 "default": {
 "max_tokens": 1200,
 "temperature": 0.3
 }
 },
 "input_variables": [
 {
 "name": "input",
 "description": "Details about the user's body area",
 "required": true
 }
 ]
}

```

And for our `skprompt.txt` file:

```
The following is a conversation with an AI fitness instructor. The instructor is friendly, positive and knowledgeable.
 Can you give me a list of leg exercises that will help me build my leg muscles? 
 Of course! Do you have any exercises that you know and love to do? 
 ${input} "

```

Let’s test our new prompts and update our `Program.cs` file to import our new Plugins.

```
using Microsoft.Extensions.Configuration;
using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.ChatCompletion;
using Microsoft.SemanticKernel.Plugins.Core;
var config = new ConfigurationBuilder()
 .AddJsonFile("appsettings.json")
 .Build();
var builder = Kernel.CreateBuilder();
builder.Services.AddAzureOpenAIChatCompletion(
 config["DEPLOYMENT_MODEL"],
 config["AZURE_OPEN_AI_ENDPOINT"],
 config["AZURE_OPEN_AI_KEY"]);
var kernel = builder.Build();
kernel.ImportPluginFromType ();
var prompts = kernel.ImportPluginFromPromptDirectory("Prompts/ExercisePlugins");
ChatHistory history = [];
string input = @"I want to build my leg strength. I love barbell exercises and compound exercises.";
var result = await kernel.InvokeAsync (prompts["SuggestExercises"],
 new() { { "input", input } });
Console.WriteLine(result);
history.AddUserMessage(input);
history.AddAssistantMessage(result);

```

In this code, we’ve imported our created plugins. We can store the user’s conversation using the `ChatHistory` object, and pass some information to the `SuggestExercises` prompt and record the results.

We should see the following output.

```
Great! Here are some exercises that can help you build your leg muscles:
1. Squats - This is a classic exercise that targets your quadriceps, hamstrings, and glutes. You can do squats with just your bodyweight or add weights for more resistance.
2. Lunges - Lunges are another great exercise that targets your quads, hamstrings, and glutes. You can do walking lunges, reverse lunges, or stationary lunges.
3. Deadlifts - Deadlifts are a compound exercise that work your hamstrings, glutes, and lower back. They can be done with a barbell, dumbbells, or kettlebells.
4. Leg press - The leg press machine is a great way to target your quads, hamstrings, and glutes. You can adjust the weight and foot placement to target different areas of your legs.
5. Calf raises - Calf raises target your calf muscles and can be done with bodyweight or added weight.
Remember to always warm up before exercising and to use proper form to prevent injury. Good luck with your leg workouts!

```

## Conclusion [\#](https://www.willvelida.com/posts/create-plugins-semantic-kernel/\#conclusion)

In this article, we talked about how we can use built-in plugins in Semantic Kernel. We also learned how to prompt and craft prompts to get the best response from a LLM. We also learnt how to create our own custom prompts to further tailor our experience for our users.

If you want to learn more about the Semantic Kernal SDK and how prompts work, check out the following resources:

- [What is Semantic Kernel?](https://learn.microsoft.com/en-us/semantic-kernel/overview/)
- [Getting started with the Semantic Kernel](https://learn.microsoft.com/en-us/semantic-kernel/get-started/quick-start-guide?toc=%2Fsemantic-kernel%2Ftoc.json&tabs=Csharp)
- [Semantic Kernel on GitHub](https://github.com/microsoft/semantic-kernel)
- [What are prompts?](https://learn.microsoft.com/en-us/semantic-kernel/prompts/)
- [Understanding AI plugins in Semantic Kernel](https://learn.microsoft.com/en-us/semantic-kernel/agents/plugins/?tabs=Csharp)
- [Saving and sharing prompts](https://learn.microsoft.com/en-us/semantic-kernel/prompts/saving-prompts-as-files?tabs=Csharp)

As always, if you have any questions, feel free to reach out to me on twitter [@willvelida](https://twitter.com/willvelida)

Until next time, Happy coding! 🤓🖥️
Highlights: None
Highlight Scores: None
Summary: None

Title: Using Semantic Kernel to create a Time Plugin with .NET | Semantic Kernel
URL: https://devblogs.microsoft.com/semantic-kernel/using-semantic-kernel-to-create-a-time-plugin-with-net/
ID: https://devblogs.microsoft.com/semantic-kernel/using-semantic-kernel-to-create-a-time-plugin-with-net/
Score: None
Published Date: 2024-05-14T13:53:10.000Z
Author: Sophia Lagerkrans-Pandey
Image: https://devblogs.microsoft.com/semantic-kernel/wp-content/uploads/sites/78/2024/03/Tutorial.png
Favicon: None
Extras: None
Subpages: None
Text: [Skip to main content](javascript:void(0))

![Sophia Lagerkrans-Pandey](https://devblogs.microsoft.com/semantic-kernel/wp-content/uploads/sites/78/2024/02/Sophia-Pandey-96x96.jpeg)![Roger Barreto](https://devblogs.microsoft.com/semantic-kernel/wp-content/uploads/sites/78/2024/03/19890735-96x96.png)

[Sophia](https://devblogs.microsoft.com/semantic-kernel/author/sopand),

[Roger](https://devblogs.microsoft.com/semantic-kernel/author/rbarreto)

Plugins are one of the most powerful features of Semantic Kernel and in this demo we show how you can easily use Plugins with the power of Auto Function Calling from AI Models.

**A Glimpse into the Demonstration**

**Time Information Plugin**

In the demo we implement a simple class TimeInformantionPlugin with one function to retrieve the UTC time in string format.

```
public class TimeInformationPlugin
{
    [KernelFunction]
    [Description("Retrieves the current time in UTC.")]
    public string GetCurrentUtcTime() => DateTime.UtcNow.ToString("R");
}
```

C# functions that can be imported to Plugins are marked with KernelFunction that will instruct the Kernel what are going to be imported into Plugins using Description attribute will be used on how those functions will be detailed to the AI Model for calling so it will have a better understanding on when to use your functions.

When implementing functions in your plugins you can use many different signatures, including asynchronous tasks and different types, check our \[Concept – Method Function Types\]( [semantic-kernel/dotnet/samples/Concepts/Functions/MethodFunctions\_Types.cs at main · microsoft/semantic-kernel (github.com)](https://github.com/microsoft/semantic-kernel/blob/main/dotnet/samples/Concepts/Functions/MethodFunctions_Types.cs)) sample for more details.

- Info: Is very important providing descriptions to your functions and arguments when using them against the AI for best results.

**Configuring the Kernel**

In the code below we use the configuration extensions from .Net to get the current OpenAI configuration details to setup and initialize the kernel with an OpenAI connector and our TimeInformationPlugin ready to use.

```
var config = new ConfigurationBuilder()
    .AddUserSecrets ()
    .AddEnvironmentVariables()
    .Build()

var kernelBuilder = Kernel.CreateBuilder().AddOpenAIChatCompletion(
    modelId: config["OpenAI:ChatModelId"]!,
    apiKey: config["OpenAI:ApiKey"]!);

kernelBuilder.Plugins.AddFromType ();

var kernel = kernelBuilder.Build();
```

**Using Auto Function Calling**

With the kernel instance is possible to get the completion service and use it to call the AI. Is important to configure your execution settings to enable AutoInvocation as this is not a default configuration and won’t expose your plugins inadvertently to AI.

```
var chatCompletionService = kernel.GetRequiredService ();

OpenAIPromptExecutionSettings openAIPromptExecutionSettings = new()
{
    // Enable auto function calling
    ToolCallBehavior = ToolCallBehavior.AutoInvokeKernelFunctions
};
```

Is also important to create and pass the chat history so it keeps the track of the conversation with the AI in a loop and it improves the overall results.

```
chatHistory.AddUserMessage(input);

var chatResult = await chatCompletionService.GetChatMessageContentAsync(chatHistory, openAIPromptExecutionSettings, kernel);
Console.Write($"\nAssistant > {chatResult}\n");
```

For each iteration in this loop, the assistant will get an instruction from the user, and whenever the instruction suggest a need to get the current time, it will be invoked by the AI automatically.

**Dive Deeper**

Please reach out if you have any questions or feedback through our [Semantic Kernel GitHub Discussion Channel](https://github.com/microsoft/semantic-kernel/discussions/categories/general). We look forward to hearing from you!

Category

[.NET](https://devblogs.microsoft.com/semantic-kernel/category/net/) [Samples](https://devblogs.microsoft.com/semantic-kernel/category/samples/) [Semantic Kernel](https://devblogs.microsoft.com/semantic-kernel/category/semantic-kernel/)

Topics

[.NET](https://devblogs.microsoft.com/semantic-kernel/tag/net/) [AI](https://devblogs.microsoft.com/semantic-kernel/tag/ai/) [Microsoft Semantic Kernel](https://devblogs.microsoft.com/semantic-kernel/tag/microsoft-semantic-kernel/) [Semantic Kernel](https://devblogs.microsoft.com/semantic-kernel/tag/semantic-kernel/)

## Author

![Sophia Lagerkrans-Pandey](https://devblogs.microsoft.com/semantic-kernel/wp-content/uploads/sites/78/2024/02/Sophia-Pandey-96x96.jpeg)

[Sophia Lagerkrans-Pandey](https://devblogs.microsoft.com/semantic-kernel/author/sopand)

![Roger Barreto](https://devblogs.microsoft.com/semantic-kernel/wp-content/uploads/sites/78/2024/03/19890735-96x96.png)

[Roger Barreto](https://devblogs.microsoft.com/semantic-kernel/author/rbarreto)

Senior Software Engineer

## 1 comment

Discussion is closed. [Login to edit/delete existing comments.](https://devblogs.microsoft.com/semantic-kernel/wp-login.php?redirect_to=https%3A%2F%2Fdevblogs.microsoft.com%2Fsemantic-kernel%2Fusing-semantic-kernel-to-create-a-time-plugin-with-net%2F%23comments)

[Code of Conduct](https://answers.microsoft.com/en-us/page/codeofconduct)

Sort by :

Newest

[Newest](javascript:void(0)) [Popular](javascript:void(0)) [Oldest](javascript:void(0))

- ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGQAAAAyAQMAAACQ++z9AAAAA1BMVEXW1taWrGEgAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAAD0lEQVQokWNgGAWjYGgCAAK8AAGBAoNpAAAAAElFTkSuQmCC)





I do not see \`ToolCallBehavior\` in the \`HuggingFacePromptExecutionSettings\`. When running the application without this setting the time is not returned, which sounds like is the expected functionality when the setting is not used. Is it possible to use HuggingFace with kernel functions?


## Read next

May 17, 2024

### [Using Semantic Kernel to create a Time Plugin with Java](https://devblogs.microsoft.com/semantic-kernel/using-semantic-kernel-to-create-a-time-plugin-with-java/)

![Sophia Lagerkrans-Pandey](https://devblogs.microsoft.com/semantic-kernel/wp-content/uploads/sites/78/2024/02/Sophia-Pandey-96x96.jpeg)

Sophia Lagerkrans-Pandey

May 17, 2024

### [Use Semantic Kernel to create a Restaurant Bookings Sample with Java](https://devblogs.microsoft.com/semantic-kernel/use-semantic-kernel-to-create-a-restaurant-bookings-sample-with-java/)

![Sophia Lagerkrans-Pandey](https://devblogs.microsoft.com/semantic-kernel/wp-content/uploads/sites/78/2024/02/Sophia-Pandey-96x96.jpeg)

Sophia Lagerkrans-Pandey

## Stay informed

Get notified when new posts are published.

Subscribe

By subscribing you agree to our [Terms of Use](https://docs.microsoft.com/en-us/collaborate/terms-of-use) and [Privacy](https://go.microsoft.com/fwlink/?LinkId=521839)

Follow this blog

[![linkedin](https://devblogs.microsoft.com/semantic-kernel/wp-content/themes/devblogs-evo/images/social-icons/linkedin.svg)](https://www.linkedin.com/showcase/microsoft-developers/)

[Sign in](https://devblogs.microsoft.com/semantic-kernel/wp-login.php?redirect_to=https%3A%2F%2Fdevblogs.microsoft.com%2Fsemantic-kernel%2Fusing-semantic-kernel-to-create-a-time-plugin-with-net%2F)

Theme

# Insert/edit link

Close

Enter the destination URL

URL

Link Text

Open link in a new tab

Or link to existing content

Search

_No search term specified. Showing recent items._ _Search or use up and down arrow keys to select an item._

Cancel

[Feedback](javascript://https:%2F%2Fdevblogs.microsoft.com%2Fsemantic-kernel%2Fusing-semantic-kernel-to-create-a-time-plugin-with-net%2F)
Highlights: None
Highlight Scores: None
Summary: None

Title: Guest Blog: Orchestrating AI Agents with Semantic Kernel Plugins: A Technical Deep Dive | Semantic Kernel
URL: https://devblogs.microsoft.com/semantic-kernel/guest-blog-orchestrating-ai-agents-with-semantic-kernel-plugins-a-technical-deep-dive/
ID: https://devblogs.microsoft.com/semantic-kernel/guest-blog-orchestrating-ai-agents-with-semantic-kernel-plugins-a-technical-deep-dive/
Score: None
Published Date: 2025-05-02T21:10:12.000Z
Author: Sophia Lagerkrans-Pandey
Image: https://devblogs.microsoft.com/semantic-kernel/wp-content/uploads/sites/78/2025/05/2025-05-02-140637-dall-e-3.jpg
Favicon: None
Extras: None
Subpages: None
Text: Today we’re excited to welcome Jarre Nejatyab as a guest blog to highlight a technical deep dive on orchestrating AI Agents with Semantic Kernel Plugins.

In the rapidly evolving world of Large Language Models (LLMs), orchestrating specialized AI agents has become crucial for building sophisticated cognitive architectures capable of complex reasoning and task execution. While powerful, coordinating multiple agents—each with unique capabilities and data access—presents significant engineering challenges. Microsoft’s Semantic Kernel (SK) offers a robust framework for managing this complexity through its intuitive plugin system. This blog post provides a technical deep dive into leveraging SK plugins for effective agent orchestration, illustrated with practical implementation patterns.

## The Challenge of Agent Orchestration

Modern AI applications often transcend the capabilities of a single LLM. They increasingly rely on ensembles of specialized agents working in concert. For instance, a query might require input from an agent accessing internal policy documents, another searching the public web, and a third querying a private database. The core challenge lies in:

- **Dynamically selecting** the right agent(s) for a given task.
- **Managing context and data flow** between agents.
- **Synthesizing potentially conflicting outputs** into a coherent final response.
- **Maintaining modularity and observability** as the system scales.

## Semantic Kernel Plugins

Semantic Kernel’s plugin architecture provides a structured solution. Plugins act as standardized wrappers around agent capabilities, enabling the kernel (the central orchestrator) to discover, invoke, and manage them effectively. Key benefits include:

1. **Modular Agent Integration**: Encapsulate each agent’s logic within a dedicated plugin.
2. **Declarative Invocation**: Define agent capabilities with clear descriptions, allowing the kernel’s LLM to dynamically choose the appropriate tool(s) based on the user query and context.
3. **Unified Interface**: Standardize communication, simplifying interactions between the orchestrator and diverse agents.
4. **Centralized Monitoring**: Track resource usage (like tokens) and execution flow across all agents.
5. **Simplified Result Aggregation**: Provide hooks to combine outputs from multiple agents into a cohesive final response.

## Architecture Overview

Let’s examine a conceptual architecture for an orchestration system using SK plugins:

This architecture features:

- A central **Orchestrator Agent**, powered by Semantic Kernel, receiving user queries.
- Multiple **Specialized Agent Plugins**, each exposing the capabilities of a specific agent (e.g., Web Search, Org Policy Lookup, Private Data Query).
- A **Plugin Registration** mechanism making agent capabilities discoverable by the kernel.
- **Result Aggregation** logic within the orchestrator to synthesize a final answer. The kernel uses the descriptions provided within each plugin (via decorators like `@kernel_function`) to determine which plugin(s) are relevant to the user’s query, enabling dynamic and context-aware agent invocation.

## Implementation Example

Consider this simplified Python implementation of an orchestrator agent using the Semantic Kernel SDK:

```
class OrchestratorAgent:
 async def invoke(self, message: ChatMessage, context: Context) -> ChatResponseMessage:
 # 1. Set up the system prompt guiding the LLM orchestrator
 self._history.add_system_message(self.system_prompt)
 self._history.add_user_message(message.user_query)
 # 2. Initialize specialized agent plugins
 org_policy_agent_plugin = OrgPolicyAgentInvokingPlugin(kernel=self._kernel, message=message)
 web_search_agent_plugin = WebSearchAgentInvokingPlugin(kernel=self._kernel, message=message)
 private_data_agent_plugin = PrivateDataAgentInvokingPlugin(kernel=self._kernel, message=message)
 generic_agent_plugin = GenericAgentInvokingPlugin(kernel=self._kernel, message=message) # Fallback agent
 # 3. Register plugins with the kernel, providing descriptive names
 self._kernel.add_plugin(org_policy_agent_plugin, plugin_name="ORG_POLICY_AGENT")
 self._kernel.add_plugin(web_search_agent_plugin, plugin_name="WEB_SEARCH_AGENT")
 self._kernel.add_plugin(private_data_agent_plugin, plugin_name="PRIVATE_DATA_AGENT")
 self._kernel.add_plugin(generic_agent_plugin, plugin_name="GENERIC_LLM_AGENT")
 # Configure the kernel to automatically invoke functions based on the prompt and plugin descriptions
 # execution_settings = ... # Configure execution settings, e.g., FunctionChoiceBehavior.Auto()
 # 4. Invoke the kernel. The underlying LLM uses the prompt and function descriptions
 # to decide which plugin functions to call (sequentially or in parallel).
 results = []
 # Assuming self._sk_agent uses the configured kernel and execution settings
 async for content in self._sk_agent.invoke(self._history): # Potentially involves multiple plugin calls
 results.append(content)
 # 5. Aggregate results from all potentially invoked plugins
 # (Plugins should track their own invocation status and results)
 agent_invoking_plugins = [
 org_policy_agent_plugin,
 web_search_agent_plugin,
 private_data_agent_plugin,
 generic_agent_plugin
 ] # List of all potential plugins
 # 6. Calculate total token usage across invoked plugins
 # (Requires plugins to expose usage data)
 total_prompt_tokens = sum(plugin.token_usage.prompt_token for plugin in agent_invoking_plugins if plugin.was_invoked) # Example: Check if invoked
 total_completion_tokens = sum(plugin.token_usage.completion_token for plugin in agent_invoking_plugins if plugin.was_invoked)
 # 7. Compile search results/citations from invoked plugins
 # (Requires plugins to expose relevant results)
 search_result = SearchResult(docs=[], citations=[])
 for plugin in agent_invoking_plugins:
 if plugin.was_invoked: # Example: Check if invoked
 search_result.docs.extend(plugin.search_result.docs)
 search_result.citations.extend(plugin.search_result.citations)
 # 8. Return the consolidated response (likely the final LLM synthesis from step 4)
 final_content = results[-1].content if results else "Could not generate a response."
 return ChatResponseMessage(
 content=final_content,
 search_result=search_result,
 token_usage=TokenUsage(
 prompt_token=total_prompt_tokens,
 completion_token=total_completion_tokens,
 ),
 )
# Note: Requires AgentInvokingPlugin base class to define/manage
# token_usage, search_result, was_invoked attributes, etc.

```

This example highlights how plugins are registered and how the kernel orchestrates their execution, followed by result aggregation. (Note: Error handling and detailed state management are omitted for brevity).

## Anatomy of an Agent Plugin: WebSearchAgentInvokingPlugin

Let’s examine the `WebSearchAgentInvokingPlugin` more closely.

```
# Assumes AgentInvokingPlugin base class handles kernel, message, runtime, etc.
class WebSearchAgentInvokingPlugin(AgentInvokingPlugin):
 @kernel_function(
 name="invoke_web_search_agent",
 description="""WebSearch plugin. Use this to answer questions requiring current, public information, such as:
 - General knowledge questions or facts (e.g., 'What is the capital of France?')
 - Current events, market data, or industry trends (e.g., 'Latest stock price for MSFT?')
 - Technical information likely found online (e.g., 'How to configure a Flask server?')
 - Information published in academic papers or public industry reports.""",
 )
 async def invoke_web_search_agent(
 self,
 query: Annotated[str, "The specific question or topic to search the web for. Should be self-contained."],
 ):
 """Invokes the external Web Search Agent."""
 # self.was_invoked = True # Mark as invoked
 message_body = self.create_message_body(query) # Prepare agent-specific message
 recipient = AgentId(WEBSEARCH_AGENT, str(self.message.metadata.session_id)) # Target agent
 # Send message via runtime and await response
 result = await self.runtime.send_message(message=message_body, recipient=recipient)
 # Process result, update internal state (token usage, search results), and return
 processed_response = self.proccess_and_create_response(result)
 # self.token_usage = ... # Update token usage based on result
 # self.search_result = ... # Update search results based on result
 return processed_response # Return processed data, often just a summary string for the orchestrator LLM

```

Key aspects enabling orchestration:

### 1\. Clear Domain Boundaries via `@kernel_function`

The `description` parameter in `@kernel_function` is crucial. The orchestrator LLM uses this natural language description to understand _when_ to use this specific plugin. A well-crafted description significantly improves the accuracy of dynamic function calling.

### 2\. Informative Parameter Signatures with `Annotated`

Type hints ( `str`) and `Annotated` descriptions ( `"The specific question..."`) provide further context to the LLM, helping it formulate the correct input ( `query`) for the function based on the overall user request.

### 3\. Encapsulated Agent Communication Logic

The plugin abstracts the details of interacting with the specific agent (creating messages, identifying recipients, handling runtime communication). The orchestrator only needs to know about the high-level `invoke_web_search_agent` function.

### 4\. Standardized Result Processing

The `proccess_and_create_response` method (part of the base class or implemented here) normalizes the agent’s raw output into a format the orchestrator expects. It also updates shared state like token counts and extracted citations, essential for the final aggregation step.

## Hierarchical Plugin Structure

Semantic Kernel supports organizing plugins hierarchically, which can mirror complex agent interactions:

An `AgentInvokingPlugin` might internally use other, more granular plugins (e.g., a `BingSearchPlugin` or an `HttpRequestPlugin`). This allows for composition and reuse of lower-level functionalities within the agent abstraction.

## The Power of Plugin-Based Orchestration

This SK plugin approach yields significant advantages:

### 1\. Dynamic & Context-Aware Agent Selection

The kernel’s LLM acts as the intelligent router, using function descriptions and conversation history to select the most relevant agent(s) for each turn or sub-task. The `system_prompt` guides this selection process:

```
# Example system prompt snippet for the orchestrator LLM
system_prompt = """You are an AI assistant orchestrating specialized agents. Analyze the user query.
Based on the query and the descriptions of available tools (plugins), select the most appropriate tool(s).
Available tools:
- ORG_POLICY_AGENT: Use for questions about internal company policies and procedures.
- WEB_SEARCH_AGENT: Use for current events, public facts, and general web knowledge.
- PRIVATE_DATA_AGENT: Use for queries requiring access to internal databases (e.g., sales figures, user data).
- GENERIC_LLM_AGENT: Use as a fallback for general conversation or if no other tool is suitable.
Invoke the chosen tool(s). If multiple tools are needed, plan their execution. Synthesize their outputs into a final, comprehensive response.
"""

```

### 2\. Flexible Execution Flows (Parallel/Sequential)

SK supports different function calling modes. You can configure the kernel to:

- Invoke multiple plugins in parallel if their tasks are independent.
- Chain plugin calls sequentially if one agent’s output is needed as input for another.
- Allow the LLM to automatically decide the best execution strategy.

### 3\. Unified Resource Monitoring

By having plugins report their token usage and execution time back to the orchestrator, you gain centralized visibility into costs and performance bottlenecks across the entire multi-agent system.

## Implementation Patterns

### 1\. Base Class for Agent Invocation Plugins

Create a base class to handle common logic like kernel/message storage, runtime access, state tracking (invocation status, token usage, results), and result processing.

```
from semantic_kernel.kernel_pugin import KernelPlugin
# ... other imports ...
class AgentInvokingPlugin(KernelPlugin):
 def __init__(self, kernel, message, runtime):
 self.kernel = kernel
 self.message = message
 self.runtime = runtime # Agent communication runtime
 self.token_usage = TokenUsage(prompt_token=0, completion_token=0)
 self.search_result = SearchResult(docs=[], citations=[])
 self.was_invoked = False
 # Potentially add abstract methods for processing results, etc.
 def create_message_body(self, query: str) -> dict:
 # Standardize message creation
 pass
 def proccess_and_create_response(self, agent_result: dict) -> str:
 # Standardize response processing, update state (tokens, results)
 # Returns a string summary suitable for the orchestrator LLM
 pass
 def get_summary(self) -> str:
 # Return a summary of results if invoked
 pass
 # ... other common methods ...

```

### 2\. Descriptive Plugin and Function Naming

Use clear, descriptive names for plugin registration ( `plugin_name="WEB_SEARCH_AGENT"`) and kernel functions ( `@kernel_function(name="invoke_web_search_agent", ...)`). This aids both the LLM’s understanding and human debugging.

### 3\. Explicit Function Choice Configuration

Leverage `FunctionChoiceBehavior` (or similar mechanisms in the specific SK SDK version) to control how the LLM selects and executes functions (e.g., `Auto` for dynamic selection, `Required` to force a specific function call).

## Best Practices for Agent Orchestration with SK Plugins

01. **Rich Function Descriptions**: Write detailed, unambiguous descriptions for `@kernel_function`. This is paramount for accurate dynamic routing.
02. **Clear System Prompts**: Guide the orchestrator LLM on the overall goal, available tools, and how to choose between them.
03. **Standardized Inputs/Outputs**: Design plugin functions to accept simple inputs (like strings) where possible and return standardized, predictable outputs (or update state predictably).
04. **Robust Error Handling**: Implement try/except blocks within plugin functions and report errors clearly back to the orchestrator.
05. **Comprehensive Telemetry**: Log key events (plugin invocation, agent requests/responses, errors, timings) for monitoring and debugging. Use correlation IDs.
06. **State Management**: Carefully manage shared state (like conversation history) passed to plugins and how plugins update aggregated results (tokens, citations).
07. **Observability First**: Design plugins with logging and metrics in mind from the outset. Track token usage per plugin/agent.
08. **Agent Contract Testing**: Implement tests for each plugin, mocking the underlying agent, to ensure it adheres to its expected interface and behavior.
09. **Idempotency Considerations**: If agents might be retried, consider designing their actions to be idempotent where possible.
10. **Circuit Breakers**: Implement resilience patterns like circuit breakers for calls to external agents that might be unreliable or slow.

## Conclusion

Semantic Kernel plugins offer a powerful and structured approach to the complex challenge of AI agent orchestration. By encapsulating agent capabilities within a standardized plugin framework, developers can build sophisticated multi-agent systems that benefit from:

- **Modularity**: Easier development, testing, and maintenance.
- **Dynamic Routing**: Intelligent, context-aware selection of specialized agents.
- **Scalability**: A clear pattern for adding new agent capabilities.
- **Observability**: Centralized monitoring of performance and resource consumption.

As AI applications increasingly rely on collaborative ensembles of specialized agents, mastering plugin-based orchestration frameworks like Semantic Kernel will be essential for building the next generation of intelligent, capable, and maintainable systems.

## References:

- [Semantic Kernel](https://learn.microsoft.com/en-us/semantic-kernel/concepts/kernel)
- [Semantic Kernel Plugin](https://learn.microsoft.com/en-us/semantic-kernel/concepts/plugins)
- [Function calling](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/function-calling)

* * *

_This blog post targets software engineers familiar with LLM concepts and agent-based architectures. Code examples are illustrative and simplified; production systems require more extensive error handling, configuration, and state management._

## Author
Highlights: None
Highlight Scores: None
Summary: None

Title: Empowering AI Agents with Tools via OpenAPI: A Hands-On Guide with Microsoft Semantic Kernel Agents | Semantic Kernel
URL: https://devblogs.microsoft.com/semantic-kernel/empowering-ai-agents-with-tools-via-openapi-a-hands-on-guide-with-microsoft-semantic-kernel-agents/
ID: https://devblogs.microsoft.com/semantic-kernel/empowering-ai-agents-with-tools-via-openapi-a-hands-on-guide-with-microsoft-semantic-kernel-agents/
Score: None
Published Date: 2025-01-09T22:43:35.000Z
Author: Sophia Lagerkrans-Pandey
Image: https://devblogs.microsoft.com/semantic-kernel/wp-content/uploads/sites/78/2024/03/Guest-Blog_-Building-Your-Custom-Copilot-with-Semantic-Kernel-1.png
Favicon: None
Extras: None
Subpages: None
Text: Today the Semantic Kernel team is happy to welcome back our guest author, [Akshay Kokane](https://medium.com/@akshaykokane09). We will turn it over to him to dive into his recent Medium article on Semantic Kernel.

As we advance towards an Agentic Approach in the AI world, I would like to share my insights on how Semantic Kernel can assist in building AI agents and leveraging existing APIs to create intelligent agents.

In a previous [article](https://medium.com/@akshaykokane09/step-by-step-guide-to-develop-ai-multi-agent-system-using-microsoft-semantic-kernel-and-gpt-4o-f5991af40ea6), I discussed how Semantic Kernel can develop a multi-agent system that fosters a collaborative environment for these agents to interact and deliver results. In this new blog post, I am pleased to share that by using the OpenAPI specification, we can utilize existing APIs to integrate with agents. These are referred to as tools or plugins, which AI agents can call upon to obtain contextual data.

Using Semantic Kernel, adding plugins via the OpenAPI specification is simplified. Furthermore, these plugins are automatically triggered as and when required using the OpenAI Tool Calling. Semantic Kernel eliminates the complexities associated with tool invocation, streamlining the development of AI agents by removing the need to focus on these intricacies.

In this blog post, I will showcase how to create a chat-based application for an e-commerce platform that manages customer payments through the integration of their existing Payment Service APIs. Here are high level steps to import plugin through OpenApi:

To add a plugin to your kernel:

1\. Add the following NuGet Reference:

```
 
```

2\. Import the Plugin to the Kernel:

```
await kernel.ImportPluginFromOpenApiAsync(
 pluginName: "paymentProcessor",
 uri: new Uri("localhost:8080/swagger/v1/swagger.json"),
 executionParameters: new OpenApiFunctionExecutionParameters() {
 EnablePayloadNamespacing = true
 }
);
```

This approach is transformative for enterprises aiming to leverage their existing APIs without reinventing the wheel. Additionally, the OpenAPI spec enables microservice architecture for your AI agents, facilitating easy scalability and resource management at the plugin level.

Semantic Kernel offers several methods for calling APIs. The blog includes a simple example of non-Auth APIs, but it is also possible to call Auth-based APIs. For more information, refer to the documentation on [Give agents access to OpenAPI APIs \| Microsoft Learn](https://learn.microsoft.com/en-us/semantic-kernel/concepts/plugins/adding-openapi-plugins?pivots=programming-language-csharp) For more details, please read the full [article](http://Empowering AI Agents with Tools via OpenAPI: A Hands-On Guide with Microsoft Semantic Kernel Agents) below.

### Empowering AI Agents with Tools via OpenAPI: A Hands-On Guide with Microsoft Semantic Kernel Agents

I recently explored how the OpenAPI Specification can be utilized to give actionable capabilities to AI agents. In this blog, I aim to share my insights and demonstrate the process.

## Understanding the OpenAPI Specification

TThe **OpenAPI Specification** (formerly known as Swagger) is a standardized, language-agnostic framework for defining HTTP APIs. It allows both humans and machines t discover a service’s capabilities without needing access to its source code or documentation. Properly defined OpenAPI specs enable consumers to interact with services using minimal implementation logic.. [Learn more here](https://swagger.io/specification/).

## Why Use OpenAPI with AI Agents?

Many enterprises already have robust APIs in place. With the growing demand for AI-enabled applications, using OpenAPI-based plugins simplifies the process of empowering AI agents with existing APIs. Semantic Kernel, when integrated with OpenAPI, provides AI agents with detailed API semantics, including endpoint descriptions, data types, and expected responses.

For instance, imagine an e-commerce platform launching a new feature called **ShopChat.AI**, where customers can interact with an AI agent to find and purchase products. The AI agent can handle payments and check order statuses by leveraging the existing **Payment Service APIs** through OpenAPI specs.

## Key Benefits of Combining OpenAPI with Semantic Kernel

Integrating OpenAPI specs with Semantic Kernel and Azure OpenAI provides numerous advantages:

## 1\. Simplified AI Integration

OpenAPI specs offer a standardized method for AI agents to understand and interact with existing APIs, eliminating the need for complex custom integrations.

## 2\. Enhanced Agent Functionality

By leveraging existing APIs, AI agents can handle a wide range of tasks, such as inventory management and payment processing, resulting in more versatile applications.

## 3\. Improved Scalability

As your application grows, integrating new APIs becomes easier with OpenAPI. This ensures that your AI agents can evolve alongside your platform.

## Building an AI-Powered Application with OpenAPI and Semantic Kernel

Example Agent based Application

Let’s consider an example: Suppose you have a payment service for your e-commerce platform already in use. The service exposes two APIs:

1. `payment/accept`: This API accepts credit card information, processes the payment, and returns a `transactionId`.
2. `payment/status`: This API uses the `transactionId` to retrieve the payment status.

Now the e-commerce website is planning to launch new feature “ShopeChat.AI” where you can interact with AI agent like you interact with actual shopkeeper to find best product and buy that product.

## Step 1: Exposing OpenAPI Specs for Your Service

Make sure your Payment Service is exposing the OpenAPI Spec. I am doing it in .net, so in .net you can expose the OpenAPI Spech by using Swagger. Complete guide can be found here [https://learn.microsoft.com/en-us/aspnet/core/tutorials/web-api-help-pages-using-swagger?view=aspnetcore-8.0](https://learn.microsoft.com/en-us/aspnet/core/tutorials/web-api-help-pages-using-swagger?view=aspnetcore-8.0)

This is using SwagsBuckler package, I will add this service

```
builder.Services.AddSwaggerGen(options =>
{
 var xmlFile = $"{System.Reflection.Assembly.GetExecutingAssembly().GetName().Name}.xml";
 var xmlPath = Path.Combine(AppContext.BaseDirectory, xmlFile);
 options.IncludeXmlComments(xmlPath);
});
```

Learn more about configuring Swagger/OpenAPI at [https://aka.ms/aspnetcore/swashbuckle](https://aka.ms/aspnetcore/swashbuckle)

This should create output [http://localhost:5272/swagger/v1/swagger.json](http://localhost:5272/swagger/v1/swagger.json).

```
{
"openapi": "3.0.1",
"info": {
"title": "PaymentProcessor",
"version": "1.0"
},
"paths": {
"/api/Payments/status": {
"get": {
"tags": [
"Payments"
],
"summary": "Retrieves the status of a specific payment.",
"responses": {
"200": {
"description": "Success"
}
}
}
},
"/api/Payments/process": {
"post": {
"tags": [
"Payments"
],
"summary": "Processes a payment request.",
"requestBody": {
"description": "The payment request details.",
"content": {
"application/json": {
"schema": {
"$ref": "#/components/schemas/PaymentRequest"
}
},
"text/json": {
"schema": {
"$ref": "#/components/schemas/PaymentRequest"
}
},
"application/*+json": {
"schema": {
"$ref": "#/components/schemas/PaymentRequest"
}
}
}
},
"responses": {
"200": {
"description": "Success"
}
}
}
}
},
"components": {
"schemas": {
"PaymentRequest": {
"required": [
"transactionId"
],
"type": "object",
"properties": {
"transactionId": {
"minLength": 1,
"type": "string"
},
"amount": {
"minimum": 0.01,
"type": "number",
"format": "double"
}
},
"additionalProperties": false
}
}
}
}
```

## To ensure the Payment Service APIs are invoked correctly, I’ve added a constant static transaction ID for verification purposes:

**TransactionId = “TestService123”**

## Step 2: Optional Deployment to Azure

While optional, deploying your service to Azure ensures accessibility and scalability. You can follow Microsoft’s official guide on deploying ASP.NET Core apps to Azure App Services for a smooth cloud integration.If you plan to host your application in the cloud, deploy it to Azure for accessibility and scalability. While optional, this step ensures seamless integration and availability for testing and deployment.

## **Step 3:** Configuring a Semantic Kernel Agent. **We will call this agent as “SalesAgent”.**

We’ll set up a Semantic Kernel agent, which we’ll refer to as **“SalesAgent”** Here’s how to configure it:

1. Add the required package reference in your project
2. Import the paymentProcessor plugin from your OpenAPI specification:

```
 
```

```
await kernel.ImportPluginFromOpenApiAsync(
 pluginName: "paymentProcessor",
 uri: new Uri("http://payment-backend-f4bjgseugsdhddb4.eastus-01.azurewebsites.net/swagger/v1/swagger.json."),
 executionParameters: new OpenApiFunctionExecutionParameters()
 {
 EnablePayloadNamespacing = true
 }
 );
```

Once your application is launched, the `Kernel` object should display the **paymentProcessor** plugin. This confirms the successful integration of the APIs.

_If you want to learn how to define kernel, checkout my previous_ [_blogs_](https://medium.com/@akshaykokane09/step-by-step-guide-to-develop-ai-multi-agent-system-using-microsoft-semantic-kernel-and-gpt-4o-f5991af40ea6)

**Step 4: Run the app**

Now that everything is set up, deploy your application and begin interacting with the Semantic Kernel agent. The system is designed to handle various tasks seamlessly.

## Sample Application Overview

Here’s a quick summary of the sample application I’ve created. It includes two key plugins:

1. **Inventory Plugin**
Retrieves the latest inventory details. This plugin resides inside SalesAgent service
2. **PaymentProcessor Plugin**
This plugin is hosted on another service. Makes API calls hosted on the PaymentProcessor service for handling transactions.

## **Transaction id confirms that InventoryService’s both APIs were called successfully by our AI Agent!!**

## Conclusion: A Powerful Combination for Streamlined AI Integration

The OpenAPI Specification, along with Semantic Kernel and Azure OpenAI, presents a compelling solution for empowering AI agents with real-world capabilities. This combination offers several key benefits:

- **Simplified AI Integration:** OpenAPI specs provide a standardized way for AI agents to understand and interact with existing APIs, eliminating the need for complex custom integrations.
- **Enhanced Agent Functionality:** By leveraging existing APIs, AI agents can perform a wider range of tasks, such as processing payments or managing inventory. This leads to more versatile and helpful AI experiences.
- **Improved Scalability:** As your application grows, you can easily integrate new APIs using the OpenAPI, allowing your AI agents to keep pace with evolving functionalities.

This blog has provided a step-by-step guide on utilizing OpenAPI specs with Semantic Kernel Agents and Azure OpenAI. By following these steps and embracing this powerful combination, you can empower your AI agents to deliver a more comprehensive and valuable user experience.

## Author
Highlights: None
Highlight Scores: None
Summary: None

Title: Yashints | Semantic kernel series - Part two - Plugins
URL: https://yashints.dev/blog/2024/05/13/semantic-kernel-plugins/
ID: https://yashints.dev/blog/2024/05/13/semantic-kernel-plugins/
Score: None
Published Date: 2024-05-13T00:00:00.000Z
Author: 
Image: https://yashints.dev/static/9dd7e334f99df27d871a581fa1226847/socialpreview.png
Favicon: None
Extras: None
Subpages: None
Text: [![Back to top](data:image/svg+xml,%3C?xml%20version=%221.0%22%20encoding=%22iso-8859-1%22?%3E%0D%0A%3C!--%20Generator:%20Adobe%20Illustrator%2019.0.0,%20SVG%20Export%20Plug-In%20.%20SVG%20Version:%206.00%20Build%200)%20%20--%3E%0D%0A%3Csvg%20version=%221.1%22%20id=%22Layer_1%22%20xmlns=%22http://www.w3.org/2000/svg%22%20xmlns:xlink=%22http://www.w3.org/1999/xlink%22%20x=%220px%22%20y=%220px%22%0D%0A%09%20viewBox=%220%200%20511.999%20511.999%22%20style=%22enable-background:new%200%200%20511.999%20511.999;%22%20xml:space=%22preserve%22%3E%0D%0A%3Cpath%20style=%22fill:%23FF9737;%22%20d=%22M310.641,387.709c-0.816-2.159-2.885-3.587-5.192-3.587H206.55c-2.309,0-4.375,1.428-5.194,3.587%0D%0A%09c-4.157,10.99-6.266,22.565-6.266,34.405c0,38.873,23.042,73.976,58.701,89.428c0.705,0.305,1.457,0.457,2.208,0.457%0D%0A%09c0.752,0,1.504-0.152,2.208-0.457c35.66-15.452,58.701-50.554,58.701-89.428C316.909,410.27,314.8,398.695,310.641,387.709z%22/%3E%0D%0A%3Cpath%20style=%22fill:%23FFD960;%22%20d=%22M292.446,380.352c-1.052-1.136-2.528-1.782-4.076-1.782h-64.742c-1.548,0-3.025,0.645-4.076,1.782%0D%0A%09c-1.049,1.135-1.579,2.659-1.459,4.202c1.681,21.554,15.743,40.738,35.824,48.871c0.668,0.271,1.376,0.406,2.084,0.406%0D%0A%09c0.708,0,1.416-0.135,2.084-0.406c20.08-8.133,34.14-27.316,35.822-48.871C294.024,383.01,293.495,381.487,292.446,380.352z%22/%3E%0D%0A%3Cpath%20style=%22opacity:0.1;fill:%23231F20;enable-background:new%20%20%20%20;%22%20d=%22M213.598,428.947c0-12.774,2.275-25.264,6.763-37.122%0D%0A%09c0.883-2.33,3.113-3.87,5.603-3.87h84.765c-0.03-0.081-0.056-0.164-0.087-0.246c-0.816-2.159-2.885-3.587-5.192-3.587h-98.899%0D%0A%09c-2.309,0-4.375,1.428-5.194,3.587c-4.157,10.99-6.266,22.565-6.266,34.405c0,38.752,22.902,73.752,58.37,89.277%0D%0A%09C228.653,491.753,213.598,461.585,213.598,428.947z%22/%3E%0D%0A%3Cg%3E%0D%0A%09%3Cpath%20style=%22fill:%233A5D74;%22%20d=%22M420.78,396.97v-51.543c0-22.857-11.084-37.559-14.882-41.925l-76.866-83.428v152.156l80.955,37.293%0D%0A%09%09C413.007,410.695,420.78,412.236,420.78,396.97z%22/%3E%0D%0A%09%3Cpath%20style=%22fill:%233A5D74;%22%20d=%22M91.219,396.97v-51.543c0-22.857,11.084-37.559,14.882-41.925l76.866-83.428v152.156l-80.953,37.293%0D%0A%09%09C98.992,410.695,91.219,412.236,91.219,396.97z%22/%3E%0D%0A%3C/g%3E%0D%0A%3Cpath%20style=%22fill:%2390C8EC;%22%20d=%22M255.999,103.143c-4.599,0-8.328-3.729-8.328-8.328V8.328c0-4.599,3.729-8.328,8.328-8.328%0D%0A%09s8.328,3.729,8.328,8.328v86.487C264.327,99.414,260.598,103.143,255.999,103.143z%22/%3E%0D%0A%3Cpath%20style=%22fill:%23CAE9F7;%22%20d=%22M263.525,49.363h-15.052c-37.406,0-67.728,30.323-67.728,67.727v255.14%0D%0A%09c0,10.247,8.306,18.555,18.557,18.555h113.395c10.248,0,18.557-8.308,18.557-18.555V170.738v-27.205v-26.444%0D%0A%09C331.253,79.685,300.931,49.363,263.525,49.363z%22/%3E%0D%0A%3Cpath%20style=%22fill:%2390C8EC;%22%20d=%22M180.746,345.426v26.803c0,10.247,8.306,18.555,18.557,18.555h113.395%0D%0A%09c10.248,0,18.557-8.308,18.557-18.555v-26.803H180.746z%22/%3E%0D%0A%3Ccircle%20style=%22fill:%233A5D74;%22%20cx=%22256%22%20cy=%22269.137%22%20r=%2232.988%22/%3E%0D%0A%3Cg%3E%0D%0A%09%3Cpath%20style=%22opacity:0.1;fill:%23231F20;enable-background:new%20%20%20%20;%22%20d=%22M109.726,405.405v-51.543%0D%0A%09%09c0-22.857,11.084-37.559,14.882-41.925l58.358-63.341v-28.523l-76.866,83.428c-3.798,4.365-14.882,19.067-14.882,41.925v51.543%0D%0A%09%09c0,15.265,7.773,13.725,10.795,12.552l7.722-3.558C109.733,405.777,109.726,405.598,109.726,405.405z%22/%3E%0D%0A%09%3Cpath%20style=%22opacity:0.1;fill:%23231F20;enable-background:new%20%20%20%20;%22%20d=%22M199.253,372.229v-255.14c0-36.824,29.397-66.763,66-67.682%0D%0A%09%09c-0.576-0.014-1.147-0.044-1.728-0.044h-15.052c-37.406,0-67.728,30.323-67.728,67.727v255.14c0,10.247,8.306,18.555,18.557,18.555%0D%0A%09%09h18.508C207.559,390.784,199.253,382.477,199.253,372.229z%22/%3E%0D%0A%09%3Cpath%20style=%22opacity:0.1;fill:%23231F20;enable-background:new%20%20%20%20;%22%20d=%22M241.519,269.141c0-15.005,10.021-27.662,23.733-31.664%0D%0A%09%09c-2.937-0.856-6.04-1.325-9.253-1.325c-18.22,0-32.988,14.769-32.988,32.989c0,18.219,14.768,32.988,32.988,32.988%0D%0A%09%09c3.214,0,6.316-0.467,9.253-1.325C251.539,296.802,241.519,284.146,241.519,269.141z%22/%3E%0D%0A%3C/g%3E%0D%0A%3Cg%3E%0D%0A%3C/g%3E%0D%0A%3Cg%3E%0D%0A%3C/g%3E%0D%0A%3Cg%3E%0D%0A%3C/g%3E%0D%0A%3Cg%3E%0D%0A%3C/g%3E%0D%0A%3Cg%3E%0D%0A%3C/g%3E%0D%0A%3Cg%3E%0D%0A%3C/g%3E%0D%0A%3Cg%3E%0D%0A%3C/g%3E%0D%0A%3Cg%3E%0D%0A%3C/g%3E%0D%0A%3Cg%3E%0D%0A%3C/g%3E%0D%0A%3Cg%3E%0D%0A%3C/g%3E%0D%0A%3Cg%3E%0D%0A%3C/g%3E%0D%0A%3Cg%3E%0D%0A%3C/g%3E%0D%0A%3Cg%3E%0D%0A%3C/g%3E%0D%0A%3Cg%3E%0D%0A%3C/g%3E%0D%0A%3Cg%3E%0D%0A%3C/g%3E%0D%0A%3C/svg%3E%0D%0A)](https://yashints.dev/blog/2024/05/13/semantic-kernel-plugins/#top)

[![Yaser Adel Mehraban's headshot](https://yashints.dev/me.jpg)\
Yashints](https://yashints.dev/)

[Home](https://yashints.dev/) [About](https://yashints.dev/about/) [Services](https://yashints.dev/services/) [Speaking](https://yashints.dev/speaking/) [Blog](https://yashints.dev/blog/) [Contact](https://yashints.dev/contact/)![light](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20width=%2224%22%20height=%2224%22%20viewBox=%220%200%20480%20480%22%3E%3Cpath%20d=%22M459.8%20347.3a16%2016%200%200%200-17.8-5A176.2%20176.2%200%200%201%20208.7%20176c0-58.3%2028.8-112.7%2077-145.4a16%2016%200%200%200-6.6-29C271.6.3%20264%200%20256.6%200c-132.3%200-240%20107.6-240%20240s107.7%20240%20240%20240c84%200%20160.5-42.7%20204.4-114.2%203.6-5.8%203-13.2-1.2-18.5z%22/%3E%3C/svg%3E)

[Home](https://yashints.dev/) [About](https://yashints.dev/about/) [Services](https://yashints.dev/services/) [Speaking](https://yashints.dev/speaking/) [Blog](https://yashints.dev/blog/) [Contact](https://yashints.dev/contact/)![light](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20width=%2224%22%20height=%2224%22%20viewBox=%220%200%20480%20480%22%3E%3Cpath%20d=%22M459.8%20347.3a16%2016%200%200%200-17.8-5A176.2%20176.2%200%200%201%20208.7%20176c0-58.3%2028.8-112.7%2077-145.4a16%2016%200%200%200-6.6-29C271.6.3%20264%200%20256.6%200c-132.3%200-240%20107.6-240%20240s107.7%20240%20240%20240c84%200%20160.5-42.7%20204.4-114.2%203.6-5.8%203-13.2-1.2-18.5z%22/%3E%3C/svg%3E)

![](https://yashints.dev/static/5d276e3388107f4c25e22e895f6d8490/sk.png)

## Semantic kernel series - Part two - Plugins

![Published](data:image/svg+xml,%3Csvg%20height=%22512pt%22%20viewBox=%220%200%20512%20512%22%20width=%22512pt%22%20xmlns=%22http://www.w3.org/2000/svg%22%3E%3Cpath%20d=%22m0%20121h482v391h-482zm0%200%22%20fill=%22%237ed8f6%22/%3E%3Cpath%20d=%22m287%20121h195v391h-195zm0%200%22%20fill=%22%236aa9ff%22/%3E%3Cpath%20d=%22m512%2060v121l-30%2030h-390l-30-30v-121h120l15.902344-30%2014.097656%2030h90l17.699219-30%2012.300781%2030h90l12.300781-30%2017.699219%2030zm0%200%22%20fill=%22%234a696f%22/%3E%3Cpath%20d=%22m512%2060v121l-30%2030h-195v-151h15l17.699219-30%2012.300781%2030h90l12.300781-30%2017.699219%2030zm0%200%22%20fill=%22%23384949%22/%3E%3Cpath%20d=%22m407%200c-24.8125%200-45%2020.1875-45%2045v61c0%2024.8125%2020.1875%2045%2045%2045v-30c-8.277344%200-15-6.722656-15-15v-61c0-8.277344%206.722656-15%2015-15s15%206.722656%2015%2015v15h30v-15c0-24.8125-20.1875-45-45-45zm0%200%22%20fill=%22%23f4d7af%22/%3E%3Cpath%20d=%22m332%2045v15h-30v-15c0-8.402344-6.597656-15-15-15s-15%206.597656-15%2015v61c0%208.402344%206.597656%2015%2015%2015v30c-24.902344%200-45-20.097656-45-45v-61c0-24.902344%2020.097656-45%2045-45s45%2020.097656%2045%2045zm0%200%22%20fill=%22%23faecd8%22/%3E%3Cpath%20d=%22m167%200c-24.8125%200-45%2020.1875-45%2045v61c0%2024.8125%2020.1875%2045%2045%2045v-30c-8.277344%200-15-6.722656-15-15v-61c0-8.277344%206.722656-15%2015-15s15%206.722656%2015%2015v15h30v-15c0-24.8125-20.1875-45-45-45zm0%200%22%20fill=%22%23faecd8%22/%3E%3Cpath%20d=%22m287%2030v-30c24.902344%200%2045%2020.097656%2045%2045v15h-30v-15c0-8.402344-6.597656-15-15-15zm0%200%22%20fill=%22%23f4d7af%22/%3E%3Cpath%20d=%22m512%20181v150l-90%2030-30%2090h-330v-270zm0%200%22%20fill=%22%236aa9ff%22/%3E%3Cpath%20d=%22m512%20181v150l-90%2030-30%2090h-105v-270zm0%200%22%20fill=%22%234895ff%22/%3E%3Cpath%20d=%22m306.800781%20330.398438c-7.203125.902343-14.101562-.597657-19.800781-4.199219-8.699219-5.101563-15-14.398438-15-25.199219%200-10.5%205.699219-20.402344%2015-25.5.300781-.300781.601562-.601562%201.199219-.902344l27.601562-14.398437-28.5-12.601563h-.300781c-9.601562-4.496094-19.5-6.597656-30-6.597656-41.398438%200-75%2033.601562-75%2075s33.601562%2075%2075%2075c10.5%200%2020.699219-2.101562%2030-6.300781%2014.699219-6.597657%2027-17.699219%2035.097656-32.101563l15.300782-26.996094zm0%200%22%20fill=%22%23faecd8%22/%3E%3Cpath%20d=%22m332%20271h30v30h-30zm0%200%22%20fill=%22%23f4d7af%22/%3E%3Cpath%20d=%22m512%20331v120h-120l35.902344-95.902344zm0%200%22%20fill=%22%236aa9ff%22/%3E%3Cpath%20d=%22m512%20331-120%20120v-120zm0%200%22%20fill=%22%237ed8f6%22/%3E%3Cg%20fill=%22%23f4d7af%22%3E%3Cpath%20d=%22m288.199219%20274.601562c-.597657.296876-.898438.597657-1.199219.898438v-27.902344h.300781l28.5%2012.601563zm0%200%22/%3E%3Cpath%20d=%22m337.398438%20325.601562-15.296876%2026.996094c-8.101562%2014.402344-20.402343%2025.503906-35.101562%2032.101563v-58.5c5.699219%203.601562%2012.597656%205.101562%2019.800781%204.199219zm0%200%22/%3E%3C/g%3E%3C/svg%3E)_May 13, 2024_![Time to read](data:image/svg+xml,%3C?xml%20version=%221.0%22%20encoding=%22iso-8859-1%22?%3E%0D%0A%3C!--%20Generator:%20Adobe%20Illustrator%2019.0.0,%20SVG%20Export%20Plug-In%20.%20SVG%20Version:%206.00%20Build%200)%20%20--%3E%0D%0A%3Csvg%20version=%221.1%22%20id=%22Capa_1%22%20xmlns=%22http://www.w3.org/2000/svg%22%20xmlns:xlink=%22http://www.w3.org/1999/xlink%22%20x=%220px%22%20y=%220px%22%0D%0A%09%20viewBox=%220%200%2059%2059%22%20style=%22enable-background:new%200%200%2059%2059;%22%20xml:space=%22preserve%22%3E%0D%0A%3Cline%20style=%22fill:none;stroke:%23424A60;stroke-width:2;stroke-linecap:round;stroke-miterlimit:10;%22%20x1=%2248.515%22%20y1=%2213.615%22%20x2=%2252.05%22%20y2=%2210.08%22/%3E%0D%0A%3Crect%20x=%2250.464%22%20y=%225.665%22%20transform=%22matrix(0.7071%20-0.7071%200.7071%200.7071%209.5322%2040.3433)%22%20style=%22fill:%23AFB6BB;%22%20width=%226.001%22%20height=%226%22/%3E%0D%0A%3Cpath%20style=%22fill:%233083C9;%22%20d=%22M30.13,6c-2.008,0-3.96,0.235-5.837,0.666V13h-8c-0.553,0-1,0.447-1,1s0.447,1,1,1h8v5h-13%0D%0A%09c-0.553,0-1,0.447-1,1s0.447,1,1,1h13v5h-18c-0.553,0-1,0.447-1,1s0.447,1,1,1h18v5h-22c-0.553,0-1,0.447-1,1s0.447,1,1,1h22v5h-16%0D%0A%09c-0.553,0-1,0.447-1,1s0.447,1,1,1h16v5h-10c-0.553,0-1,0.447-1,1s0.447,1,1,1h10v7.334C26.17,57.765,28.122,58,30.13,58%0D%0A%09c14.359,0,26-11.641,26-26S44.489,6,30.13,6z%22/%3E%0D%0A%3Cpath%20style=%22fill:%232B77AA;%22%20d=%22M44,23.172c-0.348-0.346-0.896-0.39-1.293-0.104L29.76,32.433c-0.844,0.614-1.375,1.563-1.456,2.604%0D%0A%09s0.296,2.06,1.033,2.797c0.673,0.673,1.567,1.044,2.518,1.044c1.138,0,2.216-0.549,2.886-1.47l9.363-12.944%0D%0A%09C44.391,24.067,44.348,23.519,44,23.172z%22/%3E%0D%0A%3Cpath%20style=%22fill:%23EFCE4A;%22%20d=%22M43,21.293c-0.348-0.346-0.896-0.39-1.293-0.104L28.76,30.554c-0.844,0.614-1.375,1.563-1.456,2.604%0D%0A%09s0.296,2.06,1.033,2.797C29.01,36.629,29.904,37,30.854,37c1.138,0,2.216-0.549,2.886-1.47l9.363-12.944%0D%0A%09C43.391,22.188,43.348,21.64,43,21.293z%22/%3E%0D%0A%3Cpath%20style=%22fill:%23424A60;%22%20d=%22M28.293,6.084C28.954,6.034,29.619,6,30.293,6s1.339,0.034,2,0.084V3h2.5c0.828,0,1.5-0.672,1.5-1.5%0D%0A%09v0c0-0.828-0.672-1.5-1.5-1.5h-9c-0.828,0-1.5,0.672-1.5,1.5v0c0,0.828,0.672,1.5,1.5,1.5h2.5V6.084z%22/%3E%0D%0A%3Cg%3E%0D%0A%09%3Cpath%20style=%22fill:%23A1C8EC;%22%20d=%22M30.293,5c-0.553,0-1,0.447-1,1v3c0,0.553,0.447,1,1,1s1-0.447,1-1V6%0D%0A%09%09C31.293,5.447,30.846,5,30.293,5z%22/%3E%0D%0A%09%3Cpath%20style=%22fill:%23A1C8EC;%22%20d=%22M30.293,54c-0.553,0-1,0.447-1,1v3c0,0.553,0.447,1,1,1s1-0.447,1-1v-3%0D%0A%09%09C31.293,54.447,30.846,54,30.293,54z%22/%3E%0D%0A%09%3Cpath%20style=%22fill:%23A1C8EC;%22%20d=%22M56.13,31h-3c-0.553,0-1,0.447-1,1s0.447,1,1,1h3c0.553,0,1-0.447,1-1S56.683,31,56.13,31z%22/%3E%0D%0A%09%3Cpath%20style=%22fill:%23A1C8EC;%22%20d=%22M43.63,8.617c-0.479-0.277-1.09-0.112-1.366,0.366l-1.5,2.599c-0.276,0.479-0.112,1.09,0.366,1.366%0D%0A%09%09c0.157,0.091,0.329,0.134,0.499,0.134c0.346,0,0.682-0.18,0.867-0.5l1.5-2.599C44.272,9.505,44.108,8.893,43.63,8.617z%22/%3E%0D%0A%09%3Cpath%20style=%22fill:%23A1C8EC;%22%20d=%22M53.146,44.134l-2.598-1.5c-0.478-0.277-1.09-0.114-1.366,0.366%0D%0A%09%09c-0.276,0.479-0.112,1.09,0.366,1.366l2.598,1.5C52.304,45.957,52.475,46,52.645,46c0.346,0,0.682-0.179,0.867-0.5%0D%0A%09%09C53.789,45.021,53.625,44.41,53.146,44.134z%22/%3E%0D%0A%09%3Cpath%20style=%22fill:%23A1C8EC;%22%20d=%22M42.496,51.419c-0.277-0.48-0.89-0.644-1.366-0.366c-0.479,0.276-0.643,0.888-0.366,1.366l1.5,2.598%0D%0A%09%09c0.186,0.321,0.521,0.5,0.867,0.5c0.17,0,0.342-0.043,0.499-0.134c0.479-0.276,0.643-0.888,0.366-1.366L42.496,51.419z%22/%3E%0D%0A%09%3Cpath%20style=%22fill:%23A1C8EC;%22%20d=%22M50.05,21.5c0.17,0,0.342-0.043,0.499-0.134l2.598-1.5c0.479-0.276,0.643-0.888,0.366-1.366%0D%0A%09%09c-0.276-0.479-0.89-0.644-1.366-0.366l-2.598,1.5C49.07,19.91,48.906,20.521,49.183,21C49.368,21.321,49.704,21.5,50.05,21.5z%22/%3E%0D%0A%3C/g%3E%0D%0A%3Cg%3E%0D%0A%3C/g%3E%0D%0A%3Cg%3E%0D%0A%3C/g%3E%0D%0A%3Cg%3E%0D%0A%3C/g%3E%0D%0A%3Cg%3E%0D%0A%3C/g%3E%0D%0A%3Cg%3E%0D%0A%3C/g%3E%0D%0A%3Cg%3E%0D%0A%3C/g%3E%0D%0A%3Cg%3E%0D%0A%3C/g%3E%0D%0A%3Cg%3E%0D%0A%3C/g%3E%0D%0A%3Cg%3E%0D%0A%3C/g%3E%0D%0A%3Cg%3E%0D%0A%3C/g%3E%0D%0A%3Cg%3E%0D%0A%3C/g%3E%0D%0A%3Cg%3E%0D%0A%3C/g%3E%0D%0A%3Cg%3E%0D%0A%3C/g%3E%0D%0A%3Cg%3E%0D%0A%3C/g%3E%0D%0A%3Cg%3E%0D%0A%3C/g%3E%0D%0A%3C/svg%3E%0D%0A) _6 min read_

In my previous post, I introduced you to foundational concepts of [Semantic Kernel](https://learn.microsoft.com/en-us/semantic-kernel/overview/), offering a glimpse into its potential. Now, when I was learning about the what and the why, that wasn’t enough for me to fully understand the concepts and that’s why I started writing these series.

Semantic Kernel Series:

✔️ Part one: [Intro](https://yashints.dev/blog/2024/04/30/semantic-kernel)

✔️ Part two: [Plugins](https://yashints.dev/blog/2024/05/13/semantic-kernel-plugins)

✔️ Part three: [Planners and Native Function plugins](https://yashints.dev/blog/2024/05/27/semantic-kernel-planners/)

[You can find the code on my GitHub repository here](https://github.com/yashints/semantic-kernel-devops).

In order for us to learn about the concepts, the best way is with a story, and I chose DevOps because I was interested in finding better ways to automate daily tasks in that space for my course. Let’s go through the context and see what we’re trying to achieve.

## Context

I want to use Semantic Kernel to generate Azure DevOps pipelines/GitHub Actions workflow for my application with simple and details instructions (aka prompts). Now the application might have multiple tiers and each might have dependency with one another and I wanted to see how this will work out.

The first thing we need after we have our starter project ( [use my previous post to create yours](https://yashints.dev/blog/2024/05/13/04/semantic-kernel.md)), is to define our prompts. I want to use plugins at this point since it is very easy with them to get my prompts introduced to the kernel and execute them based on different inputs.

## Setup

Here is what we need to get the whole setup working:

- An instance of the kernel.
- An instance of the Azure OpenAI or OpenAI to setup the kernel with.
- A plugin with different functions for Azure DevOps and GitHub Actions.
- Input from the user describing the application and its structure.

## Prompts

As I mentioned we would use plugins and their functions to be able to get our input passed to our Azure OpenAI service via the kernel. Technically we could add these as inline code and it works perfectly, however, that would mean we have to define these one by one and it just blows our code base. A much better way is to use the built in feature of the kernel which allows us to load multiple plugins with their functions from a directory.

All you need is a folder which contains all your plugins, and for each plugin, a subdirectory per function. Every function which is mapped to our prompts will need two files:

- `config.json` which contains a description, type, and the parameters for completion or chat depending on what you intend to use.
- `skprompt.txt` which has the prompt in natural language.

## Plugin setup

Let’s set our plugin and its function up. As mentioned we intend to generate either an Azure DevOps Pipeline, or GitHub Actions workflow, so one plugin and two function will do the job. Our directory structure will look like this:

[![Prompt directory structure](https://yashints.dev/static/40f98b10d1028af20e1bdfed583f50b2/4651d/dir.png)](https://yashints.dev/static/40f98b10d1028af20e1bdfed583f50b2/4651d/dir.png)

_DevOps_ is the name of our plugin, and _AzDevOps_ and _GitHubActions_ are our function names.

## Prompt text

You can write your prompts however you like, just make sure you follow the principles of [prompt engineering](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/prompt-engineering) which in short is all about the details and be as specific as you can.

Here is how mine looks like for GitHub Actions:

Copy

```
INSTRUCTIONS:

Generate workflow YAML files to deploy an application to Azure from GitHub Actions.

RULES:

- All YAML files must be complete
- YAML files must be listed one by one
- Every file is indicated with "FILE:" followed by it's path
- Every file content must begin and end with #-----#
- All pipelines should use either GitHub hosted runners with latest ubuntu version.
- All YAML files should contain two stages for build and deploy where deploy depends on build

DESCRIPTION:{{$input}}
```

The details of how the workflow is going to be generated is outlined in details and at the end I have left a placeholder for a variable called `$input` which will be passed by the user to the kernel later.

And here is what the `config.json` looks like for this prompt:

Copy

```
{
 "schema": 1,
 "description": "Create pipeline YAML files for GitHub Actions",
 "type": "completion",
 "completion": {
 "max_tokens": 1000,
 "temperature": 0.5,
 "top_p": 0,
 "presence_penalty": 0,
 "frequency_penalty": 0
 },
 "input": {
 "parameters": [
 {
 "name": "input",
 "description": "The description of the deployment to be be created",
 "defaultValue": ""
 }
 ]
 }
}
```

You don’t need to know the details of the parameters for now, all that is important is the definition of the input parameter and the fact that we intend to use the completion feature of Azure OpenAI.

## Input

For our inputs, I also would like to use files, but you don’t have to follow this convention, this just keeps the code clean and short so it’s more understandable for me and other beginners learning the concepts.

I have created a folder called desc which includes two files one for an application written with `.Net 8` and one for a `node` based application.

Here is the content of the `node` based input file:

Copy

```
This is an application written in NodeJs and has below components:

- A front end app which is written in React and uses create-react-app starter. This will be hosted in an Azure Static Web App and is stored in the `frontend` directory.
- A backend API which is going to be hosted in an Azure Function as the backend for the static web app in the `api` directory.
- The API uses a Cosmos DB database as its datastore.
```

## Setting up the kernel

In order to setup the kernel we need a few things:

- The information about the Azure OpenAI service like endpoint, key and model number.
- A way for the user to specify which input and prompt to use.
- Setting up the kernel so it knows about our Azure OpenAI service and our plugin directory.
- Calling the kernel and getting the result.

We already covered how to setup the Azure OpenAI part with the kernel in our first post, here I just show you how to load the plugins from the directory:

Copy

```
//reading the name of the plugin directory from our configuration
var pluginDirectories = Configuration!.GetSection("PluginSettings:Root").Get ();

// loading the plugins from the plugin directory
var skillImport = kernel.ImportPluginFromPromptDirectory(pluginDirectories!);

// read user's task description from given file
string description = await File.ReadAllTextAsync(file.FullName!);

// this is a data structure that holds temporary data while the kernel task runs
var context = new KernelArguments();

// associate user's description with "input" variable
string key = "input";
context.Add(key, description);

// call the kernel and tell it which plugin function to call and pass to the LLM
var result = await kernel.InvokeAsync(skillImport[function], context);
Console.WriteLine(result.GetValue ());
```

## Output

You can find the [full code for this post here](https://github.com/yashints/semantic-kernel-devops). Simply clone the code, build and run it passing the required information like so:

Copy

```
git clone https://github.com/yashints/semantic-kernel-devops.git

cd semantic-kernel-devops

dotnet restore

dotnet build

dotnet run -- -i .\desc\dotnet.txt -f GitHubActions
```

I am passing the `.Net` application prompt and tell the kernel to create a GitHub Actions workflow.

The result will look like this:

Copy

```
FILE: .github/workflows/dotnet.yml
#-----#
name: Build and Deploy

on:
 push:
 branches:
 - master

jobs:
 build:
 name: Build
 runs-on: ubuntu-latest
 strategy:
 matrix:
 dotnet-version: ['8.x']

 steps:
 - name: Checkout code
 uses: actions/checkout@v2

 - name: Setup .NET Core
 uses: actions/setup-dotnet@v1
 with:
 dotnet-version: ${{ matrix.dotnet-version }}

 - name: Restore dependencies
 run: dotnet restore

 - name: Build
 run: dotnet build --configuration Release --no-restore

 - name: Test
 run: dotnet test --no-restore --verbosity normal

 deploy:
 needs: build
 runs-on: ubuntu-latest
 steps:
 - name: Login via Az module
 uses: azure/login@v1
 with:
 creds: ${{ secrets.AZURE_CREDENTIALS }}

 - name: 'Run Azure Functions Action'
 uses: Azure/functions-action@v1
 id: fa
 with:
 app-name: 'myFunctionApp'
 package: 'api'
 publish-profile: ${{ secrets.AZURE_FUNCTIONAPP_PUBLISH_PROFILE }}

 - name: 'Deploy to Azure Web App'
 uses: azure/webapps-deploy@v2
 with:
 app-name: 'myWebApp'
 package: 'frontend'
 publish-profile: ${{ secrets.AZURE_WEBAPP_PUBLISH_PROFILE }}
#-----#
```

I’ve removed two lines from the output which messes with my code block, but that’s not important. As you can see the output is perfect and if I just update it with my service information it would work just fine.

**Note:** You need to update the `appsettings.json` or add a development version and update it with your service information to get the full code working. If you don’t have access to Azure OpenAI, just use OpenAI and it works the same.

## What next?

So far we have created our prompts, dynamically loaded them as plugins and functions and then called our kernel passing the input to be passed to our LLM. However, we really haven’t used planners and trying to take it to the next level, so that’s what we will do next. If you liked this post, please share and spread the word too.

Support my work 👇🏽

[![](data:image/svg+xml,%3Csvg%20id=%22Capa_1%22%20enable-background=%22new%200%200%20512.078%20512.078%22%20height=%22512%22%20viewBox=%220%200%20512.078%20512.078%22%20width=%22512%22%20xmlns=%22http://www.w3.org/2000/svg%22%3E%3Cg%3E%3Cg%3E%3Cg%3E%3Cpath%20d=%22m354.677%20314.852c-86.93%200-157.401-70.471-157.401-157.401s70.471-157.401%20157.401-157.401%2086.931%20314.802%200%20314.802z%22%20fill=%22%23fde53f%22/%3E%3Cg%3E%3Cpath%20d=%22m354.677.05v314.802c86.93%200%20157.401-70.471%20157.401-157.401s-70.47-157.401-157.401-157.401z%22%20fill=%22%23fed330%22/%3E%3C/g%3E%3C/g%3E%3Cg%3E%3Cpath%20d=%22m398.438%2088.34v-24.157h-29.991v23.965h-26.995v-23.965h-29.991v23.965h-24.995v29.991h24.995v78.306h-24.995v29.991h24.995v23.964h29.991v-23.965h26.995v23.965h29.991v-24.157c21.344-2.006%2038.104-20.017%2038.104-41.877%200-10.305-3.73-19.752-9.904-27.074%206.173-7.323%209.904-16.769%209.904-27.074%200-21.861-16.76-39.873-38.104-41.878zm-3.966%2029.798c6.66%200%2012.079%205.419%2012.079%2012.079s-5.419%2012.079-12.079%2012.079h-53.02v-24.158zm0%2078.306h-53.02v-24.158h53.02c6.66%200%2012.079%205.419%2012.079%2012.079%200%206.661-5.419%2012.079-12.079%2012.079z%22%20fill=%22%23fd9e28%22/%3E%3Cg%3E%3Cpath%20d=%22m368.447%20250.4h29.991v-24.157c21.344-2.006%2038.104-20.017%2038.104-41.877%200-10.305-3.73-19.752-9.904-27.074%206.173-7.323%209.904-16.769%209.904-27.074%200-21.86-16.76-39.872-38.104-41.877v-24.158h-29.991v23.965h-13.769v29.991h39.795c6.66%200%2012.079%205.419%2012.079%2012.079s-5.419%2012.079-12.079%2012.079h-39.795v29.991h39.795c6.66%200%2012.079%205.419%2012.079%2012.079s-5.419%2012.079-12.079%2012.079h-39.795v29.991h13.769z%22%20fill=%22%23fd8d34%22/%3E%3C/g%3E%3C/g%3E%3C/g%3E%3Cg%3E%3Cpath%20d=%22m0%20482.387%20107.492-35.914%20174.457%2065.554%20229.895-47.37-1.209-5.042c-9.298-38.776-47.467-63.387-86.65-55.869l-124.907%2023.996-243.57-96.837-55.508%2018.922z%22%20fill=%22%23ffdfcf%22/%3E%3Cpath%20d=%22m55.508%20330.907%2048.207-17.052c32.305-11.427%2067.781-9.915%2098.995%204.221l101.62%2046.019c17.103%207.745%2024.724%2027.851%2017.048%2044.977-7.627%2017.017-27.522%2024.749-44.649%2017.354z%22%20fill=%22%23ffcebf%22/%3E%3C/g%3E%3C/g%3E%3C/svg%3E) Crypto](https://commerce.coinbase.com/checkout/f305ab16-b8a6-460a-a517-af767ec3c0c7) ![](data:image/svg+xml,%3Csvg%20id=%22Capa_1%22%20enable-background=%22new%200%200%20512%20512%22%20height=%22512%22%20viewBox=%220%200%20512%20512%22%20width=%22512%22%20xmlns=%22http://www.w3.org/2000/svg%22%3E%3Cpath%20d=%22m209.7%20512h-84.648c-4.205%200-8.218-1.766-11.06-4.866-2.841-3.101-4.25-7.252-3.884-11.441l36.132-412.975c.679-7.748%207.166-13.692%2014.943-13.692h196.687c35.688%200%2068.12%2013.944%2091.322%2039.265%2023.313%2025.442%2034.426%2059.193%2031.29%2095.036-3.085%2035.254-19.651%2068.342-46.649%2093.167-27.012%2024.838-61.321%2038.518-96.609%2038.518h-98.294l-14.286%20163.297c-.679%207.747-7.166%2013.691-14.944%2013.691z%22%20fill=%22%23507be9%22/%3E%3Cpath%20d=%22m357.87%2069.025h-101.873v265.985h81.227c35.288%200%2069.598-13.68%2096.609-38.518%2026.998-24.825%2043.564-57.913%2046.649-93.167%203.136-35.843-7.977-69.594-31.29-95.036-23.201-25.319-55.634-39.264-91.322-39.264z%22%20fill=%22%233266c8%22/%3E%3Cpath%20d=%22m130.645%20442.975h-84.648c-4.205%200-8.218-1.766-11.06-4.866-2.841-3.101-4.25-7.252-3.884-11.441l36.132-412.976c.679-7.748%207.166-13.692%2014.943-13.692h196.687c35.688%200%2068.121%2013.944%2091.323%2039.266%2023.313%2025.441%2034.426%2059.192%2031.29%2095.034-3.085%2035.255-19.651%2068.342-46.648%2093.168-27.012%2024.838-61.322%2038.518-96.61%2038.518h-98.295l-14.286%20163.297c-.68%207.747-7.167%2013.692-14.944%2013.692z%22%20fill=%22%237dbeff%22/%3E%3Cpath%20d=%22m278.815%200h-22.817v265.985h2.172c35.288%200%2069.599-13.68%2096.61-38.518%2026.997-24.826%2043.563-57.913%2046.648-93.168%203.136-35.842-7.977-69.593-31.29-95.034-23.202-25.321-55.635-39.265-91.323-39.265z%22%20fill=%22%236496f7%22/%3E%3Cpath%20d=%22m161.183%2069.025c-7.777%200-14.265%205.944-14.943%2013.692l-31.519%20360.257h15.924c7.777%200%2014.265-5.944%2014.943-13.692l14.286-163.297h98.295c35.288%200%2069.599-13.68%2096.61-38.518%2026.997-24.826%2043.563-57.913%2046.648-93.168%201.875-21.434-1.349-42.117-9.227-60.726-10.937-2.995-22.452-4.549-34.331-4.549h-196.686z%22%20fill=%22%236496f7%22/%3E%3Cpath%20d=%22m357.87%2069.025h-101.873v196.96h2.172c35.288%200%2069.599-13.68%2096.61-38.518%2026.997-24.826%2043.563-57.913%2046.648-93.168%201.875-21.434-1.349-42.117-9.227-60.726-10.936-2.994-22.451-4.548-34.33-4.548z%22%20fill=%22%23507be9%22/%3E%3C/svg%3E)PayPal![](https://www.paypal.com/en_AU/i/scr/pixel.gif)

[👈🏻 Previous article](https://yashints.dev/blog/2024/05/27/semantic-kernel-planners/)

[Next article 👉🏻](https://yashints.dev/blog/2024/04/30/semantic-kernel/)
Highlights: None
Highlight Scores: None
Summary: None

Title: Leverage MCP tools with Semantic Kernel Agents | by Valentina Alto
URL: https://valentinaalto.medium.com/leverage-mcp-tools-with-semantic-kernel-agents-36120136832d
ID: https://valentinaalto.medium.com/leverage-mcp-tools-with-semantic-kernel-agents-36120136832d
Score: None
Published Date: 2025-06-03T11:36:15.000Z
Author: Valentina Alto
Image: https://miro.medium.com/v2/resize:fit:945/0*edimuOGIEFeoocaU.png
Favicon: None
Extras: None
Subpages: None
Text: ## Understanding Agentic Protocols — Part 2

In my previous article of this series, we introduced the concept of Model Context Protocol (MCP) and demonstrated how to quickly deploy a tool as an MCP server and consume through Claude Desktop as MCP host.

In this chapter, we will do a step further and explore how to build your own Agent leveraging Semantic Kernel (SK) and equipping it with MCP servers as tool. Before starting, let’s quickly recap what SK and MCP are.

## Semantic Kernel

Semantic kernel is a lightweight framework which make it easier to develop AI-powered applications. It falls into the category of AI orchestrators like Llama-Index, LangChain, TaskWeaver and so on.

It serves as a middleware layer, allowing for the orchestration of LLMs alongside traditional programming code in languages such as C#, Python, and Java . By providing abstractions for AI services, plugins, memory management, and planning, Semantic Kernel simplifies the development of AI-driven applications, making it easier to build intelligent agents that can perform complex tasks, interact with users, and adapt to changing requirements.

## Model Context Protocol

The Model Context Protocol (MCP) is a standard designed to unify how large language models (LLMs) interact with external tools and data sources — much like how HTTP and REST APIs standardize web communication.

The MCP aims at addressing the following challenges:

- Current fragmentation: Frameworks like Semantic Kernel and other popular offering - like LangChain or AutoGen - rely on custom, often siloed integrations.
- Maintenance burden: Changes in provider-specific APIs require constant updates.
- No universal standard: Each system connects to resources in its own way, limiting scalability and interoperability.

From an architecture perspective, the protocol is made of the following components:

- MCP Host: The app managing LLM interactions (e.g., Claude Desktop, GitHub Copilot).
- MCP Client: The middleware that connects hosts to external tools via the protocol.
- MCP Server: The actual tools, prompts, or data sources the LLM can call.

## What’s the difference between an AI framework and a Protocol?

Frameworks like **Semantic Kernel (SK)** and protocols like the **Model Context Protocol (MCP)** both aim to simplify how AI systems interact with tools and data — but they operate at different layers of abstraction and serve distinct purposes.

SK is a developer-facing **framework** that provides structured abstractions (e.g., planners, plugins, memory, and function calling) to help build and orchestrate AI-powered workflows inside applications. It offers rich tooling for working with language models, chaining functions, and managing state.

MCP, on the other hand, is a **protocol** — a standardized interface specification — that defines how LLMs can dynamically discover and invoke external tools at runtime, regardless of the implementation language or orchestration logic behind them. While SK is opinionated and extensible within its ecosystem, MCP is designed to be interoperable and model-agnostic, enabling cross-platform tool invocation directly from the LLM’s reasoning loop.

## Building an AI Agent in SK with MCP Plugin

Let’s get practical. I this demonstration, I will re-use a SK plugin for TextToSQL interaction I developed [here](https://github.com/Valentina-Alto/multi-framework-semantic-kernel). Note that the plugin itself is leveraging LangChain as well — which confirms the design principle of AI Agents of modularity and abstractions. In other words, AI Agents’ components can be seen as stand-alone assets, which are agnostic with respect to the framework you use or the programming language you prefer.

> **Note:** When it comes to modularity and abstraction, MCP is truly the cherry on top. It enables agent tools to be fully agnostic. For instance, in the repository mentioned earlier, I was able to integrate a LangChain component into an SK-based agent using SK-specific taxonomy. With MCP, that same LangChain component becomes compatible across any framework or host that supports the protocol — making it reusable and interoperable by design. The best part? Adoption is growing rapidly, especially among enterprise platforms.

Let’s have a look at the plugin:

```
import os
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP
from semantic_kernel.functions import kernel_functionfrom langchain_community.utilities.sql_database import SQLDatabase
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory# -------------------------------
# Load environment variables
# -------------------------------
load_dotenv()AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT")
AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION", "2025-01-01-preview")# -------------------------------
# Initialize MCP Server
# -------------------------------
mcp = FastMCP("SQLAgentServer")# -------------------------------
# Global components: LLM, DB, Tools, Prompt, Agent
# -------------------------------
llm = AzureChatOpenAI(
 openai_api_version=AZURE_OPENAI_API_VERSION,
 azure_deployment=AZURE_OPENAI_DEPLOYMENT,
)db = SQLDatabase.from_uri("sqlite:///chinook.db")
toolkit = SQLDatabaseToolkit(db=db, llm=llm)
tools = toolkit.get_tools()prompt = ChatPromptTemplate.from_messages(
 [
 ("system", """You are an agent designed to interact with a SQL database.
Given an input question, create a syntactically correct SQLite query to run, then look at the results of the query and return the answer.
Unless the user specifies a specific number of examples they wish to obtain, always limit your query to at most 5 results.
You can order the results by a relevant column to return the most interesting examples in the database.
Never query for all the columns from a specific table, only ask for the relevant columns given the question.
You have access to tools for interacting with the database.
Only use the below tools. Only use the information returned by the below tools to construct your final answer.
You MUST double check your query before executing it. If you get an error while executing a query, rewrite the query and try again.DO NOT make any DML statements (INSERT, UPDATE, DELETE, DROP etc.) to the database.To start you should ALWAYS look at the tables in the database to see what you can query.
Do NOT skip this step.
Then you should query the schema of the most relevant tables.
 """),
 MessagesPlaceholder("chat_history", optional=True),
 ("human", "{input}"),
 MessagesPlaceholder("agent_scratchpad"),
 ]
)chat_history = ChatMessageHistory()
agent = create_openai_tools_agent(llm, tools, prompt)
executor = AgentExecutor(agent=agent, tools=tools, verbose=True)agent_with_memory = RunnableWithMessageHistory(
 executor,
 lambda session_id: chat_history,
 input_messages_key="input",
 history_messages_key="chat_history",
)# -------------------------------
# MCP Tool: SQL Agent Query Runner
# -------------------------------
@mcp.tool()
def run_sql_query(user_input: str) -> str:
 """
 Tool specialized in retrieving information from the chinook database using SQL queries. The chinook database is a sample database that contains information about a music store, including artists, albums, tracks, and customers. """
 result = agent_with_memory.invoke(
 {"input": user_input},
 config={"configurable": {"session_id": " "}},
 )
 return result["output"]# -------------------------------
# MCP Entry Point
# -------------------------------
if __name__ == "__main__":
 mcp.run(transport="stdio")
```

As you can see, the core structure doesn’t change. There are three main additional elements that we need to keep in mind:

- Initialization of the MCP

```
mcp = FastMCP("SQLAgentServer")
```

- mcp.tool() decorator: this is needed to initialize the core function of the mcp, in our case the SQL tool.

```
@mcp.tool()
def func():
 return
```

Note that MCP servers can host multiple tools and resources. You will have as many decorators as the number of assets you host on your server, each one provided with a name and description in natural language.

- MCP entry point: When running Model Context Protocol (MCP) servers, you can choose between two primary transport mechanisms: **STDIO (Standard Input/Output)** and **SSE (Server-Sent Events)**. STDIO transport facilitates communication between the client and server through standard input and output streams. SSE transport enables servers to push real-time updates to clients over HTTP. Clients initiate a connection via an HTTP GET request, and the server sends events as they occur. In our case, we will go for the STDIO mechanism:

```
if __name__ == "__main__":
 mcp.run(transport="stdio")
```

Great! Now that we have our plugins, we need to attach them to our agent in SK. To do so, we will use the The `MCPStdioPlugin,` a component of SK Python SDK that facilitates integration with MCP servers via STDIO. This plugin allows your Semantic Kernel applications to communicate with local MCP servers by spawning them as subprocesses and interacting through their stdin and stdout streams.

Let’s see how to do that:

```
 mcp_plugin = MCPStdioPlugin(
 name="SQLServer",
 command="python",
 args=[str(Path("your_path_to_mcp_server")],
 )
```

The moment you initialize this plugin, you can manage it as a standard SK plugin, meaning that you can either add it to your kernel, or directly at your agent level. In my case, I added the plugin directly at kernel level:

```
try:
 await mcp_plugin.connect()
 print("✅ MCP plugin connected.")
 kernel.add_plugin(mcp_plugin, plugin_name="sqltool")
 print("🔧 MCP plugin registered with kernel.")
except Exception as e:
 print(f"❌ Error: Could not register the MCP plugin: {str(e)}")
 await mcp_plugin.close()
 sys.exit(1)agent = ChatCompletionAgent(
 kernel=kernel,
 name="Assistant",
 instructions="You are a helpful assistant."
)
```

> Note: `mcp_plugin.connect()` is asynchronous because it launches and manages a subprocess with potentially **streaming** input/output. By doing so, the app waits for the tool to be ready and it can support long-lived communication (e.g., streaming SQL results).

We are now ready to test our app (you can find the whole code [here](https://github.com/Valentina-Alto/semantic-kernel-mcp-sql/tree/main)):

```
python test_mcp_sql.py
```

As you can see, the Agent first answered without the tool to greet me, then it invoked the MCP tool to run the SQL query as needed.

## Conclusion

By combining Semantic Kernel’s orchestration capabilities with the interoperability of the Model Context Protocol, developers can build AI agents that are both modular and framework-agnostic. This integration allows components — which can be developed with the framework and language of your choice — to be reused seamlessly across different environments, making your agent architecture more scalable and future-proof.

## References

- [SQLDatabase Toolkit \| 🦜️🔗 LangChain](https://python.langchain.com/docs/integrations/tools/sql_database/)
- [lerocha/chinook-database: Sample database for SQL Server, Oracle, MySQL, PostgreSQL, SQLite, DB2](https://github.com/lerocha/chinook-database)
- [https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python](https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python)
- [Prompts — Model Context Protocol （MCP）](https://modelcontextprotocol.info/docs/concepts/prompts/)
- [Resources — Model Context Protocol （MCP）](https://modelcontextprotocol.info/docs/concepts/resources/)
- [Tools — Model Context Protocol （MCP）](https://modelcontextprotocol.info/docs/concepts/tools/)
- [modelcontextprotocol/python-sdk: The official Python SDK for Model Context Protocol servers and clients](https://github.com/modelcontextprotocol/python-sdk)
Highlights: None
Highlight Scores: None
Summary: None

Title: Why Your AI Agent Isn't Calling Your Tools: Fixing Function Invocation Issues in Semantic Kernel
URL: https://systenics.ai/blog/2025-04-11-fixing-function-invocation-issues-in-semantic-kernel
ID: https://systenics.ai/blog/2025-04-11-fixing-function-invocation-issues-in-semantic-kernel/
Score: None
Published Date: 2025-04-11T00:00:00.000Z
Author: 
Image: https://systenics.ai/_astro/agent-plugin.Cuao4byw_1zBFq2.jpg
Favicon: https://systenics.ai/favicon.ico
Extras: None
Subpages: None
Text: You’re building an AI agent using a powerful framework like [Microsoft Semantic Kernel](https://learn.microsoft.com/en-us/semantic-kernel/overview/). You’ve carefully crafted a plugin with specific functions to give your agent new skills – maybe fetching weather data, accessing a database, or interacting with an API. You write a prompt that clearly requires this plugin… but the agent just responds with plain text, completely ignoring the tool you gave it. Sound familiar?

If you’ve spent hours scratching your head, debugging, and wondering why your agent isn’t using its tools, you’re not alone. This is a common hurdle, especially when diving into agent development, and the solution is often simpler than you think.

This blog will explain this frequent issue, show you why it happens, and provide a straightforward fix within Semantic Kernel.

Learn about [Building AI Agent using Semantic Kernel Agent Framework](https://systenics.ai/blog/2025-04-09-building-ai-agent-using-semantic-kernel-agent-framework/).

## What Are AI Agents and Plugins?

Think of an AI Agent as a smart assistant powered by a large language model (LLM). It can understand your requests, reason about them, and plan steps to achieve a goal. However, LLM’s knowledge is generally limited to the data it was trained on. It can’t inherently know today’s weather or access your company’s private database. That’s where Plugins (sometimes called Tools or Functions) come in. Plugins are pieces of code that extend an agent’s capabilities. They are like tools in a toolbox, allowing the agent to interact with the outside world, perform specific calculations, or access real-time information. When you give an agent a plugin, you’re essentially teaching it a new skill.

## The Problem: The Agent Ignores Your Plugin

Let’s illustrate with a common scenario using Semantic Kernel. Imagine you have a simple plugin to get the current weather:

```
public class WeatherPlugin
{
 [KernelFunction, Description("Gets the current weather for a specific location")]
 public string GetWeather([Description("The city name")] string location)
 {
 // (Code here to call a weather API and return the weather)
 return $"The weather in {location} is sunny.";
 }
}

```

Now, you set up your Semantic Kernel agent and add this plugin:

```
using Microsoft.SemanticKernel;

var builder = Kernel.CreateBuilder();
builder.AddAzureOpenAIChatCompletion(
 deploymentName:,
 endpoint:,
 apiKey:);

Kernel kernel = builder.Build();

ChatCompletionAgent agent = new ChatCompletionAgent()
{
 Name = "SK-Agent",
 Instructions = "You are a helpful assistant that can use plugins to perform tasks.",
 Kernel = kernel
 Arguments = new KernelArguments()
 };

KernelPlugin weatherPlugin = KernelPluginFactory.CreateFromType ();
agent.Kernel.Plugins.Add(weatherPlugin);

var message = new ChatMessageContent(AuthorRole.User, "What's the weather like in London today?");

await foreach (StreamingChatMessageContent response in weatherInformationAgent.InvokeStreamingAsync(message))
{
 Console.Write($"{response.Content}");
}

```

You run this, expecting the agent to recognize the need for weather information, call your GetWeather function, and return the result. Instead, it gives a generic LLM response, completely bypassing the plugin. You check your plugin code, the registration, the prompt – everything seems right. Why isn’t it working?

## The Solution

The core issue often lies in the execution settings. By default, the agent might not be configured to automatically decide whether to call a function based on the prompt. It needs explicit permission or guidance.

In Semantic Kernel, this guidance is provided through PromptExecutionSettings, specifically the FunctionChoiceBehavior property. To solve our problem, you need to tell the kernel that the agent is allowed to automatically choose and execute a suitable function from its available plugins if the prompt suggests it.

Here’s how you modify the agent invocation call:

```
// Initialize the PromptExecutionSettings and set FunctionChoiceBehavior to Auto
var executionSettings = new PromptExecutionSettings()
{
 // This setting allows the agent to auto-select and invoke plugin functions if needed.
 FunctionChoiceBehavior = FunctionChoiceBehavior.Auto()
};

// Pass these settings when creating the KernelArguments for your agent.
var kernelArguments = new KernelArguments(executionSettings);

// Create the agent with these settings included.
ChatCompletionAgent agent = new ChatCompletionAgent()
{
 Name = "SK-Agent",
 Instructions = "You are a helpful assistant that can use plugins to perform tasks.",
 Kernel = kernel,
 Arguments = kernelArguments
};

```

It instructs the underlying LLM (that supports function/tool calling) to analyze the prompt and the descriptions of the available functions (plugins). If it determines that calling one or more functions is the best way to fulfill the request, it will output the necessary information to trigger those function calls, which Semantic Kernel then handles.

## Conclusion

Building AI agents that can leverage external tools is incredibly powerful, but small configuration details can sometimes lead to significant debugging headaches. If your Semantic Kernel agent isn’t calling its plugins when you expect it to, one of the very first things to check is your PromptExecutionSettings.

Ensuring you set FunctionChoiceBehavior = FunctionChoiceBehavior.Auto() (or ToolChoiceBehavior.Auto) in your execution settings explicitly grants the agent the autonomy to decide when to use its tools, bridging the gap between understanding a request and taking action.
Highlights: None
Highlight Scores: None
Summary: None

Title: Introduction to Semantic Kernel: The .NET Developer’s Guide to Building Powerful AI Agents
URL: https://developersvoice.com/blog/ai-development/semantic_kernel_ai/
ID: https://developersvoice.com/blog/ai-development/semantic_kernel_ai/
Score: None
Published Date: 2025-06-20T00:00:00.000Z
Author: DevelopersVoice
Image: https://developersvoice.com/images/semantic_kernel_ai.jpg
Favicon: https://developersvoice.com/images/favicon-96x96.png
Extras: None
Subpages: None
Text: [Skip to content](https://developersvoice.com/developersvoice.com#main-content)

[![Developers Voice | The Software Architects Hub](https://developersvoice.com/_astro/assets/MainLogo.CORfMhAy_Z13ixJq.webp)![Developers Voice | The Software Architects Hub](https://developersvoice.com/_astro/assets/MainLogoDark.B0va-2kM_1zFQ5x.webp)](https://developersvoice.com/)

## Search

to navigate to select `ESC` to close

![Introduction to Semantic Kernel: The .NET Developer's Guide to Building Powerful AI Agents](https://developersvoice.com/_astro/assets/semantic_kernel_ai.D6E2NtkG_UVYHx.webp)

# Introduction to Semantic Kernel: The .NET Developer's Guide to Building Powerful AI Agents

By

[Sudhir mangla](https://developersvoice.com/authors/sudhir-mangla)

Category

[Artificial Intelligence](https://developersvoice.com/categories/artificial-intelligence)

Published

20 Jun, 2025

Read time

32 min

## 1\. Introduction: The Dawn of the AI-Powered .NET Application

Artificial intelligence is no longer a futuristic ideal reserved for research labs and Silicon Valley giants. It’s becoming the backbone of modern applications across industries. For .NET architects and developers, this shift signals a transformative opportunity to enhance software with intelligence that adapts, reasons, and learns. As business requirements grow more dynamic and expectations around user experience rise, AI isn’t just a differentiator. It’s rapidly becoming a core requirement.

### 1.1. The Paradigm Shift: Moving from Traditional Software to Intelligent Applications

Traditionally, software has been deterministic. You write rules, and the program executes them. These systems are reliable but limited; they can’t flexibly respond to ambiguous input or interpret intent beyond explicit instructions. The rise of large language models (LLMs) like GPT-4 and similar technologies marks a turning point. Instead of relying solely on rules, modern software can interpret, generate, and reason about text, code, and sometimes even images.

This evolution doesn’t mean replacing every deterministic algorithm with AI. Instead, it’s about infusing intelligence where it matters—understanding natural language, extracting meaning from documents, automating conversations, and orchestrating complex workflows based on human-like reasoning.

### 1.2. Why AI Orchestration is the Next Frontier for .NET Architects

You might be asking, “Can’t I just call an LLM API and get answers?” Technically, yes. But enterprise-grade applications require far more. They demand contextual awareness, composability, modularity, and robust integration with data and services. Making raw calls to a language model is like having a super-intelligent assistant who forgets everything between conversations and needs constant handholding.

Orchestration frameworks allow you to manage this intelligence—connecting LLMs to business logic, APIs, memory stores, and plugins—while maintaining the best practices you already follow in .NET development. AI orchestration bridges the gap between the potential of LLMs and the real-world needs of production software.

### 1.3. Introducing Semantic Kernel: Your Bridge to Large Language Models (LLMs)

Semantic Kernel, an open-source project from Microsoft, aims to make AI orchestration accessible, reliable, and powerful for .NET developers. It’s more than a wrapper for LLM APIs. Semantic Kernel gives you tools to:

- Compose AI-driven workflows
- Integrate semantic and native functions (both prompts and C# code)
- Store and retrieve memory/context for stateful AI
- Connect LLMs with real-world data and services

If you’re familiar with .NET patterns—dependency injection, plugin architectures, composable services—Semantic Kernel will feel like home, but with new capabilities that unlock generative AI.

### 1.4. What to Expect: A Practical Journey from Core Concepts to Enterprise-Ready AI Agents

This guide will walk you through everything you need to know as a .NET architect or senior developer who wants to build intelligent applications using Semantic Kernel. Whether your goal is a smart chatbot, a contextual document search, or an automated agent that can reason and act, you’ll find:

- A clear explanation of LLMs from an architect’s perspective
- How Semantic Kernel compares to other frameworks like LangChain
- Step-by-step environment setup and code examples using the latest .NET features
- A deep dive into Semantic Kernel’s core components: kernel, plugins, prompt engineering, and memory
- Best practices, real-world scenarios, and practical tips for building robust AI agents

Are you ready to build the next generation of .NET applications? Let’s begin by understanding the technology at the heart of this new paradigm: large language models.

## 2\. Understanding the Foundations: LLMs and the Rise of Semantic Kernel

### 2.1. A .NET Architect’s Primer on Large Language Models (LLMs)

#### 2.1.1. What are LLMs and How Do They Work? (Conceptual Overview)

At their core, large language models (LLMs) like OpenAI’s GPT-4, Microsoft’s Phi-3, and Meta’s Llama are deep learning models trained on vast amounts of text data. They predict the next word in a sequence, given the previous words. But thanks to scale and architecture (transformers), they can generate coherent text, summarize documents, translate languages, answer questions, and even write code.

For a .NET developer, think of an LLM as a supercharged autocomplete on steroids. You provide input (the _prompt_), and the model returns output (the _completion_), whether it’s a sentence, an answer, or even a structured plan.

LLMs are not databases. They don’t “know” things in the way a SQL server does. Their knowledge is implicit, encoded in billions of parameters from training data. They excel at language understanding, pattern recognition, and analogical reasoning—but can’t guarantee factual accuracy or recall specific items outside their training window.

#### 2.1.2. Key Terminology for Architects: Tokens, Embeddings, and Prompts

To use LLMs effectively, a few concepts are critical:

- **Tokens**: These are the chunks of text (words, subwords, or characters) the model processes. For example, “.NET” may be one or more tokens. Cost and context length are often measured in tokens.
- **Embeddings**: These are numerical representations of text. You can think of them as a way to compare the meaning of different pieces of text for similarity searches, clustering, or semantic retrieval.
- **Prompts**: The input you send to the LLM. Crafting prompts is both an art and a science. The structure, clarity, and specificity of prompts heavily influence output quality.

Understanding these terms will help you make informed choices as you design intelligent .NET applications.

#### 2.1.3. The Power and Limitations of LLMs in Enterprise Scenarios

LLMs offer a lot of promise: rapid prototyping, natural language interfaces, summarization, code generation, and more. But they have limitations:

- **Context size**: LLMs have a maximum number of tokens they can process at once. Long documents may need to be chunked.
- **Factuality**: LLMs can “hallucinate,” generating plausible-sounding but incorrect information.
- **Determinism**: LLM outputs can vary based on randomness and prompt wording.
- **Latency and cost**: LLM inference, especially with large models, may be slower and more expensive than traditional code execution.

Balancing these strengths and weaknesses is a key challenge in architecting real-world systems.

### 2.2. The Need for an Orchestration Framework: Why Raw LLM Calls Aren’t Enough

Calling an LLM directly from your .NET application can deliver a quick proof of concept, but scaling to production requires more:

- **State management**: LLMs don’t remember previous interactions unless you provide them with context.
- **Tool use**: LLMs can’t call APIs, access databases, or trigger workflows by themselves.
- **Security and compliance**: Enterprise applications must handle data securely, log activity, and meet regulatory requirements.
- **Composability**: Real solutions often require chaining multiple steps, integrating with external data, and combining native code with AI.

This is where orchestration frameworks like Semantic Kernel come in—wrapping raw LLM calls with structured components, context, plugins, and extensibility.

### 2.3. Semantic Kernel vs. The Competition: A .NET Perspective on LangChain

#### 2.3.1. Core Philosophies and Architectural Differences

LangChain (popular in the Python ecosystem) and Semantic Kernel (for .NET and Python) both aim to orchestrate LLMs, memory, and tool usage. However, their core philosophies diverge:

- **LangChain**: Emphasizes flexible chains, agents, and integrations. Designed for Python-first data science and rapid prototyping.
- **Semantic Kernel**: Built natively for .NET (with a Python sibling). Focuses on composability, dependency injection, and familiar .NET patterns. Prioritizes strong typing, modularity, and integration with enterprise infrastructure (like Azure).

In short, Semantic Kernel is engineered for .NET professionals who want to blend AI with existing code, services, and enterprise patterns.

#### 2.3.2. Why Semantic Kernel is a Natural Fit for the .NET Ecosystem

.NET architects value stability, maintainability, and the power of C#. Semantic Kernel fits right in:

- **First-class C# support**: Write plugins and native functions in C# using the latest language features (including async/await, records, pattern matching, and more).
- **NuGet ecosystem**: Easy installation, version management, and community support.
- **Integration with Microsoft services**: Out-of-the-box connectors for Azure OpenAI, Azure Cognitive Search, and more.
- **Strong typing and dependency injection**: Leverage established patterns for testing, scaling, and maintaining codebases.

If you’re building enterprise-grade software on .NET, Semantic Kernel offers an idiomatic and robust entry point into AI orchestration.

### 2.4. Setting Up Your Development Environment

Let’s get practical. To follow along, you’ll need:

#### 2.4.1. Prerequisites: .NET 8, an IDE, and Your First “Hello, AI!” Project

Ensure you have the latest .NET 8 SDK installed. Any modern IDE works—Visual Studio 2022+, JetBrains Rider, or Visual Studio Code. Create a new console application:

```
dotnet new console -n HelloSemanticKernel
cd HelloSemanticKernel
```

#### 2.4.2. Installing the Semantic Kernel SDK via NuGet

Install the Semantic Kernel NuGet package. At the time of writing, use:

```
dotnet add package Microsoft.SemanticKernel
```

Check for the latest version on NuGet as Semantic Kernel evolves rapidly.

#### 2.4.3. Configuring Your First Kernel with an LLM Connector (e.g., OpenAI, Azure OpenAI)

To use Semantic Kernel, you need to connect it to an LLM. Here’s a minimal example using OpenAI’s GPT-4:

```
using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.Connectors.OpenAI;

var builder = Kernel.CreateBuilder();
builder.AddOpenAIChatCompletion(
 modelId: "gpt-4",
 apiKey: " "
);

var kernel = builder.Build();

var result = await kernel.InvokePromptAsync("What is Semantic Kernel?");
Console.WriteLine(result);
```

For Azure OpenAI, use `AddAzureOpenAIChatCompletion` instead, supplying the endpoint and deployment details. Keep your API keys secure—use user secrets or environment variables in real projects.

Now that you have a kernel connected to an LLM, you’re ready to explore Semantic Kernel’s architecture in depth.

## 3\. The Core Components of Semantic Kernel: A Deep Dive

Understanding the pieces of Semantic Kernel is key to building powerful, maintainable, and intelligent applications. Let’s examine the main components: the kernel, plugins, prompt engineering, and memory.

### 3.1. The Kernel: The Heart of Your AI Application

#### 3.1.1. Understanding the `Kernel` Class and its Role

The `Kernel` class is the orchestrator of your AI-powered .NET app. It manages the lifecycle of all your AI functions, plugins, connectors, and memory. Think of it as the AI engine—receiving user requests, delegating work to plugins, passing context between functions, and interacting with LLMs.

#### 3.1.2. The `KernelBuilder`: Configuring Services and Dependencies

Much like `HostBuilder` in ASP.NET Core, `KernelBuilder` helps you configure dependencies and register services. You can add connectors for different LLMs, configure memory stores, and register plugins. This pattern aligns well with modern .NET practices and makes your application easier to test and maintain.

**Example: Configuring Kernel with Multiple Services**

```
using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.Connectors.OpenAI;

var builder = Kernel.CreateBuilder();

// Register OpenAI for text completion
builder.AddOpenAIChatCompletion(
 modelId: "gpt-4",
 apiKey: " "
);

// Register memory with Azure Cognitive Search
builder.AddAzureCognitiveSearchMemory(
 endpoint: " ",
 apiKey: " "
);

// Register custom plugins
builder.Plugins.AddFromType ();

var kernel = builder.Build();
```

This modular approach allows you to swap components or add new ones as your solution evolves.

### 3.2. Plugins: The Building Blocks of Functionality

#### 3.2.1. What are Plugins? A Blend of Native C\# and Semantic Functions

Plugins in Semantic Kernel encapsulate functionality that can be invoked by the kernel. They come in two flavors:

- **Native functions**: Pure C# code, ideal for deterministic logic, API calls, or data processing.
- **Semantic functions**: Prompt-based, executed via LLMs, useful for natural language understanding, summarization, and generative tasks.

Plugins can expose one or more functions, and can be invoked directly or composed into workflows.

#### 3.2.2. Creating Your First Native Function in C\#

Here’s how you might define a simple native plugin in C#:

```
using Microsoft.SemanticKernel.SkillDefinition;

public class MathPlugin
{
 [KernelFunction("add")]
 public Task AddAsync(int a, int b)
 {
 return Task.FromResult(a + b);
 }
}

// Register plugin
builder.Plugins.AddFromType ();
```

This makes your C# function callable by other plugins, prompts, or LLM-driven workflows.

#### 3.2.3. Crafting Your First Semantic Function with Prompts

Semantic functions are defined with prompt templates. Here’s an example for summarizing text:

```
var summarizeFunction = kernel.CreateSemanticFunction(
 "Summarize the following text in one sentence: {{$input}}"
);

string inputText = "Semantic Kernel is an open-source orchestration framework...";
var summary = await kernel.InvokeAsync(summarizeFunction, new() { ["input"] = inputText });
Console.WriteLine(summary);
```

Semantic functions can be registered as part of a plugin for reuse and composition.

#### 3.2.4. Best Practices for Designing and Organizing Plugins

- **Separation of concerns**: Group related functions into plugins for clarity and maintainability.
- **Reusability**: Keep plugins stateless where possible. Store state in memory/context passed between invocations.
- **Strong typing**: Use well-defined input/output types for native functions.
- **Error handling**: Anticipate and gracefully handle failures, especially for external API calls.

Organize plugins much like you would controllers or services in an ASP.NET project.

### 3.3. Prompts and Prompt Engineering for .NET Developers

#### 3.3.1. The Art of the Prompt: From Simple Instructions to Complex Templates

Prompt engineering is the craft of designing inputs that reliably elicit high-quality outputs from LLMs. A well-structured prompt clarifies intent and reduces ambiguity.

**Simple prompt example:**

```
"Translate the following text to French: {{$input}}"
```

**Complex template with variables:**

```
"You are an expert .NET software architect. Summarize the following requirements, and suggest a suitable design pattern. Requirements: {{$requirements}}"
```

Testing and refining prompts is iterative. Small changes can have large impacts on output quality.

#### 3.3.2. Using `PromptTemplate` and `PromptTemplateFactory`

Semantic Kernel provides APIs for building reusable prompt templates.

```
using Microsoft.SemanticKernel.TemplateEngine;

var templateFactory = new PromptTemplateFactory();
var template = templateFactory.Create("Rewrite the following as a bullet list: {{$input}}");

var kernelFunction = kernel.CreateSemanticFunction(template);
```

You can parameterize templates for dynamic inputs and maintain a library of prompts for your application.

#### 3.3.3. Advanced Prompting Techniques: Few-shot Learning and Chain of Thought

- **Few-shot learning**: Include examples in your prompt to guide the LLM.

```
"Convert date formats. Example: '2025-06-20' -> 'June 20, 2025'. Now, convert: '{{$input}}'"
```

- **Chain of thought**: Encourage the model to “think aloud” by requesting step-by-step reasoning.

```
"Solve the following math problem step by step: {{$input}}"
```

Use these techniques to improve reliability for complex tasks.

### 3.4. Memory: Giving Your AI a Past and a Context

#### 3.4.1. The Importance of Memory in Conversational AI

Stateless LLMs are like goldfish—they forget each interaction. For many applications, especially chatbots and agents, you need to maintain conversation history, user preferences, or task progress. Memory makes your AI feel intelligent, personal, and context-aware.

#### 3.4.2. Volatile Memory: Quick, In-Process Context

Semantic Kernel supports volatile, in-memory storage for session-level context.

**Example: Adding and retrieving memory within a session**

```
var memory = kernel.Memory;

// Save data
await memory.SaveInformationAsync(
 collection: "chatHistory",
 text: "Hello, how can I help you?",
 id: "message1"
);

// Retrieve data
var message = await memory.GetAsync("chatHistory", "message1");
Console.WriteLine(message?.Metadata.Text);
```

Volatile memory is fast, but not persistent. Use it for short-lived state.

#### 3.4.3. Semantic Memory and Vector Databases (e.g., Azure AI Search, Pinecone, Chroma)

For richer, persistent memory, connect Semantic Kernel to a vector database. Text is stored as embeddings, enabling similarity search and semantic retrieval.

**Configuring Azure Cognitive Search memory:**

```
builder.AddAzureCognitiveSearchMemory(
 endpoint: " ",
 apiKey: " "
);
```

**Usage pattern:**

- Store documents, conversation history, or knowledge snippets as embeddings.
- At runtime, retrieve the most relevant items based on semantic similarity to the current context.

This unlocks powerful capabilities like RAG (retrieval-augmented generation), where your LLM can “recall” enterprise knowledge.

#### 3.4.4. Practical Example: Building a Chatbot with Conversational History

Let’s combine the concepts:

```
// Assume kernel and memory are already configured

string userInput = "How do I connect to Azure from .NET?";
await memory.SaveInformationAsync("chatHistory", userInput, Guid.NewGuid().ToString());

string conversation = string.Join("\n", await memory.SearchAsync("chatHistory", "", limit: 10));

// Build prompt with context
string prompt = $"The following is a conversation between a user and an assistant.\n{conversation}\nUser: {userInput}\nAssistant:";

// Create semantic function
var chatFunction = kernel.CreateSemanticFunction(prompt);

// Invoke LLM
var response = await kernel.InvokeAsync(chatFunction);
Console.WriteLine(response);

// Save assistant’s response
await memory.SaveInformationAsync("chatHistory", response.ToString(), Guid.NewGuid().ToString());
```

This pattern forms the

backbone of context-aware chatbots, assistants, and intelligent agents.

## 4\. Connectors: Extending the Reach of Your AI Agent

Enterprise applications rarely operate in isolation. The true power of Semantic Kernel emerges when it acts as a hub, seamlessly integrating with external data sources, services, and infrastructure. This extensibility is enabled by _connectors_. Understanding and leveraging connectors allows your AI agents not only to “think” but also to act within the broader technology landscape.

### 4.1. The Role of Connectors in an Extensible Architecture

Connectors in Semantic Kernel are modular interfaces that enable your kernel to interact with the outside world. At a high level, connectors abstract communication with:

- Language models (LLM connectors)
- Memory stores (memory connectors)
- Data sources (SQL, REST APIs, or any service you need to orchestrate)

For .NET architects, connectors represent clear separation of concerns—each connector encapsulates integration logic for a specific external resource, making your system more maintainable and adaptable. Whether you need to switch LLM providers, swap out a memory store, or add a custom business system, connectors make this evolution straightforward.

In essence, connectors enable your AI agent to become truly actionable and context-aware, with the ability to _see_, _remember_, and _interact_ with the resources you define.

### 4.2. LLM Connectors: Beyond OpenAI

#### 4.2.1. Integrating with Azure OpenAI for Enterprise-Grade Security and Scalability

While OpenAI’s hosted APIs are popular for experimentation and smaller-scale deployments, many organizations require greater control over data residency, compliance, throughput, and security. This is where Azure OpenAI shines.

Azure OpenAI offers:

- **Enterprise security** (AAD integration, VNETs, private endpoints)
- **Scalability** (custom model deployments, throughput guarantees)
- **Compliance** with regional and industry regulations

**Configuring Semantic Kernel with Azure OpenAI:**

```
builder.AddAzureOpenAIChatCompletion(
 deploymentName: "my-gpt4-deployment",
 endpoint: "https://.openai.azure.com/",
 apiKey: " "
);

var kernel = builder.Build();
```

The main difference: _deploymentName_ is your model deployment in Azure, not just a model ID. For organizations already leveraging Azure, this integration provides peace of mind and seamless management.

#### 4.2.2. Exploring Other LLM Providers (e.g., Hugging Face)

Semantic Kernel is LLM-agnostic by design. You can connect to any provider—local or cloud—using available connectors or by writing your own. For example, integrating with Hugging Face’s hosted models is a viable alternative for teams who prefer open models, require domain-specific fine-tuning, or wish to avoid vendor lock-in.

**Using Hugging Face with Semantic Kernel:**

While direct support may not be built-in, the extensibility of Semantic Kernel allows you to wrap any RESTful LLM endpoint as a connector. This flexibility empowers you to leverage open-source models, self-hosted LLMs, or niche providers as your needs evolve.

### 4.3. Memory Connectors: Persistent and Scalable Memory Solutions

Your AI agent’s value increases dramatically when it has access to organizational knowledge and history. Memory connectors enable persistent, scalable storage and retrieval—powering advanced scenarios like Retrieval Augmented Generation (RAG), contextual chat, and semantic search.

#### 4.3.1. Connecting to Azure AI Search for a Robust RAG Implementation

Azure AI Search (previously Azure Cognitive Search) is a fully managed search-as-a-service, providing fast, scalable, and enterprise-ready vector search capabilities. When integrated with Semantic Kernel, it enables your agent to recall relevant documents, past interactions, and knowledge snippets efficiently.

**Example: Registering Azure AI Search Memory**

```
builder.AddAzureCognitiveSearchMemory(
 endpoint: "https://.search.windows.net",
 apiKey: " ",
 indexName: "support-tickets"
);
```

With this setup, your AI agent can persist and retrieve embeddings (semantic representations of text), supporting sophisticated RAG pipelines and contextual reasoning over vast data sets.

#### 4.3.2. Integrating with Other Vector Stores

Semantic Kernel’s abstraction makes it easy to use alternative vector databases:

- **Pinecone**
- **Chroma**
- **Qdrant**
- **Redis with vector extensions**
- **Any custom solution exposing a REST API**

You simply implement or use the appropriate memory connector, registering it with your kernel. This means your architecture can evolve with minimal code changes, future-proofing your AI systems as technology advances.

### 4.4. Building Custom Connectors: Tailoring Semantic Kernel to Your Needs

Not every integration comes out-of-the-box. Sometimes, your agent needs to interact with proprietary systems, legacy APIs, or specialized databases. Semantic Kernel’s connector model is fully extensible. You can build custom connectors by implementing the required interfaces.

**High-level pattern:**

1. Implement the connector interface (e.g., `IMemoryStore`, `IChatCompletionService`).
2. Register your connector with the kernel via the builder.
3. Use the connector as part of your agent’s orchestration flow.

This approach maintains separation of concerns and adheres to SOLID principles—letting your AI orchestration logic evolve independently from integration details.

## 5\. Building Your First AI Agent: A Practical, Step-by-Step Guide

It’s time to put these concepts into practice. Let’s build a fully functional, production-minded AI agent using Semantic Kernel. We’ll walk through a concrete use case, craft plugins, wire up connectors, and orchestrate everything with a planner.

### 5.1. Defining the Use Case: A “Smart Support Ticket” System

Support operations are an ideal proving ground for AI agents. Incoming tickets contain natural language—sometimes vague, sometimes lengthy—and require prompt, consistent, and contextually relevant responses.

#### 5.1.1. The Goal: Automatically Categorize, Prioritize, and Suggest Solutions for Support Tickets

Our AI agent will:

- Analyze the severity of a new support ticket
- Categorize it by department (e.g., IT, HR, Facilities)
- Retrieve and suggest solutions from similar past tickets

This automation reduces manual triage, improves response times, and ensures knowledge is reused. It also demonstrates how Semantic Kernel blends native C#, semantic prompts, memory, and connectors.

### 5.2. Step 1: Setting up the Kernel and Plugins

#### 5.2.1. A Plugin to Analyze Ticket Severity (Semantic Function)

We’ll create a semantic function that prompts the LLM to assess severity.

```
var analyzeSeverity = kernel.CreateSemanticFunction(
 @"You are a customer support agent.
 Assess the severity of the following support ticket on a scale from 1 (trivial) to 5 (critical).
 Ticket: {{$input}}
 Respond with only the number."
);
```

This approach leverages LLM strengths: nuanced understanding of language and context.

#### 5.2.2. A Plugin to Categorize by Department (Semantic Function)

Categorization by department is another classic LLM task. Here’s the function:

```
var categorizeDepartment = kernel.CreateSemanticFunction(
 @"Assign the following support ticket to the most relevant department: IT, HR, Facilities, Finance, or Other.
 Ticket: {{$input}}
 Respond with only the department name."
);
```

Both plugins could be grouped in a “SupportTicketSemanticPlugin” for clarity and reusability.

#### 5.2.3. A Plugin to Look Up Similar Historical Tickets (Native C\# with Memory)

While LLMs excel at language, finding similar tickets from memory is best handled natively—leveraging semantic memory for vector search.

```
public class TicketMemoryPlugin
{
 private readonly ISemanticTextMemory _memory;
 public TicketMemoryPlugin(ISemanticTextMemory memory) => _memory = memory;

 [KernelFunction]
 public async Task FindSimilarAsync(string input)
 {
 var results = await _memory.SearchAsync("support-tickets", input, limit: 3, minRelevanceScore: 0.7);
 return string.Join("\n", results.Select(r => r.Metadata.Text));
 }
}
```

Register the plugin:

```
builder.Plugins.AddFromType ();
```

### 5.3. Step 2: Orchestrating the Flow with a Planner

#### 5.3.1. Introduction to Planners: The “Brain” of the Agent

A _planner_ in Semantic Kernel orchestrates multiple functions—semantic and native—into a workflow. Think of the planner as the agent’s executive: it sequences actions, manages dependencies, and ensures logical flow from input to output.

Planners are especially useful when your AI agent’s behavior involves multiple steps, data dependencies, or dynamic branching.

#### 5.3.2. Using the `SequentialPlanner` for a Step-by-Step Workflow

For our support ticket system, a sequential approach works well:

1. Assess severity
2. Categorize by department
3. Retrieve similar historical tickets

Semantic Kernel provides a `SequentialPlanner` to chain these steps.

```
using Microsoft.SemanticKernel.Planning;

var planner = new SequentialPlanner(kernel);
var plan = await planner.CreatePlanAsync(
 @"Given a new support ticket, perform the following:
 1. Analyze the ticket’s severity.
 2. Categorize it by department.
 3. Look up similar historical tickets.
 Output the results as a JSON object."
);
```

The planner inspects your registered plugins and functions, building an executable workflow tailored to your agent’s capabilities.

### 5.4. Step 3: Executing the Plan and Handling the Output

#### 5.4.1. Invoking the Planner and Retrieving the Result

With the plan in place, you execute it with a new support ticket as input.

```
string ticketText = "My laptop screen is flickering, and I need it fixed urgently for a client presentation tomorrow.";

var result = await plan.InvokeAsync(kernel, ticketText);

Console.WriteLine(result.ToString());
```

The output—ideally a structured JSON object—includes severity, department, and suggested solutions.

#### 5.4.2. Integrating the Output with a Hypothetical Ticketing System API

In a real-world system, your agent’s output feeds into your support ticketing backend. Here’s a conceptual example using an HTTP client:

```
using System.Net.Http.Json;

public class TicketingSystemClient
{
 private readonly HttpClient _httpClient;
 public TicketingSystemClient(HttpClient httpClient) => _httpClient = httpClient;

 public async Task PostCategorizedTicketAsync(string ticketId, object analysisResult)
 {
 await _httpClient.PostAsJsonAsync($"/api/tickets/{ticketId}/analysis", analysisResult);
 }
}

// In your workflow:
var ticketingClient = new TicketingSystemClient(httpClient);
await ticketingClient.PostCategorizedTicketAsync("12345", result);
```

This decouples your AI logic from backend infrastructure and enables clean integration patterns.

### 5.5. Code Walkthrough and Explanation

Let’s bring the pieces together for a clear, end-to-end understanding.

```
using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.Connectors.OpenAI;
using Microsoft.SemanticKernel.Planning;
using Microsoft.SemanticKernel.Memory;
using Microsoft.SemanticKernel.SkillDefinition;
using System.Net.Http.Json;

// 1. Set up kernel, memory, and plugins
var builder = Kernel.CreateBuilder();

builder.AddOpenAIChatCompletion("gpt-4", " ");
builder.AddAzureCognitiveSearchMemory("https://.search.windows.net", " ", "support-tickets");

// Register semantic plugins
var kernel = builder.Build();

var analyzeSeverity = kernel.CreateSemanticFunction(
 @"You are a customer support agent.
 Assess the severity of the following support ticket on a scale from 1 (trivial) to 5 (critical).
 Ticket: {{$input}}
 Respond with only the number."
);

var categorizeDepartment = kernel.CreateSemanticFunction(
 @"Assign the following support ticket to the most relevant department: IT, HR, Facilities, Finance, or Other.
 Ticket: {{$input}}
 Respond with only the department name."
);

public class TicketMemoryPlugin
{
 private readonly ISemanticTextMemory _memory;
 public TicketMemoryPlugin(ISemanticTextMemory memory) => _memory = memory;

 [KernelFunction]
 public async Task FindSimilarAsync(string input)
 {
 var results = await _memory.SearchAsync("support-tickets", input, limit: 3, minRelevanceScore: 0.7);
 return string.Join("\n", results.Select(r => r.Metadata.Text));
 }
}

builder.Plugins.AddFromType ();

// 2. Define planner and plan
var planner = new SequentialPlanner(kernel);
var plan = await planner.CreatePlanAsync(
 @"Given a new support ticket, perform the following:
 1. Analyze the ticket’s severity.
 2. Categorize it by department.
 3. Look up similar historical tickets.
 Output the results as a JSON object."
);

// 3. Run the agent
string ticketText = "My laptop screen is flickering, and I need it fixed urgently for a client presentation tomorrow.";
var result = await plan.InvokeAsync(kernel, ticketText);
Console.WriteLine(result.ToString());

// 4. Optionally, send result to ticketing API
var httpClient = new HttpClient { BaseAddress = new Uri("https://yourticketingsystem/api/") };
var ticketingClient = new TicketingSystemClient(httpClient);
await ticketingClient.PostCategorizedTicketAsync("12345", result);
```

**Explanation and Takeaways:**

- **Separation of concerns**: Semantic functions handle natural language understanding, native C# manages structured tasks and API calls.
- **Modularity**: Each capability is encapsulated in a plugin, supporting reuse and evolution.
- **Extensibility**: Connectors allow you to swap LLMs or memory stores as requirements change.
- **Orchestration**: The planner composes these functions into a reliable, repeatable workflow—abstracting complexity.

This pattern is adaptable: swap in more departments, connect new memory sources, add escalation logic, or build user-facing interfaces. The architecture stays robust and comprehensible, scaling from proof of concept to enterprise deployment.

## 6\. Advanced Concepts for the .NET Architect

At this stage, you’ve mastered the fundamentals of Semantic Kernel. But to build AI agents that truly operate at scale, deliver business-critical value, and fit seamlessly into your architecture, you’ll want to explore the advanced capabilities at your disposal. Let’s unpack the next level of patterns, scalability, and operational excellence.

### 6.1. Planners in Depth: Beyond Simple Sequences

#### 6.1.1. The Evolution of Planners: From `ActionPlanner` to `StepwisePlanner`

The basic `SequentialPlanner` serves well for linear workflows. However, real-world applications often demand more adaptive, dynamic behavior. Semantic Kernel introduces advanced planners that provide these capabilities.

- **ActionPlanner:** Interprets natural language goals and generates a sequence of plugin calls to fulfill them. It uses LLM reasoning to determine which functions to invoke and in what order.
- **StepwisePlanner:** Takes adaptivity further. This planner runs in a loop, allowing the agent to adjust its strategy based on intermediate outputs. It’s akin to a human iteratively working toward a goal, reevaluating each step as new information emerges.

These planners empower your agent to tackle more ambiguous tasks, handle branching logic, and even recover from errors during multi-step operations.

#### 6.1.2. The Power of `Function Calling` and `Auto-invocation`

One of the most transformative advancements is the introduction of **function calling**. This enables LLMs to recognize when specific structured actions are needed and automatically invoke plugins or functions, passing the right parameters.

For .NET architects, this is a leap towards autonomous agents: LLMs are no longer just text generators, but can act on structured data, call APIs, and respond to system events—all orchestrated by the kernel.

With **auto-invocation**, the kernel monitors output from the LLM, detects embedded function calls, and executes the corresponding native or semantic functions—creating a fluid loop of reasoning and action.

#### 6.1.3. Building More Complex, Goal-Oriented Agents

Suppose you want your agent to resolve a support case, escalate when necessary, retrieve data, and update the ticketing system—all based on an open-ended prompt. Here’s how you’d use a planner with function calling:

```
var plan = await actionPlanner.CreatePlanAsync(
 "For the following support request, diagnose the problem, suggest next steps, and escalate if unresolved. Ticket: {{$ticketDescription}}"
);

var result = await plan.InvokeAsync(kernel, new KernelArguments { ["ticketDescription"] = ticket });
```

The planner, powered by the LLM, will automatically select functions—be they semantic or native—and chain them as needed, reacting dynamically to each output.

### 6.2. Architectural Patterns for Semantic Kernel Applications

#### 6.2.1. The “Agent” Pattern: Encapsulating AI Logic

The agent pattern encapsulates your orchestration logic, plugins, and connectors behind a cohesive interface. This makes your AI component easily reusable and testable.

**Pattern example:**

```
public interface ISupportAgent
{
 Task AnalyzeTicketAsync(string ticketText);
}

public class SupportAgent : ISupportAgent
{
 private readonly IKernel _kernel;
 private readonly IPlanner _planner;
 // Constructor omitted for brevity

 public async Task AnalyzeTicketAsync(string ticketText)
 {
 var result = await _planner.InvokeAsync(_kernel, ticketText);
 // Map output to strong-typed result
 return ParseResult(result);
 }
}
```

This aligns with .NET’s focus on strong typing and interface-driven development.

#### 6.2.2. The “Chain of Responsibility” Pattern with Plugins

Often, multiple plugins can handle a request, and you may want to try them in sequence until one succeeds. This pattern, well-known in .NET circles, works naturally with Semantic Kernel plugins.

**Usage example:**

```
foreach (var plugin in plugins)
{
 var response = await plugin.TryHandleAsync(request);
 if (response.Success)
 return response;
}
```

This lets you layer fallback strategies, combine traditional code with LLM-driven logic, and make your agents more resilient.

#### 6.2.3. Designing for Testability: Mocking and Unit Testing Semantic Kernel Components

Testability is essential for enterprise-grade AI solutions. Semantic Kernel supports dependency injection, enabling you to inject mock connectors and services.

**Testing pattern:**

- Use interfaces (e.g., `IMemoryStore`, `IChatCompletionService`)
- Register mocks or in-memory implementations during testing
- Assert that planners and plugins behave as expected for given inputs

Example with a mocking library:

```
var mockMemory = new Mock ();
mockMemory.Setup(m => m.SearchAsync(...)).ReturnsAsync(...);
// Inject mockMemory into your agent for controlled unit tests
```

By decoupling orchestration from external services, you maintain high coverage and robust, change-resilient code.

### 6.3. Scalability, Performance, and Cost Management

#### 6.3.1. Caching Strategies for LLM Responses

LLM calls are expensive and sometimes slow. Implementing response caching can reduce both cost and latency.

- **Short-term cache:** Store responses for recent prompts in-memory (e.g., using `MemoryCache`).
- **Persistent cache:** For common queries, use distributed caches like Redis.

Pattern example:

```
var cacheKey = HashPrompt(prompt);
if (_cache.TryGetValue(cacheKey, out var cachedResponse))
 return cachedResponse;

// Otherwise, call LLM and cache result
var result = await kernel.InvokePromptAsync(prompt);
_cache.Set(cacheKey, result, TimeSpan.FromHours(1));
```

#### 6.3.2. Asynchronous Processing for Long-Running AI Tasks

Some AI workflows (like document summarization) can be time-consuming. Use asynchronous APIs throughout your Semantic Kernel code, and consider offloading to background processing systems (e.g., Azure Functions, Hangfire) for heavy workloads.

#### 6.3.3. Token Management and Optimizing for Cost

LLM cost is often tied directly to token usage (input + output). Monitor and optimize:

- Trim unnecessary context and verbose prompts
- Chunk long documents before sending to the LLM
- Aggregate requests when possible

Semantic Kernel lets you manage and inspect token usage, so you can track and optimize at every step.

### 6.4. Observability and Monitoring

#### 6.4.1. Integrating with Application Insights for Telemetry

Operational visibility is crucial. Semantic Kernel plays well with .NET observability tooling. With Azure Application Insights, you can track:

- LLM call durations and success rates
- Planner execution steps
- Memory and connector performance

Integrate with `ILogger` and diagnostic events for custom metrics.

#### 6.4.2. Logging and Debugging Semantic Kernel Workflows

Use structured logging ( `ILogger `) throughout your plugins and planners:

```
_logger.LogInformation("Invoking AnalyzeTicket function with prompt: {Prompt}", prompt);
```

When debugging, capture intermediate states, planner decisions, and kernel context objects. For production, ensure that sensitive information is never logged, and use log levels appropriately.

## 7\. Real-World Implementation: A “Corporate Knowledge Base” AI Agent

Let’s bring all these concepts together with a scenario increasingly relevant in today’s enterprises: an AI-powered knowledge base assistant.

### 7.1. The Vision: An AI Assistant that Answers Employee Questions Using Internal Documentation

Imagine a virtual assistant that fields employee questions—about benefits, IT issues, HR policies, or procedures—by searching your organization’s internal documentation, summarizing answers, and always providing sources. This isn’t just search. It’s semantic reasoning over your knowledge base.

### 7.2. Architecture Overview

#### 7.2.1. Leveraging Retrieval-Augmented Generation (RAG)

RAG marries the strength of LLMs with precise, organization-specific retrieval:

1. Retrieve: Use vector search to find relevant documents/snippets based on user queries.
2. Augment: Feed these results into the LLM as context.
3. Generate: Ask the LLM to synthesize a natural-language answer, citing sources.

This pattern enables factually grounded, up-to-date responses—critical for business trust.

#### 7.2.2. Components: ASP.NET Core API, Semantic Kernel, Azure OpenAI, and Azure AI Search

A modern .NET knowledge agent typically consists of:

- **ASP.NET Core Web API:** Receives user queries and returns answers
- **Semantic Kernel orchestration:** Manages retrieval, prompt construction, and LLM calls
- **Azure OpenAI:** Provides enterprise LLM capabilities
- **Azure AI Search:** Delivers scalable vector retrieval over corporate documents

### 7.3. Step-by-Step Implementation Guide

#### 7.3.1. Ingesting and Indexing Corporate Documents into Azure AI Search

Begin by converting your internal documentation (PDFs, docs, wikis) into text and splitting into chunks. Each chunk is vectorized (converted to embeddings) and indexed in Azure AI Search.

- Use Azure’s built-in skills or your own text extractors.
- Index metadata (source, title, URL) alongside the text.

#### 7.3.2. Building a “KnowledgeBase” Plugin with Semantic Memory

Implement a plugin that retrieves the most relevant document chunks for a given query:

```
public class KnowledgeBasePlugin
{
 private readonly ISemanticTextMemory _memory;
 public KnowledgeBasePlugin(ISemanticTextMemory memory) => _memory = memory;

 [KernelFunction]
 public async Task RetrieveRelevantSnippetsAsync(string question)
 {
 var results = await _memory.SearchAsync("knowledge-base", question, limit: 5, minRelevanceScore: 0.75);
 return string.Join("\n", results.Select(r => $"{r.Metadata.Text} [Source: {r.Metadata.ExternalSourceName}]"));
 }
}
```

#### 7.3.3. Creating an API Endpoint to Handle User Queries

Wire up your orchestration in a controller:

```
[ApiController]
[Route("api/knowledge")]
public class KnowledgeController : ControllerBase
{
 private readonly IKernel _kernel;
 public KnowledgeController(IKernel kernel) => _kernel = kernel;

 [HttpPost("ask")]
 public async Task Ask([FromBody] QuestionRequest request)
 {
 var snippets = await _kernel.InvokeFunctionAsync("KnowledgeBasePlugin", "RetrieveRelevantSnippetsAsync", request.Question);
 var answer = await _kernel.InvokePromptAsync(CreateKnowledgeBasePrompt(request.Question, snippets));
 return Ok(new { answer = answer.ToString() });
 }
}
```

#### 7.3.4. Crafting a Sophisticated Prompt to Synthesize Answers from Retrieved Documents

Prompts are the heart of RAG. You want to give the LLM enough context, but also instruct it to cite sources and admit uncertainty.

Example prompt template:

```
string CreateKnowledgeBasePrompt(string question, string context) =>
$@"You are an expert corporate assistant. Using only the following documentation snippets, answer the question below. If the answer is not found, say 'I don't know'.

Documentation:
{context}

Question: {question}
Answer (cite sources):";
```

#### 7.3.5. Handling “I don’t know” Scenarios and Providing Source Links

Effective assistants admit gaps in knowledge. Make it explicit in your prompt, and in post-processing, highlight when the LLM says “I don’t know.”

You can also parse the output for `[Source: ...]` tags and render clickable links in your frontend.

### 7.4. Deployment and CI/CD Considerations for AI Applications

#### 7.4.1. Managing Prompts and Configurations in a Production Environment

Prompts evolve. Store them in a configuration service (Azure App Configuration, Key Vault, or even database) rather than code, and support dynamic reloads. Version and test prompt changes before rollout.

#### 7.4.2. A/B Testing Different Prompts and Models

Continuous improvement is key. Route a fraction of users to different prompts or model configurations. Track outcomes, user feedback, and usage metrics. Use this data to refine your knowledge agent, ensuring it gets smarter and more helpful over time.

## 8\. The Future of Semantic Kernel and AI in the .NET Ecosystem

### 8.1. The Road Ahead: Multi-Modal Models, Autonomous Agents, and Beyond

The AI landscape is evolving rapidly:

- **Multi-modal models** (text, images, audio, code) are on the horizon. Semantic Kernel is architected to extend to these new modalities, allowing agents to process and generate across domains.
- **Autonomous agents** are moving from research to practice. Expect planners to become more sophisticated, blending symbolic reasoning with LLM-powered decision-making.
- **Tighter integration** with cloud-native and on-premises resources will further blur the line between AI agents and traditional software components.

### 8.2. The Growing Semantic Kernel Community and Resources

The Semantic Kernel community is expanding, with contributions from both Microsoft and open-source developers. You’ll find:

- Regular releases and feature additions
- A lively GitHub repository with issue tracking, discussions, and roadmap visibility
- Community samples, recipes, and deployment guides
- Integration projects for other languages (e.g., Python) and frameworks

Engage early. Contribute plugins, suggest features, and shape the evolution of .NET AI orchestration.

### 8.3. Final Thoughts: Empowering the Next Generation of .NET Applications

Semantic Kernel does more than enable AI in .NET. It provides a foundation for composable, testable, and maintainable intelligent systems that solve real business problems. The architects and developers who master these patterns will lead their organizations into the AI-powered future, delivering solutions that are not only smart, but also robust and trustworthy.

## 9\. Appendix

### 9.1. Glossary of Key Terms

- **LLM (Large Language Model):** AI models trained on large corpora to understand and generate natural language.
- **Prompt:** Input sent to an LLM to elicit a specific response.
- **Embedding:** A vector representation of text for semantic search and retrieval.
- **RAG (Retrieval-Augmented Generation):** Pattern combining document retrieval with LLM synthesis.
- **Connector:** Modular component enabling integration with external LLMs or memory stores.
- **Planner:** Module that sequences function calls, often with LLM input, to achieve a goal.
- **Semantic Function:** Function powered by an LLM prompt.
- **Native Function:** Function written in C#, performing deterministic logic or integrations.

### 9.2. Useful Links and Resources

- [Semantic Kernel Documentation](https://aka.ms/semantic-kernel)
- [Semantic Kernel GitHub Repository](https://github.com/microsoft/semantic-kernel)
- [Azure OpenAI Service](https://azure.microsoft.com/en-us/products/ai-services/openai-service)
- [Azure AI Search](https://azure.microsoft.com/en-us/products/ai-services/cognitive-search)
- [Microsoft Learn: AI for Developers](https://learn.microsoft.com/en-us/ai/?tabs=developer)

### 9.3. Full Code Examples

For complete, working code, visit the [semantic-kernel GitHub repository](https://github.com/microsoft/semantic-kernel/tree/main/dotnet/samples) or adapt the snippets provided in each section above to your solution.

##### Tags

[Ai](https://developersvoice.com/tags/ai/) [Ai agent](https://developersvoice.com/tags/ai-agent/) [Large Language Models](https://developersvoice.com/tags/large-language-models/)

##### Share this article

Help others discover this content

##### About Sudhir mangla

Content creator and writer passionate about sharing knowledge and insights.

[View all articles by Sudhir mangla →](https://developersvoice.com/authors/sudhir-mangla/)

## Related Posts

Discover more content that might interest you

![Fine-Tuning LLMs with C#: A Practical Guide to Customizing Models with ML.NET](https://developersvoice.com/_astro/assets/fine-tuning-llms-with-csharp.DXIZUr4q_Z1yjcVE.webp)

#### [Fine-Tuning LLMs with C\#: A Practical Guide to Customizing Models with ML.NET](https://developersvoice.com/blog/ai-development/fine-tuning-llms-with-csharp/)

- [Sudhir mangla](https://developersvoice.com/authors/sudhir-mangla/)
- [Artificial Intelligence](https://developersvoice.com/categories/artificial-intelligence/)
- 20 Jun, 2025

Abstract As artificial intelligence continues to shape the modern enterprise, Large Language Models (LLMs) like GPT, Llama, and Mistral are increasingly integrated into business solutions. While

[Read More](https://developersvoice.com/blog/ai-development/fine-tuning-llms-with-csharp/)

![Architecting LLM-Powered Applications: A Comprehensive Guide for .NET Architects](https://developersvoice.com/_astro/assets/architecting-llm-powered-applications.z77-BWDn_Zy2lYI.webp)

#### [Architecting LLM-Powered Applications: A Comprehensive Guide for .NET Architects](https://developersvoice.com/blog/ai-development/architecting-llm-powered-applications/)

- [Sudhir mangla](https://developersvoice.com/authors/sudhir-mangla/)
- [Artificial Intelligence ,](https://developersvoice.com/categories/artificial-intelligence/) [Genai patterns](https://developersvoice.com/categories/genai-patterns/)
- 26 Jun, 2025

Abstract This guide offers .NET architects a comprehensive framework for designing, building, and deploying robust applications powered by Large Language Models (LLMs). Moving beyond theoretical

[Read More](https://developersvoice.com/blog/ai-development/architecting-llm-powered-applications/)

![AI as the Architect’s Copilot: Leveraging GenAI for System Design and Documentation (2025 Guide)](https://developersvoice.com/_astro/assets/genai-for-system-design-and-documentation.F79pNhzU_Z25T08t.webp)

#### [AI as the Architect’s Copilot: Leveraging GenAI for System Design and Documentation (2025 Guide)](https://developersvoice.com/blog/ai-development/genai-for-system-design-and-documentation/)

- [Sudhir mangla](https://developersvoice.com/authors/sudhir-mangla/)
- [Artificial Intelligence](https://developersvoice.com/categories/artificial-intelligence/)
- 09 Jul, 2025

1\. Introduction: The New Architectural Imperative 1.1. The Modern Architect’s Dilemma If you’re a solution architect, system architect, or technical leader, you’re living in a time of rel

[Read More](https://developersvoice.com/blog/ai-development/genai-for-system-design-and-documentation/)

![Using LangChain with C#: A Primer for Building Composable AI Applications](https://developersvoice.com/_astro/assets/using-langchain-with-csharp.DtVo0cqL_19z8Ou.webp)

#### [Using LangChain with C\#: A Primer for Building Composable AI Applications](https://developersvoice.com/blog/ai-development/using-langchain-with-csharp/)

- [Sudhir mangla](https://developersvoice.com/authors/sudhir-mangla/)
- [Artificial Intelligence](https://developersvoice.com/categories/artificial-intelligence/)
- 01 Jul, 2025

1\. Introduction: The New Paradigm of AI-Native Applications 1.1 Beyond the API Call: The Shift to Composable, Intelligent Systems AI has quickly evolved from a futuristic concept to a key

[Read More](https://developersvoice.com/blog/ai-development/using-langchain-with-csharp/)

![Building with Azure OpenAI On Your Data: A Secure and Private Alternative to Public APIs](https://developersvoice.com/_astro/assets/azure-openai-on-your-data.CV31do7w_Z1T5bjD.webp)

#### [Building with Azure OpenAI On Your Data: A Secure and Private Alternative to Public APIs](https://developersvoice.com/blog/ai/azure-openai-on-your-data/)

- [Sudhir mangla](https://developersvoice.com/authors/sudhir-mangla/)
- [Artificial Intelligence ,](https://developersvoice.com/categories/artificial-intelligence/) [Enterprise AI](https://developersvoice.com/categories/enterprise-ai/)
- 02 Jul, 2025

1\. Introduction: The New Frontier of Enterprise AI 1.1 The Generative AI Revolution: A Paradigm Shift in Artificial Intelligence The world of artificial intelligence has undergone a quiet

[Read More](https://developersvoice.com/blog/ai/azure-openai-on-your-data/)

![What is a Vector Database? The Missing Piece in Your GenAI .NET Application Explained](https://developersvoice.com/_astro/assets/vector-database.C3ZS1yFY_1YVE6Y.webp)

#### [What is a Vector Database? The Missing Piece in Your GenAI .NET Application Explained](https://developersvoice.com/blog/ai-development/vector-database/)

- [Sudhir mangla](https://developersvoice.com/authors/sudhir-mangla/)
- [Artificial Intelligence](https://developersvoice.com/categories/artificial-intelligence/)
- 23 Jun, 2025

1\. Introduction: The Generative AI Revolution and the Unseen Challenge for .NET Architects 1.1 The Generative AI Gold Rush Over the past several years, the landscape of software developme

[Read More](https://developersvoice.com/blog/ai-development/vector-database/)

[![Developers Voice | The Software Architects Hub](https://developersvoice.com/_astro/assets/MainLogo.CORfMhAy_Z13ixJq.webp)![Developers Voice | The Software Architects Hub](https://developersvoice.com/_astro/assets/MainLogoDark.B0va-2kM_1zFQ5x.webp)](https://developersvoice.com/)
Highlights: None
Highlight Scores: None
Summary: None

END search and content demo
