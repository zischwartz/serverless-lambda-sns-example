const request = require("supertest");
const expect = require("chai").expect;
const getSlsOfflinePort = require("../support/getSlsOfflinePort");

// describe("postSnsPublish", function postSnsPublishTest() {
//   // this.timeout(10000);
//   it("ok", function it(done) {
//     global.global.slsOfflineProcess.stdout.on("data", data => {
//       console.log("there was data");
//       console.log(data.toString());
//       // data = data.toString();
//       if (data.includes('Received MESSAGE: {"msg":"stub message"}')) {
//         done();
//       }
//     });
//
//     request(`http://localhost:${getSlsOfflinePort()}`)
//       .post(`/snsPublish`)
//       .send({ msg: "stub message" })
//       .expect(200)
//       .end(function(error, result) {
//         if (error) {
//           return done(error);
//         }
//       });
//   });
// });

describe("postSnsPublish 2", function postSnsPublishTest() {
  // this.timeout(10000);
  it("ok", function it(done) {
    global.global.slsOfflineProcess.stdout.on("data", data => {
      console.log("there was data");
      // console.log(data);
      console.log(data.toString());
      // console.log("---");
      // data = data.toString();
      if (data.includes("HELLO FROM PYTHON - consuming")) {
        done();
      }
    });

    request(`http://localhost:${getSlsOfflinePort()}`)
      .post(`/snsPublish`)
      .send({ msg: "stub message" })
      .expect(200)
      .end(function(error, result) {
        if (error) {
          return done(error);
        }
      });
  });
});
