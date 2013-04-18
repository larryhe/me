CREATE TABLE user (
    name varchar(30) primary key,
    password varchar(30) ,
    role varchar(30)
);

CREATE TABLE blog (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title varchar(50),
    content text ,
    tag int,
    created_date varchar(10),
    status int, /*1 drafted, 2 published, 3 deleted*/
    FOREIGN KEY(tag) references tag(id)
);

CREATE TABLE tag (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    desc varchar(20)
);
