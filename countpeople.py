home = 0
for entity_id in hass.states.entity_ids('input_boolean'):
    state = hass.states.get(entity_id)
    if(state.object_id in ['home_aac','home_mfc','home_paf','home_aaf'] and state.state == 'on'):
        home = home + 1

hass.states.set('sensor.family_home', home, {
    'unit_of_measurement': 'personas',
    'friendly_name': '¿Gente en Casa?'
})
