const { sayHello } = require("@axsm-nathan/hello-world");

exports.hello = async (event) => {
  const name = event?.queryStringParameters?.name || "World";
  return {
    statusCode: 200,
    body: JSON.stringify({
      message: sayHello(name),
    }),
  };
};
