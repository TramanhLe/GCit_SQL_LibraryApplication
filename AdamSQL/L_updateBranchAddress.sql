CREATE PROCEDURE `L_updateBranchAddress` (IN oldBranchName varchar(50), IN newBranchAddress varchar(50))
BEGIN
	UPDATE tbl_library_branch
    SET branchAddress=newBranchAddress
    WHERE branchName=oldBranchName;
END