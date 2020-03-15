DELIMITER $$
CREATE TRIGGER `valid_author_name` BEFORE INSERT
  ON tbl_publisher
     FOR EACH ROW
     BEGIN
      IF NEW.authorName LIKE '%0%' OR '%1%'
						OR '%2%' OR '%3%'
                        OR '%4%' OR '%5%'
                        OR '%6%' OR '%7%'
                        OR '%8%' OR '%9%'
      THEN
          SIGNAL SQLSTATE '45000'
             SET MESSAGE_TEXT= 'Cannot add invalid author name.';
      END IF;
  END;
$$