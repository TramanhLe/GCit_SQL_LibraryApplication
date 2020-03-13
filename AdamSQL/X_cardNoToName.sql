-- Adam Kiertscher

CREATE PROCEDURE `X_cardNoToName` (IN cardNoInput int)
BEGIN
	SELECT b.name
	FROM borrower b
    WHERE cardNo=cardNoInput;
END