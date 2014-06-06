insert into books_system select * from oldbooks_system;
insert into books_book select * from oldbooks_book;
insert into books_entry (id, name, image, notes) SELECT id,name,image,notes FROM oldbooks_item;
insert into books_index select * from oldbooks_index;
insert into books_category select * from oldbooks_category;
insert into books_item (entry_ptr_id, price, restricted, encumbrance, rarity, category_id) select id, price, restricted, encumbrance, rarity, category_id from oldbooks_item;
  
insert into books_skill select * from oldbooks_skill;
insert into books_rangeband select * from oldbooks_rangeband;
insert into books_weapon select * from oldbooks_weapon;
insert into books_armor select * from oldbooks_armor;
insert into books_attachment select * from oldbooks_attachment;
insert into books_vehicle select * from oldbooks_vehicle;
insert into books_crewdescriptor select * from oldbooks_crewdescriptor;
insert into books_crewentry select * from oldbooks_crewentry;
insert into books_starship select * from oldbooks_starship;
insert into books_hyperdrive select * from oldbooks_hyperdrive;
insert into books_consumable select * from oldbooks_consumable;
       