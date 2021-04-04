# -----------------------------------------------------------------------------#
#                                                                              #
# FAMILY TRACKING Control Home/Away                                           #
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
                'device_tracker.iphone_malen' ]
                'device_tracker.b6cd9e1f_4100_4cac_88d0_f4d6c044a4e6']

AAC_Trackers = ['device_tracker.aac_iphone_nmap',
                'device_tracker.aac_iphone_owntrack',
                'device_tracker.iphone_aac',
                'device_tracker.b8b52a3b_f038_4e72_a268_705d9b06e496']

PAF_Trackers = ['device_tracker.paf_iphone_nmap',
                'device_tracker.paf_iphone_owntrack',
                'device_tracker.iphone_paf',
                'device_tracker.863b93f2_f00f_4737_a35f_1ff0cce201a8']

AAF_Trackers = ['device_tracker.aaf_iphone_nmap',
                'device_tracker.a2f',
                'device_tracker.0b495ff5_94fc_4773_9644_f71df3c328ac']

# Get the entity that triggered the automation
triggeredEntity = data.get('entity_id')

# Set friendly name and the metatracker name based on the entity that triggered
if triggeredEntity in AAC_Trackers:
    newFriendlyName = 'Agustín Tracker'
    newEntityPicture = '/local/AAC_2017_co.jpeg'
    metatrackerName = 'device_tracker.meta_aac'
elif triggeredEntity in MFC_Trackers:
    newFriendlyName = 'Malen Tracker'
    newEntityPicture = '/local/MFC_2014_co.jpeg'
    metatrackerName = 'device_tracker.meta_mfc'
elif triggeredEntity in PAF_Trackers:
    newFriendlyName = 'Paloma Tracker'
    newEntityPicture = '/local/PAF_2017_co.png'
    metatrackerName = 'device_tracker.meta_paf'
elif triggeredEntity in AAF_Trackers:
    newFriendlyName = 'Agu Tracker'
    newEntityPicture = '/local/AAF_2017_co.png'
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