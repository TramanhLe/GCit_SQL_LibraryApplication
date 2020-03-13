-- Adam Kiertscher
CREATE PROCEDURE `X_branchNameToBranchId`(IN inputBranchName varchar(50))
BEGIN
	SELECT branchId
	FROM tbl_library_branch
    WHERE branchName=inputBranchName;
END