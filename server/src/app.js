const express = require('express')
const bodyParser = require('body-parser')
const cors = require('cors')
const morgan = require('morgan')



// set up google oauth2client
const {OAuth2Client} = require('google-auth-library');
const client = new OAuth2Client('677447604640-rnbtov97fi21skrh09u96mngv12gek5a.apps.googleusercontent.com');


app.listen(process.env.PORT || 8081)
