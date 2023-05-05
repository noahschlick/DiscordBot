## Introduction

FreeWater Chatbot is a user-friendly and interactive chatbot designed to answer questions and provide information about the innovative FreeWater advertising platform. The platform provides an eco-friendly alternative to bottled water. The chatbot is built using Python and utilizes an AI model to provide accurate and timely responses to user messages. The chatbot is hosted on Replit, a powerful online code editor and hosting platform, making it easy to deploy and manage. With its intuitive interface and rich features, FreeWater Chatbot is an excellent tool for anyone looking to learn more about this revolutionary platform.
## Project Structure
The project contains four Python files: main.py, bot.py, freeWaterAPI.py, and webserver.py.
### main.py:
This file is the main entry point for the application. It loads the environment variables using the python-dotenv package and starts the Discord bot using the run_discord_bot() function in the bot.py file.
### bot.py:
This file contains the main functionality for the Discord chatbot. The run_discord_bot() function initializes a Discord client and starts listening for messages. It uses the freeWaterAPI.py file to get responses to user messages and sends them back as a private message or a message in the channel. The send_message() function in the bot.py file sends the message response.

## run_discord_bot
The run_discord_bot function is a Python function that sets up a Discord bot using the discord.py library and listens for user messages in a specific Discord channel. The function takes an optional p_token parameter, which is used to specify a different Discord API token than the one stored in the DISCORD_TOKEN environment variable.

The function first creates a discord.Client instance with default intents, and then retrieves the Discord API token from the environment variable or from the p_token parameter. It then sets up a few event listeners using the @client.event decorator, including an on_ready event that prints a message to the console when the bot is started, and an on_message event that listens for messages in a specific channel and responds to them.

The on_message event listener retrieves the author, content, and channel of each message, and then sends a response to the user using the send_message function. The send_message function is not shown in the code snippet, but it is assumed to be a separate function that sends a response message to the user.

Finally, the function enters a loop that attempts to run the Discord bot using the specified token. If the token is not valid, the function prompts the user to enter a valid token. If an error occurs, the function prints the error message to the console.

## send_message
The send_message function is a Python function that sends a response message to a user based on their input message. The function takes three parameters: message, user_message, and is_private.

The message parameter represents the Discord message object that triggered the function call, while the user_message parameter represents the user's input message. The is_private parameter is a boolean value indicating whether the response should be sent as a private message or in the same channel as the original message.

The function first tries to get a response from an external API using the freeWaterAPI.getAnswer function. If the API call is successful, the function retrieves the response field from the JSON response object and sends it to the user using either the message.author.send method (if is_private is True) or the message.channel.send method (if is_private is False).

If an error occurs during the API call or the sending of the response message, the function catches the exception and sends an error message to the user using the same send methods as before. The error message indicates that the bot is not currently connected to the API that helps it answer questions.


##
### freeWaterAPI.py:
This file contains the function to call the FreeWater AI API and get a response to a user's input message. You can view the FreeWater AI API in https://github.com/noahschlick/FreeWaterChatBotAPI

## Deployment
The project can be deployed on any hosting platform that supports Python, such as Replit. Before deploying, the following steps should be taken:
1. Create a Discord bot and obtain the bot token.
2. Create an account on Replit and create a new project.
3. Add the following dependencies to the requirements.txt file: discord, python-dotenv, Flask, and requests.
4. Create a .env file and add the Discord bot token to it.
5. Copy the code from the four Python files into the corresponding files in the Replit project.
6. Start the Flask application using the keep_alive() function in the webserver.py file.
7. Start the Discord bot using the run_discord_bot() function in the bot.py file.

## My Step by Step procedure
 1. The discord bot was the second part of this project. Seeing that the REST API could be used for other platforms, I felt that it was best to have the discord bot on a separate server using the REST API chatbot. The first thing that I did was set up a discord bot. The Discord bot was can be created in the discord developer portal (log in with regular discord accout on their website). I created a new application and gave the application a name. Once I created the application, I created the bot by going to the bot tab on the left side then clicked add bot. Under the bot tab you can customize the bot by adding a bot name and image(optional). I generated a token on this page by clicking the token button. I invited the bot to a server I created in my discord account. Under the OAuth2 tab in discord, I selected the bot scope and gave it the permissions that I wanted the bot to have. I gave it the basic functionality to write public and private messages in the server. I chose the server that I wanted to invite the bot to then clicked authorize.
 2. The Token is sensitive information that can not be public. Making the token public increases the risk for attack. Therefore I created a .env file to hide the token from github and a gitignore file so that the .env will not be pulled with the other files on github. There is also a try and except clause when calling the token. If the token is not read, then the program will prompt the user to enter a token. The run_discord_bot function which initiates the discord bot using the DISCORD-TOKEN environment variable.
 4. I wrote the send_message function which sends a resonse to the user in discord. I had already created the REST API that generates an response based off of the FreeWater training data at this point. The API takes in the user_message parameter and generates an educated resonse. I used the discord message object from the discord package to to write the response in discord. I wrote a try and except clause incase the API was not working to notify the discord users that the bot is not connected to the API. I also wrote functionality where the bot would reply with a private message if the prompt had  question mark infront of it. 
 5. I am hosting the chatbot on a virtual machine in google cloud. I orginally had the code hosting on replit but after testing I realized that the server would stop running in random intervals after every few hours. I later found out a way to host the bot on a virtual machine in google cloud. I then uploaded the files through the virtual machine's shell. I ran the command tmux on the shell which keeps the code running on the server. The Virtual machine is hosted on a server on the east cost which is were the discord server is located as well. This will help with shorter latency when making a prompt. 


## Conclusion:
FreeWater Chatbot is a simple chatbot that demonstrates how to use an AI model to respond to user messages on Discord. It can be easily deployed on any hosting platform that supports Python.