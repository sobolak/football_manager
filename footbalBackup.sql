drop database football;

create database football;

use football;

DROP TABLE IF EXISTS `football`.`clubs` ;
DROP TABLE IF EXISTS `football`.`trainers` ;
DROP TABLE IF EXISTS `football`.`nations` ;
DROP TABLE IF EXISTS `football`.`players` ;
DROP TABLE IF EXISTS `football`.`contracts` ;
DROP TABLE IF EXISTS `football`.`trophies` ;
/*---------------------------TRIGGERS------------------------------------------------------------------------------*/
CREATE TABLE IF NOT EXISTS `football`.`clubs` (
  `cid` INT  PRIMARY KEY auto_increment,
  `name` VARCHAR(45) NULL,
  `number_trophies` INT NULL,
  `foudation` INT NULL,
  `avg_age` FLOAT NULL,
  `photo` VARCHAR(200) NULL,
  `money` FLOAT NULL,
  `league` VARCHAR(45) NULL)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `football`.`trainers` (
  `tid` INT  PRIMARY KEY auto_increment,
  `cid` INT NULL,
  `name` VARCHAR(45) NULL,
  `surname` VARCHAR(45) NULL,
  `nid` INT NULL,
  `age` INT NULL,
  `max_va1ue` FLOAT NULL,
  `min_va1ue` FLOAT NULL,
  `max_salary` FLOAT NULL,
  `min_salary` FLOAT NULL,
  `photo` VARCHAR(200) NULL,
  FOREIGN KEY (`cid`) REFERENCES `football`.`clubs` (`cid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `football`.`nations` (
  `nid` INT PRIMARY KEY auto_increment,
  `name` VARCHAR(45) NULL,
  `number_trophies` INT NULL,
  `ranking` INT NULL,
  `photo` VARCHAR(200) NULL)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `football`.`players` (
  `pid` INT PRIMARY KEY auto_increment,
  `nid` INT NOT NULL,
  `cid` INT NULL,
  `name` VARCHAR(45) NULL,
  `surname` VARCHAR(45) NULL,
  `position` VARCHAR(45) NOT NULL,
  `age` INT NULL,
  `heigth` FLOAT NULL,
  `foot` VARCHAR(10) NULL,
  `max_va1ue` FLOAT NULL,
  `min_va1ue` FLOAT NULL,
  `max_salary` FLOAT NULL,
  `min_salary` FLOAT NULL,
  `avg_rate` FLOAT NULL,
  `goals` INT NULL,
  `assists` INT NULL,
  `matches` INT NULL,
  `photo` VARCHAR(200) NULL,
  FOREIGN KEY (`cid`) REFERENCES `football`.`clubs` (`cid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  FOREIGN KEY (`nid`) REFERENCES `football`.`nations` (`nid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
    )
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `football`.`trophies` (
  `qid` INT PRIMARY KEY auto_increment,
  `cid` INT NULL,
  `nid` INT NULL,
  `name` VARCHAR(45) NULL,
  `year` VARCHAR(10) NULL,
  FOREIGN KEY (`nid`) REFERENCES `football`.`nations` (`nid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  FOREIGN KEY (`cid`) REFERENCES `football`.`clubs` (`cid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `football`.`contracts` (
  `mid` INT PRIMARY KEY auto_increment,
  `pid` INT NULL,
  `tid` INT NULL,
  `cid` INT NULL,
  `salary` FLOAT NULL,
  `va1ue` INT NULL,
  FOREIGN KEY (`pid`) REFERENCES `football`.`players` (`pid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  FOREIGN KEY (`tid`) REFERENCES `football`.`trainers` (`tid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  FOREIGN KEY (`cid`) REFERENCES `football`.`clubs` (`cid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;
/*---------------------------VIEWS------------------------------------------------------------------------------*/
CREATE VIEW view_PlayersToBuy AS SELECT p.pid AS id, p.name, p.surname, p.max_va1ue AS value , p.max_salary AS salary, c.name AS club, n.name AS nation ,p.position,p.age, p.heigth, p.foot, p.avg_rate, p.goals, p.matches,p.assists, c.cid FROM players p, nations n, clubs c WHERE c.cid = p.cid  AND p.nid = n.nid;
CREATE VIEW view_FreePlayers AS SELECT p.pid AS id, p.name, p.surname, p.max_va1ue AS value, p.max_salary AS salary, n.name AS nation ,p.position,p.age, p.heigth, p.foot, p.avg_rate, p.goals,p.matches, p.assists FROM players p, nations n WHERE  p.nid = n.nid AND p.cid IS NULL;

CREATE VIEW view_TrainersToBuy AS  SELECT t.tid AS id, t.name, t.surname, n.name AS nation ,c.name AS club, t.age, t.max_va1ue AS value, t.max_salary AS salary,c.cid FROM trainers t, nations n , clubs c WHERE t.nid=n.nid AND t.cid=c.cid;
CREATE VIEW view_FreeTrainers AS SELECT t.tid AS id, t.name, t.surname, n.name AS nation , t.age, t.max_va1ue AS value, t.max_salary AS salary FROM trainers t, nations n WHERE t.nid=n.nid AND t.cid IS NULL;

CREATE VIEW view_player_info AS SELECT p.pid AS id, p.name, p.surname, p.max_va1ue AS value , p.max_salary AS salary, c.name AS club, n.name AS nation ,p.position,p.age, p.heigth, p.foot, p.avg_rate, p.goals,p.matches, p.assists, c.cid, p.photo, p.pid FROM players p, nations n, clubs c WHERE c.cid = p.cid  AND p.nid = n.nid;
CREATE VIEW view_free_player_info AS SELECT p.pid AS id, p.name, p.surname, p.max_va1ue AS value, p.max_salary AS salary, n.name AS nation ,p.position,p.age, p.heigth, p.foot, p.avg_rate, p.goals,p.matches, p.assists, p.photo,p.pid FROM players p, nations n WHERE  p.nid = n.nid AND p.cid IS NULL;

CREATE VIEW view_trainer_info AS  SELECT t.tid AS id, t.name, t.surname, n.name AS nation ,c.name AS club, t.age, t.max_va1ue AS value, t.max_salary AS salary,c.cid, t.photo,t.tid FROM trainers t, nations n , clubs c WHERE t.nid=n.nid AND t.cid=c.cid;
CREATE VIEW view_free_trainer_info AS  SELECT t.tid AS id, t.name, t.surname, n.name AS nation , t.age, t.max_va1ue AS value, t.max_salary AS salary, t.photo,t.tid FROM trainers t, nations n WHERE t.nid=n.nid AND t.cid IS NULL;

CREATE VIEW view_club_info AS SELECT c.cid AS id, c.name AS club, c.number_trophies, c.foudation, c.avg_age, c.money,c.league, t.name, t.surname , c.photo,c.cid FROM clubs c LEFT JOIN  trainers t USING(cid);
CREATE VIEW view_clubs_trophies_list AS SELECT q.qid AS id, q.name AS trophy , q.year , c.name AS club,c.cid FROM trophies q, clubs c WHERE q.cid=c.cid; 
CREATE VIEW view_nations_trophies_list AS SELECT q.qid AS id, q.name AS trophy, q.year , n.name AS nation , n.nid FROM  trophies q, nations n WHERE q.nid=n.nid;

CREATE VIEW view_player_contracts_list AS SELECT m.mid AS id, p.name, p.surname , c.name AS club, m.va1ue, m.salary, c.cid FROM contracts m ,players p , clubs c WHERE m.cid = c.cid AND m.pid = p.pid; 
CREATE VIEW view_trainer_contracts_list AS SELECT m.mid AS id, t.name, t.surname , c.name AS club, m.va1ue, m.salary, c.cid FROM contracts m ,trainers t , clubs c WHERE m.cid = c.cid AND m.tid = t.tid; 

/*---------------------------PROCEDURES---------------------------------------------------------------------------*/
DELIMITER //
CREATE PROCEDURE  average_age_count (  chosen_cid INT )BEGIN

	UPDATE clubs SET avg_age = (SELECT AVG(p.age) FROM players p WHERE p.cid = chosen_cid) WHERE cid = chosen_cid;

END; //
DELIMITER ;


DELIMITER //
CREATE PROCEDURE  clubs_trophies (  chosen_cid INT )BEGIN

	UPDATE clubs SET number_trophies = coalesce((SELECT COUNT(*) FROM trophies t WHERE t.cid = chosen_cid),0) WHERE cid = chosen_cid;

END; //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE  nations_trophies (  chosen_nid INT )BEGIN

	UPDATE nations SET number_trophies = coalesce((SELECT COUNT(*) FROM trophies t WHERE t.nid = chosen_nid),0) WHERE nid = chosen_nid;

END; //
DELIMITER ;
/*---------------------------TRIGGERS---------------------------------------------------------------------------*/
DELIMITER $$ 
CREATE TRIGGER fire BEFORE DELETE on contracts FOR EACH ROW BEGIN
	DECLARE returnValue float;
	IF OLD.pid IS NOT NULL THEN	
		SELECT coalesce(0,0) INTO returnValue;
		UPDATE clubs 
			SET money = money + (OLD.salary + returnValue)
			WHERE 
			OLD.cid = cid;

		UPDATE players
			SET cid = NULL
			WHERE OLD.pid = pid;

		CALL average_age_count(OLD.cid);
	ELSEIF OLD.tid IS NOT NULL THEN
		SELECT coalesce(0,0) INTO returnValue;

		UPDATE clubs 
			SET money = money + (OLD.salary + returnValue)
			WHERE 
			OLD.cid = cid;

		UPDATE trainers
			SET cid = NULL
			WHERE OLD.tid = tid;
	END IF;
END $$
DELIMITER;

DELIMITER $$
CREATE TRIGGER  freeTransfer BEFORE INSERT on  contracts FOR EACH ROW BEGIN 
    DECLARE buffor float;
    
    IF NEW.pid IS NOT NULL  AND NEW.va1ue IS NULL  AND NEW.salary IS NOT NULL AND (SELECT cid FROM players WHERE pid = NEW.pid) IS NULL THEN
		IF NEW.salary >= (SELECT min_salary FROM players WHERE pid = NEW.pid) THEN
			SELECT money -  NEW.salary INTO buffor FROM clubs WHERE NEW.cid = cid;
			IF buffor > 0 THEN
				UPDATE clubs 
					SET money = money-NEW.salary
					WHERE 
					NEW.cid = cid;
					
				UPDATE players
					SET cid = NEW.cid
					WHERE NEW.pid = pid
					AND
					NEW.cid = (SELECT cid FROM clubs WHERE NEW.cid = cid);
				CALL average_age_count(NEW.cid);
			ELSE
				SIGNAL SQLSTATE '45000'
				SET MESSAGE_TEXT = 'ZA MALO KASKI';
			END IF;
		ELSE
			SIGNAL SQLSTATE '45000'
			SET MESSAGE_TEXT = 'ZLA OFERTA';
		END IF;
	ELSEIF NEW.tid IS NOT NULL AND NEW.va1ue IS NULL AND NEW.salary IS NOT NULL AND (SELECT cid FROM trainers WHERE tid = NEW.tid) IS NULL AND (SELECT tid FROM trainers WHERE cid = NEW.cid) IS NULL THEN
		IF NEW.salary >= (SELECT min_salary FROM trainers WHERE tid = NEW.tid) THEN
			SELECT money -  NEW.salary INTO buffor FROM clubs WHERE NEW.cid = cid;
			IF buffor > 0 THEN
				UPDATE clubs 
					SET money = money-NEW.salary
					WHERE 
					NEW.cid = cid;
				
				UPDATE trainers
					SET cid = NEW.cid
					WHERE NEW.tid = tid
					AND
					NEW.cid = (SELECT cid FROM clubs WHERE NEW.cid = cid);
			ELSE
				SIGNAL SQLSTATE '45000'
				SET MESSAGE_TEXT = 'ZA MALO KASKI';
			END IF;
		ELSE
			SIGNAL SQLSTATE '45000'
			SET MESSAGE_TEXT = 'ZLA OFERTA';
		END IF;
    ELSE
		SIGNAL SQLSTATE '45000'
		SET MESSAGE_TEXT = 'ZLY INSERT';
    END IF;
END $$
DELIMITER ;

DELIMITER $$
CREATE TRIGGER  transfer BEFORE UPDATE on  contracts FOR EACH ROW BEGIN 
    DECLARE buffor float;
    DECLARE returnValue float; 

    IF NEW.pid IS NOT NULL  AND NEW.va1ue IS NOT NULL AND NEW.salary IS NOT NULL AND (SELECT cid FROM players WHERE pid = NEW.pid) IS NOT NULL THEN
		IF NEW.salary >= (SELECT min_salary FROM players WHERE pid = NEW.pid) AND NEW.va1ue >= (SELECT min_va1ue FROM players WHERE pid = NEW.pid) THEN
			SELECT money -  (NEW.salary + NEW.va1ue)INTO buffor FROM clubs WHERE NEW.cid = cid;
			IF buffor > 0 THEN
				UPDATE clubs 
					SET money = money - (NEW.salary + NEW.va1ue)
					WHERE 
					NEW.cid = cid;
					
				SELECT coalesce(OLD.va1ue,0) INTO returnValue;

				UPDATE clubs 
					SET money = money + (OLD.salary + returnValue)
					WHERE 
					OLD.cid = cid;

				UPDATE players
					SET cid = NEW.cid
					WHERE NEW.pid = pid
					AND
					NEW.cid = (SELECT cid FROM clubs WHERE NEW.cid = cid)
					AND 
					NEW.pid = OLD.pid;
				CALL average_age_count(OLD.cid);
				CALL average_age_count(NEW.cid);
			ELSE
				SIGNAL SQLSTATE '45000'
				SET MESSAGE_TEXT = 'ZA MALO KASKI';
			END IF;
		ELSE
			SIGNAL SQLSTATE '45000'
			SET MESSAGE_TEXT = 'ZLA OFERTA';
		END IF;
	ELSEIF NEW.tid IS NOT NULL AND NEW.va1ue IS NOT NULL AND NEW.salary IS NOT NULL AND (SELECT tid FROM trainers WHERE cid = NEW.cid) IS NULL AND (SELECT cid FROM trainers WHERE tid = NEW.tid) IS NOT NULL THEN
		IF NEW.salary >= (SELECT min_salary FROM trainers WHERE tid = NEW.tid) AND NEW.va1ue >= (SELECT min_va1ue FROM trainers WHERE tid = NEW.tid) THEN
			SELECT money -  NEW.salary INTO buffor FROM clubs WHERE NEW.cid = cid;
			IF buffor > 0 THEN
				UPDATE clubs 
					SET money = money - (NEW.salary + NEW.va1ue)
					WHERE 
					NEW.cid = cid;
				
				SELECT coalesce(OLD.va1ue,0) INTO returnValue;

				UPDATE clubs 
					SET money = money + (OLD.salary + returnValue)
					WHERE 
					OLD.cid = cid;
				
				UPDATE trainers
					SET cid = NEW.cid
					WHERE NEW.tid = tid
					AND
					NEW.cid = (SELECT cid FROM clubs WHERE NEW.cid = cid);
			ELSE
				SIGNAL SQLSTATE '45000'
				SET MESSAGE_TEXT = 'ZA MALO KASKI';
			END IF;
		ELSE
			SIGNAL SQLSTATE '45000'
			SET MESSAGE_TEXT = 'ZLA OFERTA';
		END IF;
    ELSE
		SIGNAL SQLSTATE '45000'
		SET MESSAGE_TEXT = 'ZLY INSERT';
    END IF;
END $$
DELIMITER ;
/*---------------------------DATA TO CHECK---------------------------------------------------------------------*/
/*
KOLEJNOSC INSERTOW
1.ten plik
2.END_GAME_nations.txt
3.END_GAME_clubs.txt
4.END_GAME_trainers.txt
5.END_GAME_players.txt - proponuje zaparzyc herbatke
6.END_GAME_trophies.txt
*/
