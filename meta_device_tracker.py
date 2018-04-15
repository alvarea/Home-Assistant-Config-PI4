# -----------------------------------------------------------------------------#
#                                                                              #
#  FAMILY TRACKING Control Home/Away                                           #
#                                                                              #
# -----------------------------------------------------------------------------#
#
# Combine multiple device trackers into one entity
# You can call the script using the following:
# - service: python_script.meta_device_tracker
#   data_template:
#     entity_id: '{{trigger.entity_id}}'

# OPTIONS
#
# List the trackers for each individual
#
MFC_Trackers = ['device_tracker.mfc_iphone_nmap',
                'device_tracker.mfc_iphone_owntrack',
                'device_tracker.mfc_ios',
                'device_tracker.e3c67d6b51bf445ba241a0045bfe0222']

AAC_Trackers = ['device_tracker.aac_iphone_nmap',
                'device_tracker.aac_iphone_owntrack',
                'device_tracker.aac_ios',
                'device_tracker.b8b52a3bf0384e72a268705d9b06e496']

# Get the entity that triggered the automation
triggeredEntity = data.get('entity_id')

# Set friendly name and the metatracker name based on the entity that triggered
if triggeredEntity in AAC_Trackers:
    newFriendlyName = 'Agustín Tracker'
    newEntityPicture = '/local/AAC_2017_0.jpg'
    metatrackerName = 'device_tracker.meta_aac'
elif triggeredEntity in MFC_Trackers:
    newFriendlyName = 'Malen Tracker'
    newEntityPicture = '/local/MFC_2017_0.jpeg'
    metatrackerName = 'device_tracker.meta_mfc'
else:
    newFriendlyName = None
    metatrackerName = None

# Get current & new state
newState = hass.states.get(triggeredEntity)
currentState = hass.states.get(metatrackerName)
# Get New data
newSource = newState.attributes.get('source_type')
newFriendlyName_temp = newState.attributes.get('friendly_name')

if newState.state is not None:
    newStatus = newState.state
else:
    newStatus = currentState.state

# Create device_tracker.meta entity
hass.states.set(metatrackerName, newStatus, {
    'friendly_name': newFriendlyName,
    'entity_picture': newEntityPicture,
    'source_type': newSource,
    'update_source': triggeredEntity,
    'custom_ui_state_card': 'state-card-custom-ui',
    'show_last_changed': 'true'
})