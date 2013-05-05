#!/usr/bin/env node
var me = require('./me'),
    Base = me.Base,
    fs = require('fs'),
    index = Base.extend({
    options: {
            sidebar: fs.readFileSync(__dirname + '/repos.ejs', 'utf8')
        }
    });
new index().render();
