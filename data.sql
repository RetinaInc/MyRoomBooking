create database if not exists room  default charset utf8 collate utf8_general_ci;

create table room (
  `id` int not NULL primary key auto_increment, 
  `name` varchar(255) default '', 
  `floor` int not Null, 
  `room` varchar(255) default ''
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

create table booking (
  `id` int not NULL primary key auto_increment, 
  `room_id` int not null,
  `user_id` int not Null, 
  `start_time` timestamp, 
  `end_time` timestamp, 
  `title` varchar(255), 
  `info` varchar(500) default ''
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


create table user (
  `id` int not null primary key auto_increment,
  `cn_name` varchar(255) not null,
  `en_name` varchar(255) default '', 
  `password` varchar(255) not null 
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

