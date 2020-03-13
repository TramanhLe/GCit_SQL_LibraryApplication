-- Adam Kiertscher
CREATE PROCEDURE `X_titleToBookId`(IN inputTitle varchar(50))
BEGIN
	SELECT DISTINCT bookId 	-- unsure if DISTINCT is needed, using just in case
	FROM tbl_book
    WHERE title=inputTitle;
END