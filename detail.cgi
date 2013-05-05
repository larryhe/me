#!/usr/bin/env node
var fs = require('fs'),
    ejs = require('ejs'),
    me = require('../me'),
    layout = fs.readFileSync(__dirname + '/detail.ejs', 'utf8'),
    Base = me.Base,
    blog = Base.extend({
    options: {
        tab : 'blog',
        title : process.env.QUERY_STRING,
        content: ejs.render(layout)
    }
});
new blog().render();
