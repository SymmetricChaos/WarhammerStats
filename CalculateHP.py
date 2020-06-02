## Need to adjust this to python code.


function unitHealth(data) {
  let lu = data.land_unit;

  let engine_count = lu.num_engines;
  let engine_hp = engine_count > 0 && lu.engine !== null ? lu.engine.battle_entity.hit_points : 0;

  // Each engine receives the number of mounts specified (i.e. chariots)
  let mount_count = engine_count > 0 ? lu.num_mounts * engine_count : lu.num_mounts;
  let = mount_count > 0 && lu.mount !== null ? lu.mount.battle_entity.hit_points : 0;

  let unit_count = data.num_men;
  let unit_hp = lu.battle_entity.hit_points;

  // Add bonus to proper level
  let bonus = lu.bonus_hit_points;
  if (engine_count > 0) {
    engine_hp += bonus;
    if (mount_count > 0) {
      engine_hp += 1;
    } else if (unit_count > 1) {
      // wh_main_grn_art_doom_diver_catapult needs this to be accurate but then
      // wh_dlc04_vmp_veh_mortis_engine_0 is wrong with it... WTF CA!!!
      // if (data.caste == "War Machine") {
      if (engine_count > 1) {
        unit_hp += bonus;
      }
    }
  } else if (mount_count > 0) {
    mount_hp += bonus;
  } else {
    unit_hp += bonus;
  }

  let hp = (unit_count * unit_hp + mount_count * mount_hp + engine_count * engine_hp) * unitSizeMultiplier[globalSettings().unit_size]

  return Math.round(hp);
};
      
      
(unit_count * unit_hp + mount_count * mount_hp + engine_count * engine_hp) * unitSizeMultiplier[globalSettings().unit_size]
