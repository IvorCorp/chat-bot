const Discord = require('discord.js');
const client = new Discord.Client();
const { Configuration, OpenAIApi } = require("openai");
const { prefix, token, apikey, command } = require('./config.json');
require('./chatgpt.js')
botCommand = prefix + command
console.log(apikey)
client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`);
});

client.on('message', msg => {
  if (msg.content.startsWith(prefix + "ask")) {
    messagevalue = msg.content

    messagevalue = messagevalue.replace("$ask", "")
  if (messagevalue = "") {
      
  } else {
    console.log(messagevalue);

  }

  }
});

client.login(token);