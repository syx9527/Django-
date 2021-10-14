/*
MySQL Backup
Database: my_blog
Backup Time: 2021-10-14 23:09:18
*/

SET FOREIGN_KEY_CHECKS=0;
DROP TABLE IF EXISTS `my_blog`.`auth_group`;
DROP TABLE IF EXISTS `my_blog`.`auth_group_permissions`;
DROP TABLE IF EXISTS `my_blog`.`auth_permission`;
DROP TABLE IF EXISTS `my_blog`.`blog_article2tag`;
DROP TABLE IF EXISTS `my_blog`.`blog_article`;
DROP TABLE IF EXISTS `my_blog`.`blog_articleupdown`;
DROP TABLE IF EXISTS `my_blog`.`blog_blog`;
DROP TABLE IF EXISTS `my_blog`.`blog_category`;
DROP TABLE IF EXISTS `my_blog`.`blog_comment`;
DROP TABLE IF EXISTS `my_blog`.`blog_tag`;
DROP TABLE IF EXISTS `my_blog`.`blog_userinfo`;
DROP TABLE IF EXISTS `my_blog`.`blog_userinfo_groups`;
DROP TABLE IF EXISTS `my_blog`.`blog_userinfo_user_permissions`;
DROP TABLE IF EXISTS `my_blog`.`django_admin_log`;
DROP TABLE IF EXISTS `my_blog`.`django_content_type`;
DROP TABLE IF EXISTS `my_blog`.`django_migrations`;
DROP TABLE IF EXISTS `my_blog`.`django_session`;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE `blog_article2tag` (
  `nid` int NOT NULL AUTO_INCREMENT,
  `article_id` int NOT NULL,
  `tag_id` int NOT NULL,
  PRIMARY KEY (`nid`),
  UNIQUE KEY `blog_article2tag_article_id_tag_id_b0745f42_uniq` (`article_id`,`tag_id`),
  KEY `blog_article2tag_tag_id_389b9a96_fk_blog_tag_nid` (`tag_id`),
  CONSTRAINT `blog_article2tag_article_id_753a2b60_fk_blog_article_nid` FOREIGN KEY (`article_id`) REFERENCES `blog_article` (`nid`),
  CONSTRAINT `blog_article2tag_tag_id_389b9a96_fk_blog_tag_nid` FOREIGN KEY (`tag_id`) REFERENCES `blog_tag` (`nid`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE `blog_article` (
  `nid` int NOT NULL AUTO_INCREMENT,
  `title` varchar(50) NOT NULL,
  `desc` varchar(255) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `content` longtext NOT NULL,
  `category` int DEFAULT NULL,
  `user` int NOT NULL,
  `comment_count` int NOT NULL,
  `down_count` int NOT NULL,
  `up_count` int NOT NULL,
  PRIMARY KEY (`nid`),
  KEY `blog_article_category_f0bac9b4_fk_blog_category_nid` (`category`),
  KEY `blog_article_user_4a9f1839_fk_blog_userinfo_nid` (`user`),
  CONSTRAINT `blog_article_category_f0bac9b4_fk_blog_category_nid` FOREIGN KEY (`category`) REFERENCES `blog_category` (`nid`),
  CONSTRAINT `blog_article_user_4a9f1839_fk_blog_userinfo_nid` FOREIGN KEY (`user`) REFERENCES `blog_userinfo` (`nid`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE `blog_articleupdown` (
  `nid` int NOT NULL AUTO_INCREMENT,
  `is_up` tinyint(1) NOT NULL,
  `article_id` int DEFAULT NULL,
  `user_id` int DEFAULT NULL,
  PRIMARY KEY (`nid`),
  UNIQUE KEY `blog_articleupdown_article_id_user_id_fa3d0c08_uniq` (`article_id`,`user_id`),
  KEY `blog_articleupdown_user_id_2c0ebe49_fk_blog_userinfo_nid` (`user_id`),
  CONSTRAINT `blog_articleupdown_article_id_9be1a8a2_fk_blog_article_nid` FOREIGN KEY (`article_id`) REFERENCES `blog_article` (`nid`),
  CONSTRAINT `blog_articleupdown_user_id_2c0ebe49_fk_blog_userinfo_nid` FOREIGN KEY (`user_id`) REFERENCES `blog_userinfo` (`nid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE `blog_blog` (
  `nid` int NOT NULL AUTO_INCREMENT,
  `title` varchar(64) NOT NULL,
  `site_name` varchar(64) NOT NULL,
  `theme` varchar(32) NOT NULL,
  PRIMARY KEY (`nid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE `blog_category` (
  `nid` int NOT NULL AUTO_INCREMENT,
  `title` varchar(32) NOT NULL,
  `blog` int NOT NULL,
  PRIMARY KEY (`nid`),
  KEY `blog_category_blog_3087945f_fk_blog_blog_nid` (`blog`),
  CONSTRAINT `blog_category_blog_3087945f_fk_blog_blog_nid` FOREIGN KEY (`blog`) REFERENCES `blog_blog` (`nid`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE `blog_comment` (
  `nid` int NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  `content` varchar(255) NOT NULL,
  `article_id` int NOT NULL,
  `parent_comment_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`nid`),
  KEY `blog_comment_article_id_3d58bca6_fk_blog_article_nid` (`article_id`),
  KEY `blog_comment_parent_comment_id_26791b9a_fk_blog_comment_nid` (`parent_comment_id`),
  KEY `blog_comment_user_id_59a54155_fk_blog_userinfo_nid` (`user_id`),
  CONSTRAINT `blog_comment_article_id_3d58bca6_fk_blog_article_nid` FOREIGN KEY (`article_id`) REFERENCES `blog_article` (`nid`),
  CONSTRAINT `blog_comment_parent_comment_id_26791b9a_fk_blog_comment_nid` FOREIGN KEY (`parent_comment_id`) REFERENCES `blog_comment` (`nid`),
  CONSTRAINT `blog_comment_user_id_59a54155_fk_blog_userinfo_nid` FOREIGN KEY (`user_id`) REFERENCES `blog_userinfo` (`nid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE `blog_tag` (
  `nid` int NOT NULL AUTO_INCREMENT,
  `title` varchar(32) NOT NULL,
  `blog_nid` int NOT NULL,
  PRIMARY KEY (`nid`),
  KEY `blog_tag_blog_nid_1b83fa94_fk_blog_blog_nid` (`blog_nid`),
  CONSTRAINT `blog_tag_blog_nid_1b83fa94_fk_blog_blog_nid` FOREIGN KEY (`blog_nid`) REFERENCES `blog_blog` (`nid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE `blog_userinfo` (
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `nid` int NOT NULL AUTO_INCREMENT,
  `telephone` varchar(11) DEFAULT NULL,
  `avatar` varchar(100) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `blog_id` int DEFAULT NULL,
  PRIMARY KEY (`nid`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `telephone` (`telephone`),
  UNIQUE KEY `blog_id` (`blog_id`),
  CONSTRAINT `blog_userinfo_blog_id_aa34488f_fk_blog_blog_nid` FOREIGN KEY (`blog_id`) REFERENCES `blog_blog` (`nid`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE `blog_userinfo_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `userinfo_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `blog_userinfo_groups_userinfo_id_group_id_5f60ecec_uniq` (`userinfo_id`,`group_id`),
  KEY `blog_userinfo_groups_group_id_1fb5e93a_fk_auth_group_id` (`group_id`),
  CONSTRAINT `blog_userinfo_groups_group_id_1fb5e93a_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `blog_userinfo_groups_userinfo_id_f6f0498b_fk_blog_userinfo_nid` FOREIGN KEY (`userinfo_id`) REFERENCES `blog_userinfo` (`nid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE `blog_userinfo_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `userinfo_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `blog_userinfo_user_permi_userinfo_id_permission_i_7d343093_uniq` (`userinfo_id`,`permission_id`),
  KEY `blog_userinfo_user_p_permission_id_ace80f7e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `blog_userinfo_user_p_permission_id_ace80f7e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `blog_userinfo_user_p_userinfo_id_57e76697_fk_blog_user` FOREIGN KEY (`userinfo_id`) REFERENCES `blog_userinfo` (`nid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_blog_userinfo_nid` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_blog_userinfo_nid` FOREIGN KEY (`user_id`) REFERENCES `blog_userinfo` (`nid`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
BEGIN;
LOCK TABLES `my_blog`.`auth_group` WRITE;
DELETE FROM `my_blog`.`auth_group`;
UNLOCK TABLES;
COMMIT;
BEGIN;
LOCK TABLES `my_blog`.`auth_group_permissions` WRITE;
DELETE FROM `my_blog`.`auth_group_permissions`;
UNLOCK TABLES;
COMMIT;
BEGIN;
LOCK TABLES `my_blog`.`auth_permission` WRITE;
DELETE FROM `my_blog`.`auth_permission`;
INSERT INTO `my_blog`.`auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (1, 'Can add log entry', 1, 'add_logentry'),(2, 'Can change log entry', 1, 'change_logentry'),(3, 'Can delete log entry', 1, 'delete_logentry'),(4, 'Can view log entry', 1, 'view_logentry'),(5, 'Can add permission', 2, 'add_permission'),(6, 'Can change permission', 2, 'change_permission'),(7, 'Can delete permission', 2, 'delete_permission'),(8, 'Can view permission', 2, 'view_permission'),(9, 'Can add group', 3, 'add_group'),(10, 'Can change group', 3, 'change_group'),(11, 'Can delete group', 3, 'delete_group'),(12, 'Can view group', 3, 'view_group'),(13, 'Can add content type', 4, 'add_contenttype'),(14, 'Can change content type', 4, 'change_contenttype'),(15, 'Can delete content type', 4, 'delete_contenttype'),(16, 'Can view content type', 4, 'view_contenttype'),(17, 'Can add session', 5, 'add_session'),(18, 'Can change session', 5, 'change_session'),(19, 'Can delete session', 5, 'delete_session'),(20, 'Can view session', 5, 'view_session'),(21, 'Can add user', 6, 'add_userinfo'),(22, 'Can change user', 6, 'change_userinfo'),(23, 'Can delete user', 6, 'delete_userinfo'),(24, 'Can view user', 6, 'view_userinfo'),(25, 'Can add article', 7, 'add_article'),(26, 'Can change article', 7, 'change_article'),(27, 'Can delete article', 7, 'delete_article'),(28, 'Can view article', 7, 'view_article'),(29, 'Can add blog', 8, 'add_blog'),(30, 'Can change blog', 8, 'change_blog'),(31, 'Can delete blog', 8, 'delete_blog'),(32, 'Can view blog', 8, 'view_blog'),(33, 'Can add tag', 9, 'add_tag'),(34, 'Can change tag', 9, 'change_tag'),(35, 'Can delete tag', 9, 'delete_tag'),(36, 'Can view tag', 9, 'view_tag'),(37, 'Can add comment', 10, 'add_comment'),(38, 'Can change comment', 10, 'change_comment'),(39, 'Can delete comment', 10, 'delete_comment'),(40, 'Can view comment', 10, 'view_comment'),(41, 'Can add category', 11, 'add_category'),(42, 'Can change category', 11, 'change_category'),(43, 'Can delete category', 11, 'delete_category'),(44, 'Can view category', 11, 'view_category'),(45, 'Can add article2 tag', 12, 'add_article2tag'),(46, 'Can change article2 tag', 12, 'change_article2tag'),(47, 'Can delete article2 tag', 12, 'delete_article2tag'),(48, 'Can view article2 tag', 12, 'view_article2tag'),(49, 'Can add article up down', 13, 'add_articleupdown'),(50, 'Can change article up down', 13, 'change_articleupdown'),(51, 'Can delete article up down', 13, 'delete_articleupdown'),(52, 'Can view article up down', 13, 'view_articleupdown');
UNLOCK TABLES;
COMMIT;
BEGIN;
LOCK TABLES `my_blog`.`blog_article2tag` WRITE;
DELETE FROM `my_blog`.`blog_article2tag`;
INSERT INTO `my_blog`.`blog_article2tag` (`nid`,`article_id`,`tag_id`) VALUES (2, 1, 1),(1, 2, 1),(3, 3, 2);
UNLOCK TABLES;
COMMIT;
BEGIN;
LOCK TABLES `my_blog`.`blog_article` WRITE;
DELETE FROM `my_blog`.`blog_article`;
INSERT INTO `my_blog`.`blog_article` (`nid`,`title`,`desc`,`create_time`,`content`,`category`,`user`,`comment_count`,`down_count`,`up_count`) VALUES (1, 'SpringBoot如何实现定时任务', 'SpringBoot创建定时任务的方式很简单，主要有两种方式：一、基于注解的方式（@Scheduled）二、数据库动态配置。实际开发中，第一种需要在代码中写死表达式，如果修改起来，又得重启会显示很麻烦；所以我们往往会采取第二种方式，可以直接从数据库中读取定时任务的指定执行时间，无需重启。 ...', '2021-09-13 11:17:49.972000', 'SpringBoot创建定时任务的方式很简单，主要有两种方式：一、基于注解的方式（@Scheduled）二、数据库动态配置。实际开发中，第一种需要在代码中写死表达式，如果修改起来，又得重启会显示很麻烦；所以我们往往会采取第二种方式，可以直接从数据库中读取定时任务的指定执行时间，无需重启。\r\n\r\n \r\n\r\n下面就来介绍下这两种方式吧\r\n\r\n一、基于注解（@Scheduled）\r\n基于注解是一种静态的方式，只需要几行代码就可以搞定了\r\n\r\n添加一个配置类', 1, 2, 0, 0, 0),(2, 'Redis 起步', '由四个可执行文件：redis-benchmark、redis-cli、redis-server、redis-stat 这四个文件，加上一个redis.conf就构成了整...conf就构成了整个redis的最终可用包。它们的作用如下： redis-server：Redis服务器的daemon启动程序 redis-cli：Redis命令行操作工具。当', '2021-10-13 11:18:54.914399', 'Redis是一个key-value存储系统。和Memcached类似，但是解决了断电后数据完全丢失的情况，而且她支持更多无化的value类型，除了和string外，还支持lists（链表）、sets（集合）和zsets（有序集合）几种数据类型。这些数据类型都支持push/pop、add/remove及取交集并集和差集及更丰富的操作，而且这些操作都是原子性的。\r\n\r\n2.Redis的性能\r\n下面是官方的bench-mark数据：\r\n\r\nThe test was done with 50 simultaneous clients performing 100000 requests.\r\nThe value SET and GET is a 256 bytes string.\r\nThe Linux box is running Linux 2.6, it’s Xeon X3320 2.5Ghz.\r\nText executed using the loopback interface (127.0.0.1).\r\nResults: about 110000 SETs per second, about 81000 GETs per second.\r\n\r\n更多详细数据请见官方bench-mark page（http://code.google.com/p/redis/wiki/Benchmarks）', 2, 2, 0, 0, 0),(3, 'MySQL函数', 'GET_LOCK(\'MySQL\',10) ->1 (持续10秒) SELECT IS_FREE_LOCK(\'MySQL\') ->1 SELECT RELEASE_LOCK(\'MySQL\')... MySQL数据库提供了很多函数包括： 数学函数； 字符串函数； 日期和时间函数； 条件判断函数； 系统信息函数； 加密函数； 格式化函数； 一、数学函数', '2021-10-13 11:20:05.499425', 'MySQL函数\r\n　　MySQL数据库提供了很多函数包括：\r\n\r\n数学函数；\r\n字符串函数；\r\n日期和时间函数；\r\n条件判断函数；\r\n系统信息函数；\r\n加密函数；\r\n格式化函数；\r\n一、数学函数', 3, 2, 0, 0, 0);
UNLOCK TABLES;
COMMIT;
BEGIN;
LOCK TABLES `my_blog`.`blog_articleupdown` WRITE;
DELETE FROM `my_blog`.`blog_articleupdown`;
UNLOCK TABLES;
COMMIT;
BEGIN;
LOCK TABLES `my_blog`.`blog_blog` WRITE;
DELETE FROM `my_blog`.`blog_blog`;
INSERT INTO `my_blog`.`blog_blog` (`nid`,`title`,`site_name`,`theme`) VALUES (1, '测试员的博客', 'cs', '测试'),(2, '小邵的个人博客', 'xiaoshao', '随心');
UNLOCK TABLES;
COMMIT;
BEGIN;
LOCK TABLES `my_blog`.`blog_category` WRITE;
DELETE FROM `my_blog`.`blog_category`;
INSERT INTO `my_blog`.`blog_category` (`nid`,`title`,`blog`) VALUES (1, 'SpringBoot', 1),(2, '数据库', 1),(3, '数据库x', 1);
UNLOCK TABLES;
COMMIT;
BEGIN;
LOCK TABLES `my_blog`.`blog_comment` WRITE;
DELETE FROM `my_blog`.`blog_comment`;
UNLOCK TABLES;
COMMIT;
BEGIN;
LOCK TABLES `my_blog`.`blog_tag` WRITE;
DELETE FROM `my_blog`.`blog_tag`;
INSERT INTO `my_blog`.`blog_tag` (`nid`,`title`,`blog_nid`) VALUES (1, '测试标签', 1),(2, '测试标签2', 1);
UNLOCK TABLES;
COMMIT;
BEGIN;
LOCK TABLES `my_blog`.`blog_userinfo` WRITE;
DELETE FROM `my_blog`.`blog_userinfo`;
INSERT INTO `my_blog`.`blog_userinfo` (`password`,`last_login`,`is_superuser`,`username`,`first_name`,`last_name`,`email`,`is_staff`,`is_active`,`date_joined`,`nid`,`telephone`,`avatar`,`create_time`,`blog_id`) VALUES ('pbkdf2_sha256$260000$0zrVrfYLEWKhTr1MBDHsS2$ACnFAPAJJolfzuxXuR3aUdbKq4DAbRnv4ILl1iD21eM=', '2021-10-14 20:05:39.160344', 1, 'syx', '', '', '1275241305@qq.com', 1, 1, '2021-10-12 12:47:00.000000', 1, '17606927841', 'avatars/lufei.jpg', '2021-10-12 12:47:47.099900', 2),('pbkdf2_sha256$260000$RdWrBHczQpErXUfWsjY3Ue$rUOIUnOpeLuh4DwX7dgfdCGbGHNHq1cDoeLaP9G11mk=', NULL, 0, 'admin', '', '', 'admin@admin.com', 0, 1, '2021-10-13 11:12:00.000000', 2, 'ceshi', 'avatars/default_avatar_svx8J44.png', '2021-10-13 11:12:57.173471', 1);
UNLOCK TABLES;
COMMIT;
BEGIN;
LOCK TABLES `my_blog`.`blog_userinfo_groups` WRITE;
DELETE FROM `my_blog`.`blog_userinfo_groups`;
UNLOCK TABLES;
COMMIT;
BEGIN;
LOCK TABLES `my_blog`.`blog_userinfo_user_permissions` WRITE;
DELETE FROM `my_blog`.`blog_userinfo_user_permissions`;
UNLOCK TABLES;
COMMIT;
BEGIN;
LOCK TABLES `my_blog`.`django_admin_log` WRITE;
DELETE FROM `my_blog`.`django_admin_log`;
INSERT INTO `my_blog`.`django_admin_log` (`id`,`action_time`,`object_id`,`object_repr`,`action_flag`,`change_message`,`content_type_id`,`user_id`) VALUES (1, '2021-10-13 11:14:17.481748', '1', '测试员的博客', 1, '[{\"added\": {}}]', 8, 1),(2, '2021-10-13 11:14:36.718316', '2', 'admin', 2, '[{\"changed\": {\"fields\": [\"Telephone\", \"Blog\"]}}]', 6, 1),(3, '2021-10-13 11:15:52.546435', '2', '小邵的个人博客', 1, '[{\"added\": {}}]', 8, 1),(4, '2021-10-13 11:16:27.614644', '2', 'admin', 2, '[{\"changed\": {\"fields\": [\"Telephone\"]}}]', 6, 1),(5, '2021-10-13 11:16:38.521359', '1', 'syx', 2, '[{\"changed\": {\"fields\": [\"Last login\", \"Telephone\", \"Blog\"]}}]', 6, 1),(6, '2021-10-13 11:17:31.082441', '1', 'SpringBoot', 1, '[{\"added\": {}}]', 11, 1),(7, '2021-10-13 11:17:49.973323', '1', 'SpringBoot如何实现定时任务', 1, '[{\"added\": {}}]', 7, 1),(8, '2021-10-13 11:18:34.511085', '2', '数据库', 1, '[{\"added\": {}}]', 11, 1),(9, '2021-10-13 11:18:54.916394', '2', 'Redis 起步', 1, '[{\"added\": {}}]', 7, 1),(10, '2021-10-13 11:19:36.705034', '3', '数据库', 1, '[{\"added\": {}}]', 11, 1),(11, '2021-10-13 11:20:05.500423', '3', 'MySQL函数', 1, '[{\"added\": {}}]', 7, 1),(12, '2021-10-13 11:20:24.103683', '3', '数据库x', 2, '[{\"changed\": {\"fields\": [\"\\u5206\\u7c7b\\u6807\\u9898\"]}}]', 11, 1),(13, '2021-10-13 11:20:29.985955', '3', 'MySQL函数', 2, '[]', 7, 1),(14, '2021-10-13 11:39:40.975617', '1', 'syx', 2, '[{\"changed\": {\"fields\": [\"Avatar\"]}}]', 6, 1),(15, '2021-10-13 13:53:02.306269', '2', 'admin', 2, '[{\"changed\": {\"fields\": [\"Avatar\"]}}]', 6, 1),(16, '2021-10-13 15:01:08.543546', '1', '测试标签', 1, '[{\"added\": {}}]', 9, 1),(17, '2021-10-13 15:01:35.947246', '3', 'MySQL函数', 2, '[]', 7, 1),(18, '2021-10-13 15:02:05.642813', '1', 'Redis 起步---测试标签', 1, '[{\"added\": {}}]', 12, 1),(19, '2021-10-13 15:02:17.713526', '2', 'SpringBoot如何实现定时任务---测试标签', 1, '[{\"added\": {}}]', 12, 1),(20, '2021-10-13 15:02:18.708864', '2', 'SpringBoot如何实现定时任务---测试标签', 2, '[]', 12, 1),(21, '2021-10-13 15:04:44.640642', '2', '测试标签2', 1, '[{\"added\": {}}]', 9, 1),(22, '2021-10-14 22:23:15.597007', '3', 'MySQL函数', 2, '[{\"changed\": {\"fields\": [\"\\u4f5c\\u8005\"]}}]', 7, 1),(23, '2021-10-14 22:23:30.016438', '2', '测试标签2', 2, '[]', 9, 1),(24, '2021-10-14 22:23:46.869359', '3', 'MySQL函数', 2, '[]', 7, 1),(25, '2021-10-14 22:24:23.249049', '3', 'MySQL函数---测试标签2', 1, '[{\"added\": {}}]', 12, 1),(26, '2021-10-14 22:34:40.858037', '3', '数据库x', 2, '[{\"changed\": {\"fields\": [\"\\u6240\\u5c5e\\u535a\\u5ba2\"]}}]', 11, 1);
UNLOCK TABLES;
COMMIT;
BEGIN;
LOCK TABLES `my_blog`.`django_content_type` WRITE;
DELETE FROM `my_blog`.`django_content_type`;
INSERT INTO `my_blog`.`django_content_type` (`id`,`app_label`,`model`) VALUES (1, 'admin', 'logentry'),(3, 'auth', 'group'),(2, 'auth', 'permission'),(7, 'blog', 'article'),(12, 'blog', 'article2tag'),(13, 'blog', 'articleupdown'),(8, 'blog', 'blog'),(11, 'blog', 'category'),(10, 'blog', 'comment'),(9, 'blog', 'tag'),(6, 'blog', 'userinfo'),(4, 'contenttypes', 'contenttype'),(5, 'sessions', 'session');
UNLOCK TABLES;
COMMIT;
BEGIN;
LOCK TABLES `my_blog`.`django_migrations` WRITE;
DELETE FROM `my_blog`.`django_migrations`;
INSERT INTO `my_blog`.`django_migrations` (`id`,`app`,`name`,`applied`) VALUES (1, 'contenttypes', '0001_initial', '2021-10-12 12:21:40.743497'),(2, 'contenttypes', '0002_remove_content_type_name', '2021-10-12 12:21:40.856195'),(3, 'auth', '0001_initial', '2021-10-12 12:21:41.214237'),(4, 'auth', '0002_alter_permission_name_max_length', '2021-10-12 12:21:41.275075'),(5, 'auth', '0003_alter_user_email_max_length', '2021-10-12 12:21:41.281059'),(6, 'auth', '0004_alter_user_username_opts', '2021-10-12 12:21:41.288040'),(7, 'auth', '0005_alter_user_last_login_null', '2021-10-12 12:21:41.294024'),(8, 'auth', '0006_require_contenttypes_0002', '2021-10-12 12:21:41.298014'),(9, 'auth', '0007_alter_validators_add_error_messages', '2021-10-12 12:21:41.303997'),(10, 'auth', '0008_alter_user_username_max_length', '2021-10-12 12:21:41.310979'),(11, 'auth', '0009_alter_user_last_name_max_length', '2021-10-12 12:21:41.317961'),(12, 'auth', '0010_alter_group_name_max_length', '2021-10-12 12:21:41.332920'),(13, 'auth', '0011_update_proxy_permissions', '2021-10-12 12:21:41.339902'),(14, 'auth', '0012_alter_user_first_name_max_length', '2021-10-12 12:21:41.345885'),(15, 'blog', '0001_initial', '2021-10-12 12:21:43.513091'),(16, 'admin', '0001_initial', '2021-10-12 12:21:43.674659'),(17, 'admin', '0002_logentry_remove_auto_add', '2021-10-12 12:21:43.684632'),(18, 'admin', '0003_logentry_add_action_flag_choices', '2021-10-12 12:21:43.695603'),(19, 'sessions', '0001_initial', '2021-10-12 12:21:43.735496'),(20, 'blog', '0002_auto_20211013_2144', '2021-10-13 13:45:02.684080');
UNLOCK TABLES;
COMMIT;
BEGIN;
LOCK TABLES `my_blog`.`django_session` WRITE;
DELETE FROM `my_blog`.`django_session`;
INSERT INTO `my_blog`.`django_session` (`session_key`,`session_data`,`expire_date`) VALUES ('4rsss6l6sine9vhb0yw3386yo86s8v33', 'eyJ2YWxpZF9jb2RlX3N0ciI6IkZhY21PIn0:1maH1z:gYcqzGsiRzEGUMBNDC7jN4NVYc0ltN9ebA4jMJWsAXM', '2021-10-26 12:37:19.868627'),('66wzde80af2gwm83c7c8i5y30up6vxin', '.eJxVjDsOgzAQBe_iOrJYcMBOSY9yBGvt3Q0_gYQhRaLcPSDR0M7Me1_1xrEjH2din9ZFPVRfPz-DuimP29r6LfHiO9o5XFnAOPB0COpxes06ztO6dEEfiT5t0s1-PNZnezloMbX7OlTM1kCFxiA6W0DpDICLsbTBEZcVSc4uBsmt2HtBnFFmXAAxIuBA1O8PG2ZA4A:1mazUR:wl_kJxKKqP7t5ksIA7yKR4nYsBRZFTvNXFb6b33rHAs', '2021-10-28 20:05:39.164334'),('c3835u1swjurwich28hxgcs4ciuvr9o9', '.eJxVjMsOgjAQRf-la9MwUKF1aWJiYvyGZtqZEZRHQsGFxn8XEjZszzn3ftUb24Z8HIh9mkZ1UpfP7dqpg_I4T7WfE4--oYXDngWML-5XQU_sH4OOQz-NTdBrojeb9H05bs9buzuoMdXLOlTM1kCFxiA6W0DpDICLsbTBEZcVSc4uBsmt2GNBnFFmXAAxIuBA1O8PBPNAvw:1maHNW:iLYYzSXDy-IcTlyCGOTP29OXZmrKqOHLb3hdCeKktr8', '2021-10-26 12:59:34.273774'),('dd8p1wjjvarfc1e0ywqbyna25abvjog1', '.eJxVjDEOgzAQBP_iOrI4MGCnpEqTIi-wzr67QIKwhCFNlL8HJBramdn9qg-OA_mYiH1eZnVV9eNmO3VRHtel92vm2Q-0cTizgPHN0y7ohdMz6ZimZR6C3hN92Kzv2_HYHe3poMfcb-vQMlsDLRqD6GwFjTMALsbGBkfctCQluxiktGLririgwrgAYkTAgajfH7OoQEg:1mae5N:-y7KtkvRx4fHyeW8AARjWMXCkm1ZKPBkeUZIY6ISra0', '2021-10-27 13:14:21.424196'),('g0wwdd5dd8e1svzs1qbmzv21d0be0uxn', 'eyJ2YWxpZF9jb2RlX3N0ciI6InN3NUVUIn0:1maH1q:o7rwwjKNL2d8Ad51uIjyZrK1EJWRhBZVWsg0AxpQoVg', '2021-10-26 12:37:10.172853'),('lb1shoia6elbmj6yao96fam5t22md734', '.eJxVjEEOgjAQRe_StWkYKLR1adwaj9BMOzOCEkgosDHeXUjYsH3v_f9VK_YdhTQShzxP6qrsWt-f6qICLnMblsxT6GjjcGYR04eHXdAbh9eo0zjMUxf1nujDZv3Yjvvb0Z4OWsztto6W2RmwaAyidxU03gD4lBoXPXFjSUr2KUrpxNUVcUGF8RHEiIAHUb8_0m5AdQ:1macBt:L6yBoro6mQT2VuDrE6h2lk-gTCfzQj6eYG1J3a9jeeo', '2021-10-27 11:12:57.214363'),('lrsgkhvk1en24oit2lur0bl7g5iguvji', '.eJxVjDEOgzAMRe-SuYowuBB37N6pB4ic2Cm0CCQCLFXvXpBYWN97_3_Nyn0nPo6iPs-TuZnKPVc0F-N5mVu_ZJ18JxuHMwscPzrsQt48vEYbx2GeumD3xB4228d23N-P9nTQcm63dWhUHULDiMzkKqgJASjG2gUSrRtJpVIMqXTJXSvRQgqkAAlTAoJkfn_JSUBo:1mb0Tl:QMa_RMrV3RZPL85gTJz3xv3a7iEGuBQWFZDMPL8xVsY', '2021-10-28 21:09:01.752706'),('ppkp6ou32vxbmfpjttbmziwi4dv1rqzy', 'eyJ2YWxpZF9jb2RlX3N0ciI6ImswcThrIn0:1maS9i:Fnz7gobGhXe6NktDhVmhsLx6Kwrer0AJzULdSl4xlr8', '2021-10-27 00:30:02.638894'),('rru5lfq30de3cdkqr527nt92cw5a6ua3', '.eJxVjDEPgjAQRv9LZ9NwWKHn6Ghi3F2aa-9OUAIJBRfjfxcSFtb33vd9zYe6lkMaWEKeRnM2xXV-3M3BBJqnJsxZxtDywmHPIqW39KvgF_XPwaahn8Y22jWxm832thx3l63dHTSUm2UdaxHvoCbniNAfoUIHgClVPiJLVbOWgilq6dWfjiwFFw4jqFMFBDW_P-oLQJg:1maJ9S:sjeht179952rTgGvnFJutXQBBqNHEJwursRq9aUb8gY', '2021-10-26 14:53:10.930203');
UNLOCK TABLES;
COMMIT;
