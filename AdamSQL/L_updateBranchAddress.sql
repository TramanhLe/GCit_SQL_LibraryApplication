-- Adam Kiertscher
CREATE PROCEDURE `L_updateBranchAddress` (IN branchIdInput int, IN newBranchAddress varchar(50))
BEGIN
	UPDATE tbl_library_branch
    SET branchAddress=newBranchAddress
    WHERE branchId=branchIdInput;
END