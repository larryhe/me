#!/usr/bin/env node
/**
 * Module dependencies.
 */

var ejs = require('ejs')
  , fs = require('fs')
  , layout = fs.readFileSync(__dirname + '/layout.ejs', 'utf8');

var ret = ejs.render(layout, {
    title: 'Welcome to Larrys resume',
    content: 'content of resume',
    sections: ['Section1', 'Section2']
});

console.log('Content-type: text/html');
console.log('');
console.log(ret);
