insert into equipment_equipment (price, restricted, rarity, category_id, gear_id) select price,restricted,rarity,category_id,entry_ptr_id from equipment_gear where equipment_gear.price > 0;
alter table equipment_gear drop column price;
alter table equipment_gear drop column restricted;
alter table equipment_gear drop column rarity;
alter table equipment_gear drop foreign key category_id_refs_id_84ce0d00;
alter table equipment_gear drop column category_id;
