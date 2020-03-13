-- Adam Kiertscher
CREATE PROCEDURE `A_updateBook`(IN oldBookId int,
										IN newtitle varchar(50),
										IN newPubId int)
BEGIN
	UPDATE tbl_book
    SET title = newTitle
		AND pubId = newPubId
    WHERE bookId=oldBookId;
END