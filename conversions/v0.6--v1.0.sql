insert into base_system select * from oldbooks_system;
insert into base_book select * from oldbooks_book;
insert into base_category select * from oldbooks_category;
insert into base_entry (id, name, image, notes, category_id) SELECT id,name,image,notes,category_id FROM oldbooks_item;
insert into base_index select * from oldbooks_index;

insert into equipment_gear (entry_ptr_id, price, restricted, encumbrance, rarity) select id,price,restricted,encumbrance,rarity from oldbooks_item;
  
insert into equipment_skill select * from oldbooks_skill;
insert into equipment_rangeband select * from oldbooks_rangeband;
insert into equipment_weapon select * from oldbooks_weapon;
insert into equipment_armor select * from oldbooks_armor;
insert into equipment_attachment (gear_ptr_id, hard_points) select item_ptr_id, hard_points from oldbooks_attachment;

insert into transportation_vehicle select * from oldbooks_vehicle;
insert into transportation_crewdescriptor select * from oldbooks_crewdescriptor;
insert into transportation_crewentry select * from oldbooks_crewentry;
insert into transportation_starship select * from oldbooks_starship;
insert into transportation_hyperdrive select * from oldbooks_hyperdrive;
insert into transportation_consumable select * from oldbooks_consumable;
insert into transportation_vehicleattachment (attachment_ptr_id, by_silhoutte) select a.item_ptr_id,a.by_silhoutte from oldbooks_attachment a, oldbooks_item i where a.item_ptr_id = i.id and ( i.category_id=26 or i.category_id=27);
update base_category set model=7 where id=26 or id=27;
