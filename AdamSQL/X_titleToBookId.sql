CREATE PROCEDURE `X_titleToBookId`(IN titleInput varchar(50))
BEGIN
	SELECT DISTINCT bookId 	-- unsure if DISTINCT is needed, using just in case
	FROM tbl_book
    WHERE title=titleInput;
END