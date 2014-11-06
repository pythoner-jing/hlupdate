-- MySQL dump 10.14  Distrib 5.5.33-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: hlupdate
-- ------------------------------------------------------
-- Server version	5.5.33-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Context`
--

DROP TABLE IF EXISTS `Context`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Context` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fetchtime` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=55 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Context`
--

/*!40000 ALTER TABLE `Context` DISABLE KEYS */;
INSERT INTO `Context` VALUES (54,'2014-11-06 11:04:58');
/*!40000 ALTER TABLE `Context` ENABLE KEYS */;

--
-- Table structure for table `List`
--

DROP TABLE IF EXISTS `List`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `List` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(200) NOT NULL,
  `updatedate` varchar(10) NOT NULL,
  `orderno` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4107 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `List`
--

/*!40000 ALTER TABLE `List` DISABLE KEYS */;
INSERT INTO `List` VALUES (4035,'日常系的异能战斗第5集更新','11-06',0),(4036,'高达创战者 第二季第5集更新','11-06',0),(4037,'大图书馆的牧羊人第5集更新','11-06',0),(4038,'寄生兽 生命的准则第5集更新','11-06',0),(4039,'向山进发 第二季第17集更新','11-06',0),(4040,'棺姬嘉依卡 第二季第5集更新','11-06',0),(4041,'爱·天地无用第22集更新','11-06',0),(4042,'晨曦公主第5集更新','11-05',1),(4043,'魔神之骨第32集更新','11-05',1),(4044,'TRINITY SEVEN 魔道书7使者/七人魔法使第5集更新','11-05',1),(4045,'夏恋战机第6集更新','11-04',2),(4046,'妖怪手表第42集更新','11-04',2),(4047,'飙速宅男 第二季第5集更新','11-04',2),(4048,'巴哈姆特之怒GENESIS第5集更新','11-04',2),(4049,'我家浴室的现况第5集更新','11-04',2),(4050,'银仙第5集更新','11-03',3),(4051,'游戏王ARC-V第30集更新','11-03',3),(4052,'斩·赤红之瞳！第18集更新','11-03',3),(4053,'Girl Friend Beta/临时女友第4集更新','11-03',3),(4054,'灰色的果实第5集更新','11-03',3),(4055,'狼少女与黑王子第5集更新','11-03',3),(4056,'天体的秩序第5集更新','11-03',3),(4057,'绿林女儿罗妮娅/山贼女儿罗妮娅第4集更新','11-02',4),(4058,'七原罪第5集更新','11-02',4),(4059,'龙珠改 魔人布欧篇第30集更新','11-02',4),(4060,'钻石王牌第55集更新','11-02',4),(4061,'境界触发者第4集更新','11-02',4),(4062,'虫师 第二季第13集更新','11-02',4),(4063,'寻找遗失的未来第5集更新','11-02',4),(4064,'海贼王第668集更新','11-02',4),(4065,'丧女/我不受欢迎，怎么想都是你们的错！第13集更新','11-02',4),(4066,'魔弹之王与战姬第5集更新','11-02',4),(4067,'名侦探柯南第768集更新','11-02',4),(4068,'CROSSANGE 天使与龙的轮舞第5集更新','11-02',4),(4069,'美妙旋律 Puripara / 美妙旋律 PriPara第18集更新','11-02',4),(4070,'刀剑神域 第二季第17集更新','11-02',4),(4071,'美少女战士 Crystal第9集更新','11-02',4),(4072,'Fate/stay night 【Unlimited Blade Works】第4集更新','11-02',4),(4073,'记录的地平线 第二季第5集更新','11-01',5),(4074,'魔术快斗1412第5集更新','11-01',5),(4075,'早安恋味糕点店第4集更新','11-01',5),(4076,'选择感染者WIXOSS 第二季第5集更新','11-01',5),(4077,'妖精的尾巴/魔导少年第206集更新','11-01',5),(4078,'Disc Wars复仇者联盟第29集更新','11-01',5),(4079,'白箱第4集更新','11-01',5),(4080,'牙狼GARO -炎之刻印-第5集更新','11-01',5),(4081,'火星异种 阿聂克斯1号篇第6集更新','11-01',5),(4082,'笑傲云天/笑对阴天第5集更新','11-01',5),(4083,'结城友奈是勇者第4集更新','10-31',6),(4084,'电器街的漫画店第5集更新','10-31',6),(4085,'我要成为双马尾第4集更新','10-31',6),(4086,'甘城光辉游乐园第5集更新','10-31',6),(4087,'高达G之复国运动第6集更新','10-31',6),(4088,'PSYCHO-PASS 第二季第4集更新','10-31',6),(4089,'四月是你的谎言第4集更新','10-31',6),(4090,'宠物小精灵XY/神奇宝贝XY第49集更新','10-31',6),(4091,'白银的意志 安格弗伦第17集更新','10-31',6),(4092,'关于完全听不懂老公在说什么的事第5集更新','10-31',6),(4093,'火影忍者第604集更新','10-30',7),(4094,'未来卡搭档对战第36集更新','10-30',7),(4095,'漫画家与助手第12集更新','10-28',8),(4096,'生存游戏社第12集更新','10-27',9),(4097,'世界征服～谋略之星～第12集更新','10-20',10),(4098,'玉子市场第12集更新','10-12',11),(4099,'精灵使的剑舞第12集更新','10-11',12),(4100,'游戏人生/No Game No Life第12集更新','10-09',13),(4101,'青春之旅第12集更新','10-04',14),(4102,'伪恋第20集更新','10-02',15),(4103,'Buddy Complex第13集更新','10-02',15),(4104,'热血人面犬OVA第3集更新','10-01',16),(4105,'魔法少女大战第26集更新','10-01',16),(4106,'人生第13集更新','09-30',17);
/*!40000 ALTER TABLE `List` ENABLE KEYS */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2014-11-06 19:08:37
