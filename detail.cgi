#!/usr/bin/env node
var fs = require('fs'),
    ejs = require('ejs'),
    me = require('./me'),
    layout = fs.readFileSync(__dirname + '/detail.ejs', 'utf8'),
    exec = require('child_process').execFile,
    queryStr = process.env.QUERY_STRING,
    id = queryStr.substring(queryStr.indexOf('=')+1),
    id = parseInt(id);
    exec('./admin/query.sh',['./admin/config.txt',id], function(error, stdout, stderr){
        var attrs = stdout.split('|'),
            Base = me.Base,
            blog = Base.extend({
            options: {
                tab : 'blog',
                title : attrs[0],
                content: ejs.render(layout, {title: attrs[0], content: attrs[1], postedDate: attrs[2], tag: attrs[3]})
            }
        });
        new blog().render();
    });
