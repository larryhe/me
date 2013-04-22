#!/usr/bin/env node
var fs = require('fs');
var me = require('./me');
var Base = me.Base;
var blog = Base.extend({
    options: {
        tab : 'blog',
        title : 'My blogs',
        content: fs.readFileSync(__dirname + '/blog.ejs', 'utf8')
    }
});
new blog().render();
