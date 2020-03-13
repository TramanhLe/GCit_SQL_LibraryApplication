-- Adam Kiertscher
-- ***4th param must be in DATETIME
-- EX: YYYY-MM-DDTHH:MM:SS
--    '2012-04-06T12:23:45'

CREATE PROCEDURE `L_changeDueDate`(IN oldBranchId int,
										IN oldBookId int,
                                        IN oldCardNo int,
										IN newDueDate DATETIME)
BEGIN
	UPDATE tbl_book_loans
    SET dueDate = newDueDate
    WHERE oldBranchId IN (SELECT lb.branchId
						FROM tbl_library_branch lb
                        WHERE lb.branchId=oldBranchId)
    AND oldBookId IN (SELECT b.bookId
						FROM tbl_book b
                        WHERE b.bookId=oldBookId)
	AND oldCardNo IN (SELECT bo.cardNo
						FROM tbl_borrower bo
                        WHERE bo.cardNo=oldCardNo);
END