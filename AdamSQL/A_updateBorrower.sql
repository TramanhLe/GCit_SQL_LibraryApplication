-- Adam Kiertscher
CREATE PROCEDURE `A_updateBorrower`(IN inputCardNo int,
									IN newName varchar(50),
									IN newAddress varchar(50),
                                    IN newPhone varchar(50))
BEGIN
	UPDATE tbl_borrower b
    SET b.name = newName,
	b.address = newAddress,
	b.phone = newPhone
    WHERE b.cardNo = inputCardNo;
END