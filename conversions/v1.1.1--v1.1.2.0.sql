alter table equipment_weapon drop foreign key skill_id_refs_id_ab0b0a13;
alter table equipment_weapon change column `skill_id` `weapon_skill` integer NOT NULL;
alter table equipment_weapon drop foreign key range_band_id_refs_id_74964dec;
alter table equipment_weapon change column `range_band_id` `weapon_range` integer NOT NULL;
alter table transportation_vehicle drop foreign key sensor_range_id_refs_id_9f82dcb0;
alter table transportation_vehicle change column `sensor_range_id` `sensor_range` integer NOT NULL;



