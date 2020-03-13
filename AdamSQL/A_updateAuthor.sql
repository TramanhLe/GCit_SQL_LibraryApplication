-- Adam Kiertscher
CREATE PROCEDURE `A_updateAuthor`(IN oldAuthorId int,
								  IN newAuthorName varchar(50))
BEGIN
	UPDATE tbl_author
    SET authorName = newAuthorName
    WHERE authorId = oldAuthorId;
END