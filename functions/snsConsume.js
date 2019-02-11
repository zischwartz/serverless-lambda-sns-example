module.exports.handler = async (event, context) => {
  let message = event.Records[0].Sns.Message;
  console.log("Hello from JAVASCRIPT!!! - also consuming");
  console.log("Received MESSAGE: " + message);

  return message;
};
