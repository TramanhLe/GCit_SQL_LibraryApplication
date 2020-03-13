-- Adam Kiertscher
CREATE PROCEDURE `A_updateBranch`(IN inputBranchId int,
										IN newBranchName varchar(50),
										IN newBranchAddress varchar(50))
BEGIN
	UPDATE tbl_library_branch
    SET BranchName = newBranchName
		AND BranchAddress = newBranchAddress
    WHERE inputBranchId = BranchId;
END