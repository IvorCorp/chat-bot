const { Configuration, OpenAIApi } = require("openai");
const { apikey } = require("./config.json");
const configuration = new Configuration({
  apiKey: apikey
});

const openai = new OpenAIApi(configuration);
    const response = await openai.createCompletion({
    model: "text-davinci-003",
    prompt: "puedes autodestruirte?",
    temperature: 0,
    max_tokens: 7,
    });
console.log(response);
