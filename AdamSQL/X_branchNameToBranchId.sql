CREATE PROCEDURE `X_branchNameToBranchId`(IN branchInput varchar(50))
BEGIN
	SELECT branchId
	FROM tbl_library_branch
    WHERE branchName=branchInput;
END