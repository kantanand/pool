drop database if exists pooldb;
create database pooldb CHARACTER SET utf8 COLLATE utf8_general_ci;

grant all on pooldb.* to 'pooladmin'@'localhost' identified by 'pool@123#';


use pooldb;

create table if not exists `pool_users` (
        id INT UNSIGNED NOT NULL AUTO_INCREMENT,
        user_id varchar(40) NOT NULL,
        age int DEFAULT '0' NOT NULL,
        gender varchar(20) NOT NULL,
        mobile varchar(20) ,
        location varchar(30) ,
        PRIMARY KEY (user_id)
)ENGINE=INNODB CHARSET=utf8;

create table if not exists `pool_tag_master` (
        pool_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
        pool_tag varchar(100) NOT NULL,
	question text NOT NULL,
	option1 text NOT NULL,
	option2 text NOT NULL,
	option3 text NOT NULL,
	option4 text NOT NULL,
	user_id varchar(40) NOT NULL,
        age int DEFAULT '0' NOT NULL,
        gender varchar(20) NOT NULL,
        pool_start timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
	pool_end timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
	pool_tag_created timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
	option1_count INT UNSINGNED NOT NULL DEFAULT '0',
	option2_count INT UNSINGNED NOT NULL DEFAULT '0',
	option3_count INT UNSINGNED NOT NULL DEFAULT '0',
	option4_count INT UNSINGNED NOT NULL DEFAULT '0',

       	PRIMARY KEY (pool_tag),
	CONSTRAINT pool_tag_user FOREIGN KEY (user_id) REFERENCES pool_users(user_id)
)ENGINE=INNODB CHARSET=utf8;



create table if not exists 'pool_tag_answer'(
	answer_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
        pool_tag varchar(100) NOT NULL,
	option_selected varchar(10) NOT NULL,
	option_text text NOT NULL,
	user_id varchar(40) NOT NULL,
        age int DEFAULT '0' NOT NULL,
        gender varchar(20) NOT NULL,
	pool_tag_answered timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
       	PRIMARY KEY (answer_id),
	CONSTRAINT pool_tag_user FOREIGN KEY (user_id) REFERENCES pool_users(user_id),
	CONSTRAINT pool_tag_question FOREIGN KEY (pool_tag) REFERENCES pool_tag_master(pool_tag)
)ENGINE=INNODB CHARSET=utf8;
