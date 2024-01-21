-- SQL script that creates a trigger that decreases the quantity
-- of an item after adding a new order.
DELLIMETER $$
CREATE TRIGGER `update_item`
AFTER INSERT ON `orders`
FOR EACH ROW
	BEGIN
		UPDATE `item`
		SET quantity = quantity - NEW.`number`
		WHERE `name` = NEW.`item_name`;
	END $$
DELIMETER ;
