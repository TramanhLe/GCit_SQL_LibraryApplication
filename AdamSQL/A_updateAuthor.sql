-- Adam Kiertscher
CREATE PROCEDURE `A_updateAuthor`(IN inputAuthorId int,
								  IN newAuthorName varchar(50))
BEGIN
	UPDATE tbl_author
    SET authorName = newAuthorName
    WHERE authorId = inputAuthorId;
END