-- Adam Kiertscher
CREATE PROCEDURE `X_cardNoToName` (IN inputCardNo int)
BEGIN
	SELECT b.name
	FROM borrower b
    WHERE cardNo=inputCardNo;
END