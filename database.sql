CREATE DATABASE IF NOT EXISTS `prova03`;
USE `prova03`;

CREATE TABLE IF NOT EXISTS `funcao` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cod` varchar(5) NOT NULL,
  `nome` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

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
