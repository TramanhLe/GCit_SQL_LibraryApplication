-- Adam Kiertscher
CREATE PROCEDURE `L_updateNoOfCopies`(IN oldBranchId int,
										IN oldBookId int,
										IN newNoOfCopies int)
BEGIN
	UPDATE tbl_book_copies
    SET noOfCopies=newNoOfCopies
    WHERE oldBookId IN (SELECT b.bookId
						FROM tbl_book b
                        WHERE b.bookId=oldBookId)
	AND oldBranchId IN (SELECT lb.branchId
						FROM tbl_library_branch lb
                        WHERE lb.branchId=oldBranchId);
END