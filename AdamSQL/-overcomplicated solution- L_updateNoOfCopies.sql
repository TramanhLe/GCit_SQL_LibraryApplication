-- Adam Kiertscher
CREATE PROCEDURE `L_updateNoOfCopies`(IN inputBranchId int,
										IN inputBookId int,
										IN newNoOfCopies int)
BEGIN
	UPDATE tbl_book_copies bc
		INNER JOIN tbl_book b ON b.bookId = inputBookId
		INNER JOIN tbl_library_branch lb ON lb.branchId = inputBranchId
    SET noOfCopies = newNoOfCopies
    WHERE bc.bookId = inputBookId
		AND bc.branchId = inputBranchId;
END