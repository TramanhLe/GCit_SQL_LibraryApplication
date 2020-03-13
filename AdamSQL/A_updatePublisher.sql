-- Adam Kiertscher
CREATE PROCEDURE `A_updatePublisher`(IN inputPublisherId int,
										IN newPublisherName varchar(50),
										IN newPublisherAddress varchar(50),
                                        IN newPublisherPhone int)
BEGIN
	UPDATE tbl_publisher
    SET publisherName = newPublisherName
		AND publisherAddress = newPublisherAddress
        AND publisherPhone = newPublisherPhone
    WHERE inputPublisherId = publisherId;
END