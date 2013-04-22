#!/usr/bin/env node
var fs = require('fs');
var me = require('../me');
var Base = me.Base;
var manage = Base.extend({
    options: {
        tab : 'none',
        title : 'Blog management page',
        content: fs.readFileSync(__dirname + '/manage.ejs', 'utf8'),
        sidebar: ''
    }
});
new manage().render();
