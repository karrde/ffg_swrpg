BEGIN;
CREATE TABLE `base_system` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `name` varchar(100) NOT NULL,
    `initials` varchar(10) NOT NULL
)
;
CREATE TABLE `base_book` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `name` varchar(100) NOT NULL,
    `initials` varchar(10) NOT NULL,
    `num_pages` integer NOT NULL,
    `system_id` integer NOT NULL,
    `product_key` varchar(10) NOT NULL
)
;
ALTER TABLE `base_book` ADD CONSTRAINT `system_id_refs_id_8b9c127e` FOREIGN KEY (`system_id`) REFERENCES `base_system` (`id`);
CREATE TABLE `base_category` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `model` integer NOT NULL,
    `name` varchar(50) NOT NULL
)
;
CREATE TABLE `base_entry` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `name` varchar(100) NOT NULL,
    `image` varchar(100),
    `notes` varchar(500) NOT NULL,
    `category_id` integer NOT NULL
)
;
ALTER TABLE `base_entry` ADD CONSTRAINT `category_id_refs_id_0cad9688` FOREIGN KEY (`category_id`) REFERENCES `base_category` (`id`);
CREATE TABLE `base_index` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `book_id` integer NOT NULL,
    `page` integer NOT NULL,
    `entry_id` integer NOT NULL,
    `aka` varchar(100) NOT NULL
)
;
ALTER TABLE `base_index` ADD CONSTRAINT `book_id_refs_id_ab9f7ca9` FOREIGN KEY (`book_id`) REFERENCES `base_book` (`id`);
ALTER TABLE `base_index` ADD CONSTRAINT `entry_id_refs_id_cc68140e` FOREIGN KEY (`entry_id`) REFERENCES `base_entry` (`id`);

COMMIT;
BEGIN;
CREATE TABLE `equipment_skill` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `skill` integer NOT NULL,
    `name` varchar(50) NOT NULL
)
;
CREATE TABLE `equipment_rangeband` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `range_band` integer NOT NULL,
    `name` varchar(50) NOT NULL
)
;
CREATE TABLE `equipment_gear` (
    `entry_ptr_id` integer NOT NULL PRIMARY KEY,
    `price` integer NOT NULL,
    `restricted` bool NOT NULL,
    `encumbrance` integer NOT NULL,
    `rarity` integer NOT NULL
)
;
ALTER TABLE `equipment_gear` ADD CONSTRAINT `entry_ptr_id_refs_id_a0283418` FOREIGN KEY (`entry_ptr_id`) REFERENCES `base_entry` (`id`);
CREATE TABLE `equipment_weapon` (
    `gear_ptr_id` integer NOT NULL PRIMARY KEY,
    `skill_id` integer NOT NULL,
    `damage` integer NOT NULL,
    `critical` integer NOT NULL,
    `range_band_id` integer NOT NULL,
    `hard_points` integer NOT NULL,
    `special` varchar(200) NOT NULL
)
;
ALTER TABLE `equipment_weapon` ADD CONSTRAINT `gear_ptr_id_refs_entry_ptr_id_b2a90fae` FOREIGN KEY (`gear_ptr_id`) REFERENCES `equipment_gear` (`entry_ptr_id`);
ALTER TABLE `equipment_weapon` ADD CONSTRAINT `skill_id_refs_id_ab0b0a13` FOREIGN KEY (`skill_id`) REFERENCES `equipment_skill` (`id`);
ALTER TABLE `equipment_weapon` ADD CONSTRAINT `range_band_id_refs_id_74964dec` FOREIGN KEY (`range_band_id`) REFERENCES `equipment_rangeband` (`id`);
CREATE TABLE `equipment_armor` (
    `gear_ptr_id` integer NOT NULL PRIMARY KEY,
    `defense` integer NOT NULL,
    `soak` integer NOT NULL,
    `hard_points` integer NOT NULL
)
;
ALTER TABLE `equipment_armor` ADD CONSTRAINT `gear_ptr_id_refs_entry_ptr_id_c67050c1` FOREIGN KEY (`gear_ptr_id`) REFERENCES `equipment_gear` (`entry_ptr_id`);
CREATE TABLE `equipment_attachment` (
    `gear_ptr_id` integer NOT NULL PRIMARY KEY,
    `hard_points` integer NOT NULL
)
;
ALTER TABLE `equipment_attachment` ADD CONSTRAINT `gear_ptr_id_refs_entry_ptr_id_0248c256` FOREIGN KEY (`gear_ptr_id`) REFERENCES `equipment_gear` (`entry_ptr_id`);

COMMIT;
BEGIN;
CREATE TABLE `transportation_vehicle` (
    `gear_ptr_id` integer NOT NULL PRIMARY KEY,
    `silhoutte` integer NOT NULL,
    `speed` integer NOT NULL,
    `handling` integer NOT NULL,
    `def_fore` integer NOT NULL,
    `def_port` integer NOT NULL,
    `def_starboard` integer NOT NULL,
    `def_aft` integer NOT NULL,
    `armor_value` integer NOT NULL,
    `hull_trauma` integer NOT NULL,
    `system_strain` integer NOT NULL,
    `model` varchar(100) NOT NULL,
    `manufacturer` varchar(100) NOT NULL,
    `max_altitude` integer,
    `sensor_range_id` integer NOT NULL,
    `passenger` integer NOT NULL,
    `hard_points` integer NOT NULL,
    `weapon_count` integer NOT NULL
)
;
ALTER TABLE `transportation_vehicle` ADD CONSTRAINT `sensor_range_id_refs_id_9f82dcb0` FOREIGN KEY (`sensor_range_id`) REFERENCES `equipment_rangeband` (`id`);
ALTER TABLE `transportation_vehicle` ADD CONSTRAINT `gear_ptr_id_refs_entry_ptr_id_21331697` FOREIGN KEY (`gear_ptr_id`) REFERENCES `equipment_gear` (`entry_ptr_id`);
CREATE TABLE `transportation_crewdescriptor` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `description` varchar(100) NOT NULL
)
;
CREATE TABLE `transportation_crewentry` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `quantity` integer NOT NULL,
    `description_id` integer NOT NULL,
    `vehicle_id` integer NOT NULL
)
;
ALTER TABLE `transportation_crewentry` ADD CONSTRAINT `vehicle_id_refs_gear_ptr_id_5972abcf` FOREIGN KEY (`vehicle_id`) REFERENCES `transportation_vehicle` (`gear_ptr_id`);
ALTER TABLE `transportation_crewentry` ADD CONSTRAINT `description_id_refs_id_7263f6ce` FOREIGN KEY (`description_id`) REFERENCES `transportation_crewdescriptor` (`id`);
CREATE TABLE `transportation_starship` (
    `vehicle_ptr_id` integer NOT NULL PRIMARY KEY,
    `navicomputer` integer NOT NULL
)
;
ALTER TABLE `transportation_starship` ADD CONSTRAINT `vehicle_ptr_id_refs_gear_ptr_id_eac10554` FOREIGN KEY (`vehicle_ptr_id`) REFERENCES `transportation_vehicle` (`gear_ptr_id`);
CREATE TABLE `transportation_hyperdrive` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `rank` integer NOT NULL,
    `class_value` integer NOT NULL,
    `starship_id` integer NOT NULL
)
;
ALTER TABLE `transportation_hyperdrive` ADD CONSTRAINT `starship_id_refs_vehicle_ptr_id_7e4e185d` FOREIGN KEY (`starship_id`) REFERENCES `transportation_starship` (`vehicle_ptr_id`);
CREATE TABLE `transportation_consumable` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `value` integer NOT NULL,
    `period` integer NOT NULL,
    `starship_id` integer NOT NULL UNIQUE
)
;
ALTER TABLE `transportation_consumable` ADD CONSTRAINT `starship_id_refs_vehicle_ptr_id_d0ba8333` FOREIGN KEY (`starship_id`) REFERENCES `transportation_starship` (`vehicle_ptr_id`);
CREATE TABLE `transportation_vehicleattachment` (
    `attachment_ptr_id` integer NOT NULL PRIMARY KEY,
    `by_silhoutte` bool NOT NULL
)
;
ALTER TABLE `transportation_vehicleattachment` ADD CONSTRAINT `attachment_ptr_id_refs_gear_ptr_id_e578fe6f` FOREIGN KEY (`attachment_ptr_id`) REFERENCES `equipment_attachment` (`gear_ptr_id`);

COMMIT;
