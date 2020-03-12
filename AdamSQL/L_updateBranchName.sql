CREATE PROCEDURE `L_updateBranchName` (IN oldBranchName varchar(50), newBranchName varchar(50))
BEGIN
	UPDATE tbl_library_branch
    SET branchName=newBranchName
    WHERE branchName=oldBranchName;
END