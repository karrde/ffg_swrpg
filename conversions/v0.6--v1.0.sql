insert into base_system select * from oldbooks_system;
insert into base_book select * from oldbooks_book;
insert into base_entry (id, name, image, notes) SELECT id,name,image,notes FROM oldbooks_item;
insert into base_index select * from oldbooks_index;

insert into equipment_category select * from oldbooks_category;
insert into equipment_item (entry_ptr_id, price, restricted, encumbrance, rarity, category_id) select id, price, restricted, encumbrance, rarity, category_id from oldbooks_item;
  
insert into equipment_skill select * from oldbooks_skill;
insert into equipment_rangeband select * from oldbooks_rangeband;
insert into equipment_weapon select * from oldbooks_weapon;
insert into equipment_armor select * from oldbooks_armor;
insert into equipment_attachment select * from oldbooks_attachment;
insert into equipment_vehicle select * from oldbooks_vehicle;
insert into equipment_crewdescriptor select * from oldbooks_crewdescriptor;
insert into equipment_crewentry select * from oldbooks_crewentry;
insert into equipment_starship select * from oldbooks_starship;
insert into equipment_hyperdrive select * from oldbooks_hyperdrive;
insert into equipment_consumable select * from oldbooks_consumable;
       