DELIMITER $$
CREATE TRIGGER `valid_author_name` BEFORE INSERT
  ON tbl_author
     FOR EACH ROW
     BEGIN
      IF NEW.authorName LIKE '%0%' OR LIKE '%1%'
						OR LIKE '%2%' OR LIKE '%3%'
                        OR LIKE '%4%' OR LIKE '%5%'
                        OR LIKE '%6%' OR LIKE '%7%'
                        OR LIKE '%8%' OR LIKE '%9%'
      THEN
          SIGNAL SQLSTATE '45000'
             SET MESSAGE_TEXT= 'Cannot add invalid author name.';
      END IF;
  END;
$$