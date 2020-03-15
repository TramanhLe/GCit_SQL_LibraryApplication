-- Adam Kiertscher
CREATE PROCEDURE `X_existingCopies` (IN inputBranchId int, IN inputBookId int)
BEGIN
	SELECT bc.noOfCopies
	FROM tbl_book_copies bc, tbl_library_branch lb
    WHERE lb.branchId=inputBranchId
		AND bc.bookId=inputBookId
	GROUP BY lb.branchName;
END
