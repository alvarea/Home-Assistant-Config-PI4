home = 0
for entity_id in hass.states.entity_ids('device_tracker'):
    state = hass.states.get(entity_id)
    if((state.object_id == '93e3d52336a54d4d898b204abdf3ee94' or
        state.object_id == 'b8b52a3bf0384e72a268705d9b06e496' or
        state.object_id == 'bef743fa74f2464ba458612ad3e1c195' or
        state.object_id == 'e3c67d6b51bf445ba241a0045bfe0222') and
        state.state == 'home'):
            home = home + 1

hass.states.set('sensor.family_home', home, {
    'unit_of_measurement': 'personas',
    'friendly_name': '¿Gente en Casa?'
})

