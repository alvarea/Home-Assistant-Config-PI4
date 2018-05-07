home = 0
for entity_id in hass.states.entity_ids('binary_sensor'):
    state = hass.states.get(entity_id)
    if(state.object_id in ['family_home_mfc','family_home_aac','family_home_paf','family_home_aaf'] and state.state == 'on'):
        home = home + 1

hass.states.set('sensor.family_home', home, {
    'unit_of_measurement': 'personas',
    'friendly_name': '¿Gente en Casa?'
})
