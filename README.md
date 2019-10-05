# Build your Chatbot for find products and productID at Sendo.vn using the Rasa Stack
This is the **Complete Version** of the Chatbot Sendo and can be directly used with slack by filling **slack_credentials.yml**

## Setup and Installation
**Creating a virtual environment**:
```php
conda create --name botvi python=3.6
```
**Activate the new environment to use it**:
```php
LINUX, macOS: $ conda activate botvi
WINDOWS: $ activate botvi
```
## Install latest Rasa stack
### Rasa NLU
`pip install -U rasa_nlu`
### Rasa_core
`pip install -U rasa_core`
### Rasa_core_sdk
`pip install -U rasa_core_sdk`
## For dependencies
### Tensorflow (pipeline)
`pip install rasa_nlu[tensorflow]`
## Files for Rasa NLU model
* **data/nlu_vi.md** file contents training data for the NLU model.
* **nlu_config.yml** file contains the configuration of the Rasa NLU pipeline:
```php
language: "vi"
pipeline: "supervised_embeddings"
```
## Files for Rasa Core model
* **data/stories.md** file contains some training stories which represent the conversations between a user and the assistant.
* **domain.yml file** describes the domain of the assistant which includes intents, entities, slots, templates and actions the assistant should be aware of.
* **actions.py** file contains the code of a custom action which returns search results on api sendo.vn depending on actions.
* **endpoints.yml** file contains the webhook configuration for custom action.
* **policy.yml** file contains the configuration of the training policies for Rasa Core model.
## How to run Bot
**Note**: If running on Windows, you will either have to [install make](http://gnuwin32.sourceforge.net/packages/make.htm) or copy the following commands from the [Makefile](https://github.com/namnguyenduc/BotSendo/blob/master/Makefile)
1. You can train the Rasa NLU model by running:  
```php
make train-nlu
```
+ This will train the Rasa NLU model and store it inside the `/models/current/nlu` folder of your project directory.
2. Train the Rasa Core model by running: 
```php
make train-core
```
+ This will train the Rasa Core model and store it inside the `/models/dialogue` folder of your project directory.
3. Open a new terminal start the server for the custom action by running(*Keep this terminal running*):
```php
make actions
```
+ This will start the server for emulating the custom action.
## How to deploy to Slack
1. Go to your Slack app's settings page and use the **Bot User OAuth Access Token**:
![](https://github.com/namnguyenduc/BotSendo/blob/master/images/bot_token.png)
this in the slack_credentials.yml file:
```
slack:
  slack_token: "Bot User OAuth Access Token"
  slack_channel: 
```
**Ngrok** is multiplatform tunneling, reverse proxy software that establishes secure tunnels from a public endpoint such as the internet to a locally running network service while capturing all traffic for detailed inspection and replay.
<br>[***Download ngrok***](https://ngrok.com/download)

2. Setup ngrok for the port that the action server is using by the following command.
You can customize the port as you like.(*If you choose another port, set the port parameters correctly in Makefile*). Here I choose port 5002:
```
ngrok http 5002
```
This will give you an output like the following:
![](https://github.com/namnguyenduc/BotSendo/blob/master/images/Capture.PNG)
3. Now, the last step let's run command 
```php
make cmdline
```
4. Take the above url and paste it into the Events Subscription page of your slack app in the following format:
```
your_url_here/webhooks/slack/webhook
```
![](https://github.com/namnguyenduc/BotSendo/blob/master/images/event_subs.png)
<br>And you should now be able to talk to your chatbot in Slack!
<br>**Note**: The bot runs on the terminal, so you have to download Vietnamese typing software on the terminal to be able to communicate with the Bot.&ensp;[Gõ Tiếng Việt](https://www.trankynam.com/gotv/)
