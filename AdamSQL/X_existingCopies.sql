-- Adam Kiertscher

CREATE PROCEDURE `X_existingCopies` (IN branchIdInput int, IN bookIdInput int)
BEGIN
	SELECT bc.noOfCopies
	FROM tbl_book_copies bc, tbl_library_branch lb
    WHERE lb.branchId=branchIdInput
		AND bc.bookId=bookIdInput
	GROUP BY lb.branchName;
END
