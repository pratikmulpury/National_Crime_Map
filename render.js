const express = require('express');
const path = require('path');
const history = require('connect-history-api-fallback');

const app = express();

// serve static files from the dist directory (where all the built files are)
const staticFileMiddleware = express.static(path.join(__dirname + '/dist'));

app.use(staticFileMiddleware);
app.use(history({
  disableDotRule: true,
  verbose: true
}));
app.use(staticFileMiddleware);

// respond to browser requests
app.get('/', function (req, res) {
  res.render(path.join(__dirname + '/dist/index.html'));
});

// run on port 8080 or the environment port
var server = app.listen(process.env.PORT || 8080, function () {
  var port = server.address().port;
  console.log("App now running on port", port);
});

