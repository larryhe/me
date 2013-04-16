#!/usr/bin/env node
var ejs = require('ejs')
  , fs = require('fs')
  , layout = fs.readFileSync(__dirname + '/layout.ejs', 'utf8');

var ret = ejs.render(layout, {
    title: "Welcome to Larry's personal website",
    filename: 'layout.ejs',
    main: 'cv',
    tab: 'me'
});
console.log('Content-type: text/html');
console.log('');
console.log(ret);
