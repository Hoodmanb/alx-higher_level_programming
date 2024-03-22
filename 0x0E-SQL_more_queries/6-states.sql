-- a script that create a dtabase, a table with a unique and primar key
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`states` (PRIMARY KEY(`id`), `id` INT  NOT NULL AUTO_INCREMENT, `name` VARCHAR(256) NOT NULL);
