-- Adam Kiertscher
CREATE PROCEDURE `A_updateBook`(IN inputBookId int,
										IN newtitle varchar(50),
										IN newPubId int)
BEGIN
	UPDATE tbl_book
    SET title = newTitle
		AND pubId = newPubId
    WHERE bookId=inputBookId;
END