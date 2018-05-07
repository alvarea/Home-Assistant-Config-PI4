# -----------------------------------------------------------------------------#
#                                                                              #
#  FAMILY TRACKING Control Home/Away                                           #
#                                                                              #
# -----------------------------------------------------------------------------#
#
# You can call the script using the following:
# - service: python_script.meta_alarm_trigger
#   data_template:
#     entity_id: '{{trigger.entity_id}}'

# JSON: {"entity_id" : "binary_sensor.motion_sensor_158d0001e55903" }
# JSON: {"entity_id" : "alarm_control_panel.ha" }

Zona_Entrada = ['binary_sensor.motion_sensor_158d0001e55903',       # Sensor Presencia Entrada
                'binary_sensor.door_window_sensor_158d00022b393c'   # Sensor Puerta Entrada
]

Zona_Salon = ['binary_sensor.motion_sensor_158d0001e05661',         # Sensor Presencia Salón
              'binary_sensor.door_window_sensor_158d000201e2e7'     # Sensor Puerta Salón
]

Zona_Estudio = ['binary_sensor.motion_sensor_158d0001e464a6']        # Sensor Presencia Estudio

Zona_Dorm_PAF = ['binary_sensor.door_window_sensor_158d000201dddb']  # Sensor Ventana PAF

# Get the entity that triggered the automation
triggeredEntity = data.get('entity_id')

newSensor = hass.states.get(triggeredEntity)
newDeviceClass = newSensor.attributes.get('device_class')
newState = newSensor.attributes.get('friendly_name')

if triggeredEntity in Zona_Entrada:
    newIcon = 'mdi:door'
elif triggeredEntity in Zona_Salon:
    newIcon = 'mdi:sofa'
elif triggeredEntity in Zona_Estudio:
    newIcon = 'mdi:laptop-mac'
elif triggeredEntity in Zona_Dormitorio:
    newIcon = 'mdi:window-closed'
else:
    newState = ''
    newIcon = 'mdi:security-home'
    newDeviceClass = None

# Create device_tracker.meta entity
hass.states.set('sensor.alarm_zone', newState, {
    'icon': newIcon,
    'device_class': newDeviceClass
})