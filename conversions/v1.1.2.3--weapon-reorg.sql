insert into equipment_equipment (price, restricted, rarity, category_id, gear_id) select price,restricted,rarity,category_id,entry_ptr_id from equipment_gear where equipment_gear.price > 0;
