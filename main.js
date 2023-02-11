const Discord = require('discord.js');
const client = new Discord.Client();
const { prefix } = require('./config.json');
const { token } = require('./config.json')
command = prefix + "ask"

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