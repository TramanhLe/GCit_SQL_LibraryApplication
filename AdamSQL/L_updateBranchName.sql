-- Adam Kiertscher
CREATE PROCEDURE `L_updateBranchName` (IN oldBranchId int, newBranchName varchar(50))
BEGIN
	UPDATE tbl_library_branch
    SET branchName=newBranchName
    WHERE branchId=oldBranchId;
END