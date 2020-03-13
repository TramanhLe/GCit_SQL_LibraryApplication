-- Adam Kiertscher
/*likely should be replaced with a procedure that
takes in branchId instead of branchName*/

CREATE PROCEDURE `L_updateBranchAddress` (IN oldBranchName varchar(50), IN newBranchAddress varchar(50))
BEGIN
	UPDATE tbl_library_branch
    SET branchAddress=newBranchAddress
    WHERE branchName=oldBranchName;
END