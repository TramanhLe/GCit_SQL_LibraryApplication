-- Adam Kiertscher
CREATE PROCEDURE `B_addBookLoan`(IN inputBookId int,
										IN inputBranchId int,
										IN inputCardNo int)
BEGIN
	INSERT INTO tbl_book_loans
    VALUES
    (
        inputBookId,
		inputBranchId,
		inputCardNo,
		NOW(),
        DATE_ADD(NOW(), INTERVAL +14 DAY)        
    );
END