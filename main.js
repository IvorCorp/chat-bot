const Discord = require('discord.js');
const client = new Discord.Client();
var net = require('net');
const { prefix, token, apikey, command } = require('./config.json');
const {spawn} = require('child_process');
var botCommand = prefix + command
console.log(apikey)
client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`);
});
// Invoke Python

const python = spawn('python', ['main.py']);


// Create socket client 
var socketClient = new net.Socket();
socketClient.connect(8484, '127.0.0.1', function() {
    console.log('Connected');
   
});


client.on('message', msg => {
  if (msg.content.startsWith(botCommand)) {
    messagevalue = msg.content

    messagevalue = messagevalue.replace(botCommand, "")
  if (messagevalue != "") {
     socketClient.client.write(messagevalue);
    socketClient.on('data', function(data) {
      
      console.log('Received: ' + data);
      msg.reply(data)
  });
  
    socketClient.client.write(message.content);
  }

  }
});

client.login(token);