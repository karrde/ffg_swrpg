alter table transportation_vehicle change `model` `vehicle_model` varchar(100) NOT NULL;
alter table base_entry drop foreign key category_id_refs_id_0cad9688;
alter table base_entry add `model` varchar(100) NOT NULL;
rename table base_category to equipment_category;
alter table equipment_gear add `category_id` integer NOT NULL;
update equipment_gear,base_entry set equipment_gear.category_id=base_entry.category_id where equipment_gear.entry_ptr_id=base_entry.id;
ALTER TABLE `equipment_gear` ADD CONSTRAINT `category_id_refs_id_84ce0d00` FOREIGN KEY (`category_id`) REFERENCES `equipment_category` (`id`);
