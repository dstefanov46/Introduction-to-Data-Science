DROP SCHEMA IF EXISTS covid;
CREATE SCHEMA covid;
USE covid;

--
-- Table structure for table `country`
--

CREATE TABLE country (
  id SMALLINT NOT NULL,
  name VARCHAR(45) NOT NULL,
  PRIMARY KEY  (id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Table structure for table `cases`
--

CREATE TABLE cases (
  country_id SMALLINT NOT NULL,
  date DATE NOT NULL,
  region VARCHAR(45) NOT NULL,
  new_cases SMALLINT NOT NULL,
  PRIMARY KEY  (country_id, date, region),
  CONSTRAINT `fk_case_country` FOREIGN KEY (country_id) REFERENCES country (id) ON DELETE RESTRICT ON UPDATE CASCADE
)ENGINE=InnoDB DEFAULT CHARSET=utf8;