CREATE DATABASE `simmons_testbed`;
USE `simmons_testbed`;

CREATE USER `user`@`%` IDENTIFIED BY `1234`;
GRANT ALL PRIVILEGES ON *.* TO `user`@`%` WITH GRANT OPTION;
FLUSH PRIVILEGES;


DROP TABLE IF EXISTS `user`
CREATE TABLE `user`(
`id_num` int not null AUTO_INCREMENT first,
`howmany` int,
`nowcheck` boolean not null default 0,
`xboundary` int not null,
`yboundary` int not null,
PRIMARY KEY (`id_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

 create table CryDetect(
 id_num int not null AUTO_INCREMENT primary key, 
 sound int not null, 
 result int not null, 
 created_at datetime not null);