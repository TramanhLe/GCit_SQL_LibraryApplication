CREATE TRIGGER addBook
		BEFORE INSERT ON tbl_book FOR EACH ROW
<<<<<<< Updated upstream
	INSERT INTO tbl_book
=======
	INSERT INTO tbl_book -- perhaps I should make a pseudo table?
>>>>>>> Stashed changes
	SET action = 'add',
		bookId = NEW.bookId,
		title = NEW.title,
		pubId = NEW.pubId;
        
CREATE TRIGGER updateBook
<<<<<<< Updated upstream
		BEFORE INSERT ON tbl_book FOR EACH ROW
=======
		BEFORE UPDATE ON tbl_book FOR EACH ROW
>>>>>>> Stashed changes
	INSERT INTO tbl_book
	SET action = 'update',
		bookId = OLD.bookId,
		title = OLD.title,
		pubId = OLD.pubId;
        
CREATE TRIGGER addAuthor
		BEFORE INSERT ON tbl_author FOR EACH ROW
	INSERT INTO tbl_author
	SET action = 'add',
		authorId = NEW.authorId,
		authorName = NEW.authorName;
        
CREATE TRIGGER updateAuthor
<<<<<<< Updated upstream
		AFTER INSERT ON tbl_author FOR EACH ROW
=======
		AFTER UPDATE ON tbl_author FOR EACH ROW
>>>>>>> Stashed changes
	INSERT INTO tbl_author
	SET action = 'update',
		authorId = OLD.authorId,
		authorName = OLD.authorName;
        
CREATE TRIGGER addPublisher
		BEFORE INSERT ON tbl_publisher FOR EACH ROW
	INSERT INTO tbl_publisher
	SET action = 'add',
		publisherId = NEW.publisherId,
		publisherName = NEW.publisherName,
		publisherAddress = NEW.publisherAddress;
        
CREATE TRIGGER updatePublisher
		AFTER INSERT ON tbl_publisher FOR EACH ROW
	INSERT INTO tbl_publisher
	SET action = 'update',
		publisherId = OLD.publisherId,
		publisherName = OLD.publisherName,
		publisherAddress = OLD.publisherAddress;
        
CREATE TRIGGER addLibBranch
		BEFORE INSERT ON tbl_library_branch FOR EACH ROW
	INSERT INTO tbl_library_branch
	SET action = 'add',
		branchId = NEW.branchId,
		branchName = NEW.branchName,
		branchAddress = NEW.branchAddress;
        
CREATE TRIGGER updateLibBranch
		BEFORE INSERT ON tbl_library_branch FOR EACH ROW
	INSERT INTO tbl_library_branch
	SET action = 'update',
		branchId = OLD.branchId,
		branchName = OLD.branchName,
		branchAddress = OLD.branchAddress;
        

    
	