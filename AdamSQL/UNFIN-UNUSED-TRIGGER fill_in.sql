CREATE TRIGGER `fill_in_on_update` BEFORE UPDATE
  ON tbl_borrower b
  FOR EACH ROW
BEGIN
	IF NEW.b.name = ''
    THEN
		SET b.name = OLD.b.name;
    END IF;
    IF NEW.address = ''
    THEN
		SET address = OLD.address;
    END IF;
    IF NEW.phone = ''
    THEN
		SET phone = OLD.phone;
    END IF;
END