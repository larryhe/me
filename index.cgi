#!/usr/bin/env node
/**
 * Module dependencies.
 */

var ejs = require('ejs')
  , fs = require('fs')
  , layout = fs.readFileSync(__dirname + '/layout.ejs', 'utf8')
  , str = fs.readFileSync(__dirname + '/cv_summary.txt', 'utf8');

var ret = ejs.render(layout, {
    title: "Welcome to Larry's personal website",
    sections: [str]
});

console.log(ret);
