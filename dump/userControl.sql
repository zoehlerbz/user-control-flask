-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: mysql
-- Tempo de geração: 14/08/2023 às 13:28
-- Versão do servidor: 8.0.30
-- Versão do PHP: 8.2.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `userControl`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `user_registration`
--

CREATE TABLE `user_registration` (
  `ID` int NOT NULL,
  `username` varchar(50) NOT NULL,
  `email` varchar(150) NOT NULL,
  `password` varchar(255) NOT NULL,
  `token_auth` varchar(40) NOT NULL,
  `token_creation` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `user_verified` tinyint(1) NOT NULL DEFAULT '0' COMMENT '0 - não verificado\r\n1 - verificado'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `user_registration`
--

INSERT INTO `user_registration` (`ID`, `username`, `email`, `password`, `token_auth`, `token_creation`, `user_verified`) VALUES
(1, 'username', 'email@email.com', 'senha123', 'ad5291f8-393d-11ee-bfe0-0242ac130004', '2023-08-12 18:25:55', 0),
(2, 'HomerJS', 'homer.js@email.com', '123456123', '5ade8be6-394e-11ee-aea8-0242ac130004', '2023-08-12 20:25:18', 0),
(3, 'HomerJSss', 'emailsss@email.com', 'senhasenha', 'f4efb76c-3950-11ee-b924-0242ac130003', '2023-08-12 20:43:56', 0),
(4, 'usernameNaoRepetido', 'emailnaorepetido@email.com', '$2b$12$o/fPlpiKQ7h.B7li8Hwf5efEUYXYi1dfUBXTOpR0amK5ap7X/lWEe', 'a3ff50de-3954-11ee-9a4d-0242ac130004', '2023-08-12 21:10:18', 0);

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `user_registration`
--
ALTER TABLE `user_registration`
  ADD PRIMARY KEY (`ID`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `user_registration`
--
ALTER TABLE `user_registration`
  MODIFY `ID` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
