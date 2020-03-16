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
      IF NEW.authorName LIKE '%0%' OR NEW.authorName LIKE '%1%'
		OR NEW.authorName LIKE '%2%' OR NEW.authorName LIKE '%3%'
		OR NEW.authorName LIKE '%4%' OR NEW.authorName LIKE '%5%'
		OR NEW.authorName LIKE '%6%' OR NEW.authorName LIKE '%7%'
		OR NEW.authorName LIKE '%8%' OR NEW.authorName LIKE '%9%'
      THEN
          SIGNAL SQLSTATE '45000'
             SET MESSAGE_TEXT= 'Invalid author name.';
      END IF;
  END;
  
-- Procedure for Admin to add books to the library  
CREATE PROCEDURE `A_addBook`(IN bookTitleInput varchar(45)
                            IN pubIdInput int)
	-- NOTE: all primary keys are not listed because pass-by-reference of IDs
    -- 		 has already been made by console, not needed to call when adding.
	BEGIN
		-- Since primary keys are AUTO_INCREMENT, there's no assignment.
		INSERT INTO tbl_book ( bookTitle, pubId )
        VALUES (bookTitleInput, pubIdInput);
END; 

-- Procedure for Admin to add publisher to the library 
CREATE PROCEDURE `A_addPublisher`(IN publisherNameInput varchar(45),
								IN publisherAddressInput varchar(45),
								IN publisherPhoneInput varchar(45))
	BEGIN
		-- Since primary keys are AUTO_INCREMENT, there's no assignment.
		INSERT INTO tbl_publisher ( publisherName, publisherAddress, publisherPhone )
        VALUES (publisherNameInput, publisherAddressInput, publisherPhoneInput);
END; 
CREATE TRIGGER `valid_publisher_name` 
	BEFORE INSERT ON tbl_publisher FOR EACH ROW
     BEGIN
      IF NEW.publisherName LIKE '%0%' OR NEW.publisherName LIKE '%1%'
			OR NEW.publisherName LIKE '%2%' OR NEW.publisherName LIKE '%3%'
			OR NEW.publisherName LIKE '%4%' OR NEW.publisherName LIKE '%5%'
			OR NEW.publisherName LIKE '%6%' OR NEW.publisherName LIKE '%7%'
			OR NEW.publisherName LIKE '%8%' OR NEW.publisherName LIKE '%9%'
      THEN
          SIGNAL SQLSTATE '45000'
             SET MESSAGE_TEXT= 'Invalid borrower name.';
      END IF;
  END;

-- Procedure for Admin to add borrower to the library   
CREATE PROCEDURE `A_addBorrower`(IN nameInput varchar(45),
								IN addressInput varchar(45),
								IN phoneInput varchar(45))
	BEGIN
		-- Since primary keys are AUTO_INCREMENT, there's no assignment.
		INSERT INTO tbl_borrower ( name, address, phone )
			VALUES (nameInput, addressInput, phoneInput);
END;
CREATE TRIGGER `valid_borrower_name` 
	BEFORE INSERT ON tbl_borrower FOR EACH ROW
     BEGIN
      IF NEW.authorName LIKE '%0%' OR NEW.authorName LIKE '%1%'
			OR NEW.authorName LIKE '%2%' OR NEW.authorName LIKE '%3%'
			OR NEW.authorName LIKE '%4%' OR NEW.authorName LIKE '%5%'
			OR NEW.authorName LIKE '%6%' OR NEW.authorName LIKE '%7%'
			OR NEW.authorName LIKE '%8%' OR NEW.authorName LIKE '%9%'
      THEN
          SIGNAL SQLSTATE '45000'
             SET MESSAGE_TEXT= 'Invalid borrower name.';
      END IF;
  END;

-- Procedure for Admin to add library_branch to the library  
  CREATE PROCEDURE `A_addBranch`(IN branchNameInput varchar(45),
								IN branchAddressInput varchar(45))
	BEGIN
		-- Since primary keys are AUTO_INCREMENT, there's no assignment.
		INSERT INTO tbl_library_branch ( branchName, branchAddress)
			VALUES (branchNameInput, branchAddressInput);
END;
CREATE TRIGGER `valid_branch_name` 
	BEFORE INSERT ON tbl_library_branch FOR EACH ROW
     BEGIN
      IF NEW.branchName LIKE '0%' OR NEW.branchName LIKE '1%'
		OR NEW.branchName LIKE '2%' OR NEW.branchName LIKE '3%'
		OR NEW.branchName LIKE '4%' OR NEW.branchName LIKE '5%'
		OR NEW.branchName LIKE '6%' OR NEW.branchName LIKE '7%'
		OR NEW.branchName LIKE '8%' OR NEW.branchName LIKE '9%'
      THEN
          SIGNAL SQLSTATE '45000'
             SET MESSAGE_TEXT= 'Invalid library branch name.';
      END IF;
  END;
 //
