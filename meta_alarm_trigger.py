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



Zona_Entrada = ['binary_sensor.motion_sensor_158d0001e55903',       # Sensor Presencia Entrada
                'binary_sensor.door_window_sensor_158d00022b393c'   # Sensor Puerta Entrada
]

Zona_Salon = ['binary_sensor.motion_sensor_158d0001e05661',         # Sensor Presencia Salón
              'binary_sensor.door_window_sensor_158d000201e2e7'     # Sensor Puerta Salón
]

Zona_Estudio = ['binary_sensor.motion_sensor_158d0001e464a6'        # Sensor Presencia Estudio
]

Zona_Dorm_PAF = ['binary_sensor.door_window_sensor_158d000201dddb'  # Sensor Ventana PAF
]

# Get the entity that triggered the automation
triggeredEntity = data.get('entity_id')

metaAlarmZone = 'binary_sensor.alarm_zone'

# Set friendly name and the metatracker name based on the entity that triggered
if triggeredEntity in Zona_Entrada:
    newFriendlyName = 'Zona Entrada'
    newIcon = 'mdi:door'
elif triggeredEntity in 'Zona_Salon':
    newFriendlyName = 'Zona Salón'
    newIcon = 'mdi:sofa'
elif triggeredEntity in 'Zona_Estudio':
    newFriendlyName = 'Zona Estudio'
    newIcon = 'mdi:laptop-mac'
elif triggeredEntity in 'Zona_Dormitorio':
    newFriendlyName = 'Zona Dormitorio PAF'
    newIcon = 'mdi:window-closed'
else:
    metaAlarmZone = None
    newFriendlyName = None
    newIcon = None

# Get current & new state
newState = hass.states.get(triggeredEntity)
currentState = hass.states.get(metaAlarmZone)

if newState.state is not None:
    newStatus = newState.state
else:
    newStatus = currentState.state

# Get New data
newDeviceClass = newState.attributes.get('device_class')

# Create device_tracker.meta entity
hass.states.set(metaAlarmZone, newStatus, {
    'friendly_name': newFriendlyName,
    'icon': newIcon,
    'device_class': newDeviceClass
})