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
                'device_tracker.e3c67d6b_51bf_445b_a241_a0045bfe0222']

AAC_Trackers = ['device_tracker.aac_iphone_nmap',
                'device_tracker.aac_iphone_owntrack',
                'device_tracker.aac_ios',
                'device_tracker.b8b52a3b_f038_4e72_a268_705d9b06e496']

PAF_Trackers = ['device_tracker.paf_iphone_nmap',
                'device_tracker.paf_iphone_owntrack',
                'device_tracker.paf_ios',
                'device_tracker.93e3d523_36a5_4d4d_898b_204abdf3ee94']

AAF_Trackers = ['device_tracker.aaf_iphone_nmap',
                'device_tracker.bef743fa_74f2_464b_a458_612ad3e1c195']

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
elif triggeredEntity in PAF_Trackers:
    newFriendlyName = 'Paloma Tracker'
    newEntityPicture = '/local/PAF_2017_0.png'
    metatrackerName = 'device_tracker.meta_paf'
elif triggeredEntity in AAF_Trackers:
    newFriendlyName = 'Agu Tracker'
    newEntityPicture = '/local/AAF_2017_0.png'
    metatrackerName = 'device_tracker.meta_aaf'
else:
    newFriendlyName = None
    metatrackerName = None
    newEntityPicture = None

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