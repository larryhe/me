#!/usr/bin/env node
var ejs = require('ejs')
  , fs = require('fs')
  , layout = fs.readFileSync(__dirname + '/layout.ejs', 'utf8');

var ret = ejs.render(layout, {
    title: "My blogs",
    filename: 'layout.ejs',
    main: 'blog',
    tab: 'blog'
});
console.log('Content-type: text/html');
console.log('');
console.log(ret);
