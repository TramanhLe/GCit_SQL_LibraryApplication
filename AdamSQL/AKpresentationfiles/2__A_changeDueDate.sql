-- Adam Kiertscher
-- DATETIME input format: '2015-11-05 14:29:36'

CREATE PROCEDURE `A_changeDueDate`(IN inputBranchId int,
										IN inputBookId int,
                                        IN inputCardNo int,
										IN newDueDate DATETIME)
BEGIN
	UPDATE tbl_book_loans bl
		INNER JOIN tbl_book b ON b.bookId = inputBookId
        INNER JOIN tbl_borrower bo ON bo.cardNo = inputCardNo
        INNER JOIN tbl_library_branch lb ON lb.branchId = inputBranchId
    SET dueDate = newDueDate
    WHERE bl.bookId = inputBookId
		AND bl.cardNo = inputCardNo
		AND bl.branchId = inputBranchId;    
END