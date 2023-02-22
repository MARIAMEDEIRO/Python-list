-- --------------------------------------------------------
-- Servidor:                     127.0.0.1
-- Versão do servidor:           10.8.4-MariaDB - mariadb.org binary distribution
-- OS do Servidor:               Win64
-- HeidiSQL Versão:              11.3.0.6295
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Copiando estrutura do banco de dados para prova03
CREATE DATABASE IF NOT EXISTS `prova03` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;
USE `prova03`;

-- Copiando estrutura para tabela prova03.funcao
CREATE TABLE IF NOT EXISTS `funcao` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cod` varchar(5) NOT NULL,
  `nome` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Exportação de dados foi desmarcado.

-- Copiando estrutura para tabela prova03.funcionario
CREATE TABLE IF NOT EXISTS `funcionario` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cpf` varchar(11) NOT NULL DEFAULT '',
  `nome` varchar(50) NOT NULL,
  `funcao` int(11) NOT NULL DEFAULT 0,
  `salario` float NOT NULL DEFAULT 0,
  `telefone` varchar(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `FK_funcionario_funcao` (`funcao`) USING BTREE,
  CONSTRAINT `FK_funcionario_funcao` FOREIGN KEY (`funcao`) REFERENCES `funcao` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

-- Exportação de dados foi desmarcado.

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
