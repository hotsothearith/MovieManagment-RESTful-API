-- MySQL dump 10.13  Distrib 8.0.40, for Win64 (x86_64)
--
-- Host: localhost    Database: moviemanagementdb
-- ------------------------------------------------------
-- Server version	8.0.40

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `cast`
--

DROP TABLE IF EXISTS `cast`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cast` (
  `cast_id` int NOT NULL,
  `cast_full_name` varchar(50) DEFAULT NULL,
  `cast_first_name` varchar(50) DEFAULT NULL,
  `cast_last_name` varchar(50) DEFAULT NULL,
  `cast_gender` varchar(2) DEFAULT NULL,
  PRIMARY KEY (`cast_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cast`
--

LOCK TABLES `cast` WRITE;
/*!40000 ALTER TABLE `cast` DISABLE KEYS */;
INSERT INTO `cast` VALUES (1,'Bruce Willis','Bruce','Willis','M'),(2,'Alan Rickman','Alan','Rickman','M'),(3,'Tom Hardy','Tom','Hardy','M'),(4,'Charlize Theron','Charlize','Theron','F'),(5,'Keanu Reeves','Keanu','Reeves','M'),(6,'Willem Dafoe','Willem','Dafoe','M'),(7,'Harrison Ford','Harrison','Ford','M'),(8,'Karen Allen','Karen','Allen','F'),(9,'Elijah Wood','Elijah','Wood','M'),(10,'Ian McKellen','Ian','McKellen','M'),(11,'Neel Sethi','Neel','Sethi','M'),(12,'Bill Murray','Bill','Murray','M'),(13,'Tom Hanks','Tom','Hanks','M'),(14,'Tim Allen','Tim','Allen','M'),(15,'Kristen Bell','Kristen','Bell','F'),(16,'Idina Menzel','Idina','Menzel','F'),(17,'Matthew Broderick','Matthew','Broderick','M'),(18,'James Earl Jones','James','Earl Jones','M'),(19,'Bradley Cooper','Bradley','Cooper','M'),(20,'Zach Galifianakis','Zach','Galifianakis','M'),(21,'Jonah Hill','Jonah','Hill','M'),(22,'Michael Cera','Michael','Cera','M'),(23,'Will Ferrell','Will','Ferrell','M'),(24,'John C. Reilly','John','C. Reilly','M'),(25,'Tim Robbins','Tim','Robbins','M'),(26,'Morgan Freeman','Morgan','Freeman','M'),(27,'Tom Hanks','Tom','Hanks','M'),(28,'Robin Wright','Robin','Wright','F'),(29,'Marlon Brando','Marlon','Brando','M'),(30,'Al Pacino','Al','Pacino','M');
/*!40000 ALTER TABLE `cast` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cast_member`
--

DROP TABLE IF EXISTS `cast_member`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cast_member` (
  `movie_id` int NOT NULL,
  `cast_id` int NOT NULL,
  PRIMARY KEY (`movie_id`,`cast_id`),
  KEY `cast_id` (`cast_id`),
  CONSTRAINT `cast_member_ibfk_1` FOREIGN KEY (`movie_id`) REFERENCES `movie` (`movie_id`),
  CONSTRAINT `cast_member_ibfk_2` FOREIGN KEY (`cast_id`) REFERENCES `cast` (`cast_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cast_member`
--

LOCK TABLES `cast_member` WRITE;
/*!40000 ALTER TABLE `cast_member` DISABLE KEYS */;
INSERT INTO `cast_member` VALUES (1,1),(1,2),(2,3),(2,4),(3,5),(3,6),(4,7),(4,8),(5,9),(5,10),(6,11),(6,12),(7,13),(7,14),(8,15),(8,16),(9,17),(9,18),(10,19),(10,20),(11,21),(11,22),(12,23),(12,24),(13,25),(13,26),(14,27),(14,28),(15,29),(15,30);
/*!40000 ALTER TABLE `cast_member` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `director`
--

DROP TABLE IF EXISTS `director`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `director` (
  `director_id` int NOT NULL,
  `director_full_name` varchar(50) DEFAULT NULL,
  `director_first_name` varchar(50) DEFAULT NULL,
  `director_last_name` varchar(50) DEFAULT NULL,
  `director_gender` varchar(2) DEFAULT NULL,
  PRIMARY KEY (`director_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `director`
--

LOCK TABLES `director` WRITE;
/*!40000 ALTER TABLE `director` DISABLE KEYS */;
INSERT INTO `director` VALUES (1,'John McTiernan','John','McTiernan','M'),(2,'George Miller','George','Miller','M'),(3,'Chad Stahelski','Chad','Stahelski','M'),(4,'Steven Spielberg','Steven','Spielberg','M'),(5,'Peter Jackson','Peter','Jackson','M'),(6,'Jon Favreau','Jon','Favreau','M'),(7,'John Lasseter','John','Lasseter','M'),(8,'Chris Buck','Chris','Buck','M'),(9,'Roger Allers','Roger','Allers','M'),(10,'Todd Phillips','Todd','Phillips','M'),(11,'Greg Mottola','Greg','Mottola','M'),(12,'Adam McKay','Adam','McKay','M'),(13,'Frank Darabont','Frank','Darabont','M'),(14,'Robert Zemeckis','Robert','Zemeckis','M'),(15,'Francis Ford Coppola','Francis','Ford Coppola','M');
/*!40000 ALTER TABLE `director` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `genre`
--

DROP TABLE IF EXISTS `genre`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `genre` (
  `genre_id` int NOT NULL,
  `genre_description` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`genre_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `genre`
--

LOCK TABLES `genre` WRITE;
/*!40000 ALTER TABLE `genre` DISABLE KEYS */;
INSERT INTO `genre` VALUES (1,'Action'),(2,'Adventure'),(3,'Animation'),(4,'Comedy'),(5,'Crime'),(6,'Documentary'),(7,'Drama'),(8,'Fantasy'),(9,'Historical'),(10,'Horror'),(11,'Musical'),(12,'Mystery'),(13,'Romance'),(14,'Science Fiction'),(15,'Sports'),(16,'Thriller'),(17,'War'),(18,'Western');
/*!40000 ALTER TABLE `genre` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `movie`
--

DROP TABLE IF EXISTS `movie`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `movie` (
  `movie_id` int NOT NULL,
  `movie_title` varchar(150) DEFAULT NULL,
  `movie_description` varchar(250) DEFAULT NULL,
  `movie_release_date` date DEFAULT NULL,
  `movie_duration` int DEFAULT NULL,
  `director_id` int DEFAULT NULL,
  PRIMARY KEY (`movie_id`),
  KEY `director_id` (`director_id`),
  CONSTRAINT `movie_ibfk_1` FOREIGN KEY (`director_id`) REFERENCES `director` (`director_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movie`
--

LOCK TABLES `movie` WRITE;
/*!40000 ALTER TABLE `movie` DISABLE KEYS */;
INSERT INTO `movie` VALUES (1,'Die Hard','An action-packed thriller set during Christmas.','1988-07-20',132,1),(2,'Mad Max: Fury Road','A high-octane chase in a post-apocalyptic world.','2015-05-15',120,2),(3,'John Wick','A retired hitman seeks revenge.','2014-10-24',101,3),(4,'Indiana Jones: Raiders of the Lost Ark','An adventurous quest for the Ark of the Covenant.','1981-06-12',115,4),(5,'The Lord of the Rings: The Fellowship of the Ring','A journey to destroy the One Ring.','2001-12-19',178,5),(6,'The Jungle Book','A boy raised by wolves embarks on an adventure.','2016-04-15',106,6),(7,'Toy Story','A cowboy doll feels threatened by a new action figure.','1995-11-22',81,7),(8,'Frozen','A magical journey to end an eternal winter.','2013-11-27',102,8),(9,'The Lion King','A young lion prince flees his kingdom after his father’s death.','1994-06-24',88,9),(10,'The Hangover','A bachelor party goes terribly wrong.','2009-06-05',100,10),(11,'Superbad','Two high school friends attempt to buy alcohol for a party.','2007-08-17',113,11),(12,'Step Brothers','Two grown men become stepbrothers and compete for dominance.','2008-07-25',106,12),(13,'The Shawshank Redemption','Two imprisoned men bond over a number of years.','1994-09-23',142,13),(14,'Forrest Gump','The story of a man with a unique perspective on life.','1994-07-06',144,14),(15,'The Godfather','The aging patriarch of a crime dynasty transfers control to his son.','1972-03-24',175,15);
/*!40000 ALTER TABLE `movie` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `movie_genre`
--

DROP TABLE IF EXISTS `movie_genre`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `movie_genre` (
  `movie_id` int NOT NULL,
  `genre_id` int NOT NULL,
  PRIMARY KEY (`movie_id`,`genre_id`),
  KEY `genre_id` (`genre_id`),
  CONSTRAINT `movie_genre_ibfk_1` FOREIGN KEY (`movie_id`) REFERENCES `movie` (`movie_id`),
  CONSTRAINT `movie_genre_ibfk_2` FOREIGN KEY (`genre_id`) REFERENCES `genre` (`genre_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movie_genre`
--

LOCK TABLES `movie_genre` WRITE;
/*!40000 ALTER TABLE `movie_genre` DISABLE KEYS */;
INSERT INTO `movie_genre` VALUES (1,1),(2,1),(3,1),(4,2),(5,2),(6,2),(7,3),(8,3),(9,3),(10,4),(11,4),(12,4),(13,7),(14,7),(15,7);
/*!40000 ALTER TABLE `movie_genre` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-01-07  0:07:44
