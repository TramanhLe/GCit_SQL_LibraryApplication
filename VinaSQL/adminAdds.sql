DELIMITER //
CREATE PROCEDURE `A_addAuthor`(IN authorNameInput varchar(45))
	BEGIN
		INSERT INTO tbl_author ( authorName )
        VALUES (authorNameInput);
END; 
-- Adam's original trigger
CREATE TRIGGER `valid_author_name` 
	BEFORE INSERT ON tbl_book_authors FOR EACH ROW
     BEGIN
      IF NEW.authorName LIKE '%0%' OR '%1%'
					OR '%2%' OR '%3%'
					OR '%4%' OR '%5%'
					OR '%6%' OR '%7%'
					OR '%8%' OR '%9%'
      THEN
          SIGNAL SQLSTATE '45000'
             SET MESSAGE_TEXT= 'Invalid author name.';
      END IF;
  END;
  
CREATE PROCEDURE `A_addBook`(IN bookTitleInput varchar(45)
                            IN pubIdInput int)
	BEGIN
		INSERT INTO tbl_book ( bookTitle, pubId )
        VALUES (bookTitleInput, pubIdInput);
END; 

CREATE PROCEDURE `A_addPublisher`(IN publisherNameInput varchar(45),
                            IN publisherAddressInput varchar(45),
                            IN publisherPhoneInput varchar(45))
	BEGIN
		INSERT INTO tbl_publisher ( publisherName, publisherAddress, publisherPhone )
        VALUES (publisherNameInput, publisherAddressInput, publisherPhoneInput);
END; 

CREATE PROCEDURE `A_addBorrower`(IN nameInput varchar(45),
								IN addressInput varchar(45),
								IN phoneInput varchar(45))
BEGIN
	INSERT INTO tbl_borrower ( name, address, phone )
        VALUES (nameInput, addressInput, phoneInput);
END;
CREATE TRIGGER `valid_borrower_name` 
	BEFORE INSERT ON tbl_borrower FOR EACH ROW
     BEGIN
      IF NEW.authorName LIKE '%0%' OR '%1%'
					OR '%2%' OR '%3%'
					OR '%4%' OR '%5%'
					OR '%6%' OR '%7%'
					OR '%8%' OR '%9%'
      THEN
          SIGNAL SQLSTATE '45000'
             SET MESSAGE_TEXT= 'Invalid borrower name.';
      END IF;
  END;
-- addBranch procedure  
  CREATE PROCEDURE `A_addBranch`(IN branchNameInput varchar(45),
								IN branchAddressInput varchar(45))
BEGIN
	INSERT INTO tbl_library_branch ( branchName, branchAddress)
        VALUES (branchNameInput, branchAddressInput);
END;
CREATE TRIGGER `valid_branch_name` 
	BEFORE INSERT ON tbl_library_branch FOR EACH ROW
     BEGIN
      IF NEW.branchName LIKE '0%' LIKE OR '1%'
					LIKE OR '2%' LIKE OR '3%'
					LIKE OR '4%' LIKE OR '5%'
					LIKE OR '6%' LIKE OR '7%'
					LIKE OR '8%' LIKE OR '9%'
      THEN
          SIGNAL SQLSTATE '45000'
             SET MESSAGE_TEXT= 'Invalid library branch name.';
      END IF;
  END;
 //
