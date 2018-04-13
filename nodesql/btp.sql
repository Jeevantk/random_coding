SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


use btp;

CREATE TABLE IF NOT EXISTS `tempurature` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tempValue` real  NOT NULL,
  PRIMARY KEY (`id`)
);