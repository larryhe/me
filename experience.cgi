#!/usr/bin/env node
/**
 * Module dependencies.
 */

var ejs = require('ejs')
  , fs = require('fs')
  , str = fs.readFileSync(__dirname + '/layout.ejs', 'utf8');

var ret = ejs.render(str, {
    title: 'Welcome to Larrys resume',
    content: 'content of resume',
    sections: ['Section1', 'Section2']
});

console.log(ret);
