#!/usr/bin/env node
var me = require('./me');
var Base = me.Base;
var blog = Base.extend({
    options: {
        tab : 'blog',
        title : 'My blogs'
    },
    getContent: function(){
        return this.fs.readFileSync(__dirname + '/blog.ejs', 'utf8');
    }
});
new blog().render();
